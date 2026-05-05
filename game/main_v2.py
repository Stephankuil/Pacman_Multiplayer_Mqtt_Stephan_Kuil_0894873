import pygame
import sys
#hallo
from mqtt_manager import MQTTManager
from engine import Engine
from levelmap import LevelMap
from cheese import Cheese
from pacman import Pacman
from cherry import Cherry
from powerup import Powerup
from ghosts import Ghost

if __name__ == "__main__":
    player_id = sys.argv[1] if len(sys.argv) > 1 else "p1"
    game_map = LevelMap(LevelMap.MAP1, 19, 21, 1)

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
        image_path="images/pacman2.png",
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
    mqtt_manager = MQTTManager(player_id, pacman, other_players)
    mqtt_manager.connect()

    is_host = player_id == "p1"


    engine.start_game()






    last_cherry_spawn = pygame.time.get_ticks()
    cherry_spawn_interval = 20000
    cherry.load_image()

    powerup.load_image()
    last_powerup_spawn = pygame.time.get_ticks()
    powerup_spawn_interval = 30000

    while engine.running:
        current_time = pygame.time.get_ticks()

        if is_host:
            if current_time - last_cherry_spawn >= cherry_spawn_interval:
                cherry.respawn(game_map)
                last_cherry_spawn = current_time

            if current_time - last_powerup_spawn >= powerup_spawn_interval:
                powerup.respawn(game_map)
                last_powerup_spawn = current_time

        if pacman.power_mode and current_time > pacman.power_mode_end_time:
            pacman.power_mode = False

            for ghost in ghosts:
                ghost.make_normal()

            print("⚡ Power mode OFF")

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
                    pacman.eat_cheese(cheese)
                    pacman.eat_cherry(cherry)

                    if pacman.eat_powerup(powerup):
                        for ghost in ghosts:
                            ghost.make_edible()

                    mqtt_manager.publish_move()

        if is_host:
            for ghost in ghosts:
                ghost.move_random(game_map)
                ghost.teleport_if_needed(game_map)

                if ghost.edible:
                    ghost.eaten_by_pacman(pacman)
                else:
                    ghost.hit_pacman(pacman)

            mqtt_manager.publish_world_state(ghosts, cherry, powerup, cheese)

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

            cheese.positions = set(tuple(position) for position in world["cheese_positions"])

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

            name_text = pygame.font.SysFont(None, 24).render(pid, True, (255, 255, 255))
            engine.screen.blit(name_text, (x, y - 20))

        pacman.draw(engine.screen)

        pygame.display.flip()
        engine.clock.tick(10)

    mqtt_manager.disconnect()
    pygame.quit()