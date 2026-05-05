import pygame
import sys

from mqtt_manager import MQTTManager
from engine import Engine
from levelmap import LevelMap
from cheese import Cheese
from pacman import Pacman
from cherry import Cherry
from powerup import Powerup
from ghosts import Ghost
from scoreboard import Scoreboard

if __name__ == "__main__":
    player_id = sys.argv[1] if len(sys.argv) > 1 else "p1"
    is_host = player_id == "p1"

    game_map = LevelMap(LevelMap.MAP1, 19, 21, 1)

    scoreboard = Scoreboard()

    if is_host:
        scoreboard.add_player(player_id, player_id)


    cheese = Cheese(
        image_path="images/cheese3.png",
        positions=game_map.find_cheese_positions(),
        tile_size=40
    )

    cherry = Cherry(
        image_path="images/cherry3.png",
        tile_size=40,
        bonus_points=100
    )

    powerup = Powerup(
        image_path="images/power_up1.png",
        tile_size=40,
        spawn_points=50,
        amount=1
    )

    pacman = Pacman(
        x=1,
        y=1,
        image_path="images/pacman3.png",
        tile_size=40
    )

    engine = Engine(
        running=False,
        level=1,
        game_status="menu",
        number_of_players=1
    )

    ghosts = [
        Ghost(9, 9, "images/ghost1.png", "images/ghost_blue.png", 40),
        Ghost(8, 9, "images/ghost1.png", "images/ghost_blue.png", 40),
        Ghost(10, 9, "images/ghost1.png", "images/ghost_blue.png", 40),
        Ghost(9, 8, "images/ghost1.png", "images/ghost_blue.png", 40),
    ]

    other_players = {}

    mqtt_manager = MQTTManager(player_id, pacman, other_players, scoreboard, is_host)
    mqtt_manager.connect()

    engine.start_game()

    last_cherry_spawn = pygame.time.get_ticks()
    cherry_spawn_interval = 20000
    cherry.load_image()

    powerup.load_image()
    last_powerup_spawn = pygame.time.get_ticks()
    powerup_spawn_interval = 30000

    power_mode_end_time = 0
    while engine.running:
        current_time = pygame.time.get_ticks()

        # =========================
        # POWER MODE TIMER HOST
        # =========================
        if is_host and power_mode_end_time > 0 and current_time > power_mode_end_time:
            for ghost in ghosts:
                ghost.make_normal()

            power_mode_end_time = 0
            print("⚡ Host power mode OFF")

        # =========================
        # SPAWN ITEMS HOST ONLY
        # =========================
        if is_host:
            if current_time - last_cherry_spawn >= cherry_spawn_interval:
                cherry.respawn(game_map)
                last_cherry_spawn = current_time

                scoreboard.add_message("🍒 Cherry is gespawned")
                mqtt_manager.publish_scoreboard()

            if current_time - last_powerup_spawn >= powerup_spawn_interval:
                powerup.respawn(game_map)
                last_powerup_spawn = current_time

                scoreboard.add_message("⚡ Powerup is gespawned")
                mqtt_manager.publish_scoreboard()

        # =========================
        # LOCAL POWER MODE TIMER
        # =========================
        if pacman.power_mode and current_time > pacman.power_mode_end_time:
            pacman.power_mode = False

            for ghost in ghosts:
                ghost.make_normal()

            print("⚡ Power mode OFF")

        # =========================
        # INPUT
        # =========================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                engine.game_stop()

            moved = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman.move("LEFT", game_map)
                    moved = True

                elif event.key == pygame.K_RIGHT:
                    pacman.move("RIGHT", game_map)
                    moved = True

                elif event.key == pygame.K_UP:
                    pacman.move("UP", game_map)
                    moved = True

                elif event.key == pygame.K_DOWN:
                    pacman.move("DOWN", game_map)
                    moved = True

                if moved:
                    pacman.teleport_if_needed(game_map)

                    # =========================
                    # KAAS ETEN
                    # =========================
                    old_cheese_count = len(cheese.positions)
                    pacman.eat_cheese(cheese)

                    if len(cheese.positions) < old_cheese_count:

                        if is_host:
                            scoreboard.add_score(player_id, 10, "kaasje")
                            mqtt_manager.publish_scoreboard()

                        mqtt_manager.publish_cheese_eaten(
                            pacman.x_coordinate,
                            pacman.y_coordinate
                        )

                    # =========================
                    # CHERRY ETEN
                    # =========================
                    old_cherry_consumed = cherry.consumed
                    pacman.eat_cherry(cherry)

                    if cherry.consumed and not old_cherry_consumed:

                        if is_host:
                            scoreboard.add_score(player_id, 100, "cherry")
                            mqtt_manager.publish_scoreboard()

                        mqtt_manager.publish_item_eaten("cherry")

                    # =========================
                    # POWERUP ETEN
                    # =========================
                    if pacman.eat_powerup(powerup):

                        if is_host:
                            scoreboard.add_score(player_id, 50, "powerup")
                            mqtt_manager.publish_scoreboard()
                            power_mode_end_time = pygame.time.get_ticks() + 15000

                        mqtt_manager.publish_item_eaten("powerup")

                        for ghost in ghosts:
                            ghost.make_edible()

                    mqtt_manager.publish_move()

        # =========================
        # HOST LOGICA
        # =========================
        if is_host:

            # =========================
            # GHOSTS BEWEGEN + COLLISIONS
            # =========================
            for ghost in ghosts:
                ghost.move_random(game_map)
                ghost.teleport_if_needed(game_map)

                # host/p1 raakt ghost
                if ghost.x_coordinate == pacman.x_coordinate and ghost.y_coordinate == pacman.y_coordinate:
                    if ghost.edible:
                        ghost.eaten_by_pacman(pacman)

                        scoreboard.add_score(player_id, 200, "spookje")
                        mqtt_manager.publish_scoreboard()
                    else:
                        ghost.hit_pacman(pacman)

                # andere spelers raken ghost
                for pid, other in other_players.items():
                    if ghost.x_coordinate == other["x"] and ghost.y_coordinate == other["y"]:
                        if ghost.edible:
                            print(pid, "eet ghost")

                            ghost.x_coordinate = 9
                            ghost.y_coordinate = 9

                            scoreboard.add_score(pid, 200, "spookje")
                            mqtt_manager.publish_scoreboard()
                        else:
                            print(pid, "raakt ghost")

            # =========================
            # KAAS BERICHT VAN SPELER
            # =========================
            if mqtt_manager.cheese_eaten_message is not None:
                x = mqtt_manager.cheese_eaten_message["x"]
                y = mqtt_manager.cheese_eaten_message["y"]
                pid = mqtt_manager.cheese_eaten_message["player_id"]

                if pid != player_id:
                    if (x, y) in cheese.positions:
                        cheese.positions.remove((x, y))

                        scoreboard.add_score(pid, 10, "kaasje")
                        mqtt_manager.publish_scoreboard()

                mqtt_manager.cheese_eaten_message = None

            # =========================
            # ITEM BERICHT VAN SPELER
            # =========================
            if mqtt_manager.item_eaten_message is not None:
                item_type = mqtt_manager.item_eaten_message["item_type"]
                pid = mqtt_manager.item_eaten_message["player_id"]

                if pid != player_id:
                    if item_type == "cherry":
                        cherry.consumed = True

                        scoreboard.add_score(pid, 100, "cherry")
                        mqtt_manager.publish_scoreboard()

                    if item_type == "powerup":
                        powerup.consumed = True
                        power_mode_end_time = pygame.time.get_ticks() + 15000

                        scoreboard.add_score(pid, 50, "powerup")
                        mqtt_manager.publish_scoreboard()

                        for ghost in ghosts:
                            ghost.make_edible()

                mqtt_manager.item_eaten_message = None

            mqtt_manager.publish_world_state(ghosts, cherry, powerup, cheese)

        # =========================
        # CLIENT SYNC
        # =========================
        if not is_host and mqtt_manager.world_state is not None:
            world = mqtt_manager.world_state

            for index, ghost_data in enumerate(world["ghosts"]):
                ghosts[index].x_coordinate = ghost_data["x"]
                ghosts[index].y_coordinate = ghost_data["y"]

                if ghost_data["edible"]:
                    ghosts[index].make_edible()
                else:
                    ghosts[index].make_normal()

            cherry.x_coordinate = world["cherry"]["x"]
            cherry.y_coordinate = world["cherry"]["y"]
            cherry.consumed = world["cherry"]["consumed"]

            powerup.x_coordinate = world["powerup"]["x"]
            powerup.y_coordinate = world["powerup"]["y"]
            powerup.consumed = world["powerup"]["consumed"]

            cheese.positions = set(
                tuple(position) for position in world["cheese_positions"]
            )

        # =========================
        # DRAW
        # =========================
        engine.screen.fill((0, 0, 0))
        engine.draw_map(game_map)

        cheese.draw(engine.screen)
        cherry.draw(engine.screen)
        powerup.draw(engine.screen)

        for ghost in ghosts:
            ghost.draw(engine.screen)

        for pid, other in other_players.items():
            x = other["x"] * pacman.tile_size
            y = other["y"] * pacman.tile_size

            engine.screen.blit(pacman.image, (x, y))

        pacman.draw(engine.screen)

        pygame.display.flip()
        engine.clock.tick(10)