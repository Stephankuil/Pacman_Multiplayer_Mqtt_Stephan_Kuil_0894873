import pygame

from engine import Engine
from levelmap import LevelMap
from cheese import Cheese
from pacman import Pacman
from cherry import Cherry
from powerup import Powerup

if __name__ == "__main__":
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

    engine.start_game()


    last_cherry_spawn = pygame.time.get_ticks()
    cherry_spawn_interval = 20000
    cherry.load_image()

    powerup.load_image()
    last_powerup_spawn = pygame.time.get_ticks()
    powerup_spawn_interval = 30000

    while engine.running:


        current_time = pygame.time.get_ticks()

        if current_time - last_cherry_spawn >= cherry_spawn_interval:
            cherry.respawn(game_map)
            last_cherry_spawn = current_time

        if current_time - last_powerup_spawn >= powerup_spawn_interval:
            powerup.respawn(game_map)
            last_powerup_spawn = current_time


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                engine.game_stop()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman.move("LEFT", game_map)
                elif event.key == pygame.K_RIGHT:
                    pacman.move("RIGHT", game_map)
                elif event.key == pygame.K_UP:
                    pacman.move("UP", game_map)
                elif event.key == pygame.K_DOWN:
                    pacman.move("DOWN", game_map)

            pacman.eat_cheese(cheese)
            pacman.eat_cherry(cherry)
            pacman.eat_powerup(powerup)

        engine.screen.fill((0, 0, 0))

        engine.draw_map(game_map)
        cheese.draw(engine.screen)
        pacman.draw(engine.screen)
        cherry.draw(engine.screen)
        powerup.draw(engine.screen)

        pygame.display.flip()
        engine.clock.tick(10)

    pygame.quit()