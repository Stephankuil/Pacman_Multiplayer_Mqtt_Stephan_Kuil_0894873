import sys
import pygame

from game.engine import Engine
from game.level_map import LevelMap
from game.ghosts import Ghost
from game.pacman import Pacman
from game.cheese import Cheese
from game.cherry import Cherry
from game.powerup import PowerUp
from game.mqtt_manager import MQTTManager


class Main:
    def __init__(self):
        self.player_id = sys.argv[1] if len(sys.argv) > 1 else "p1"
        self.is_host = self.player_id == "p1"

        self.level_map = LevelMap(LevelMap.MAP1, 19, 21, 1)

        self.cheese_list = [
            Cheese(x, y)
            for x, y in self.level_map.find_cheese_positions()
        ]

        self.ghosts = [
            Ghost(color="red", x_coordinate=9, y_coordinate=7),
            Ghost(color="pink", x_coordinate=9, y_coordinate=8),
            Ghost(color="cyan", x_coordinate=9, y_coordinate=9),
            Ghost(color="orange", x_coordinate=9, y_coordinate=10)
        ]

        self.pacman = Pacman(x_coordinate=10, y_coordinate=15)

        self.items = [
            PowerUp(x_coordinate=1, y_coordinate=2),
            PowerUp(x_coordinate=17, y_coordinate=2),
            PowerUp(x_coordinate=1, y_coordinate=16),
            PowerUp(x_coordinate=17, y_coordinate=16),
            Cherry(x_coordinate=9, y_coordinate=8)
        ]

        self.other_players = {}

        self.mqtt_manager = MQTTManager(
            self.player_id,
            self.pacman,
            self.other_players,
            self.ghosts,
            self.is_host

        )

        self.mqtt_manager.connect()

        self.screen = pygame.display.set_mode((600, 700))
        pygame.display.set_caption("Pacman")

        self.move_delay = 150
        self.last_move = 0

        self.last_ghost_move = 0
        self.ghost_move_delay = 500


    def loop(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            current_time = pygame.time.get_ticks()

            moved = False

            if current_time - self.last_move > self.move_delay:
                if keys[pygame.K_LEFT]:
                    self.pacman.move("LEFT", self.level_map)
                    moved = True

                elif keys[pygame.K_RIGHT]:
                    self.pacman.move("RIGHT", self.level_map)
                    moved = True

                elif keys[pygame.K_UP]:
                    self.pacman.move("UP", self.level_map)
                    moved = True

                elif keys[pygame.K_DOWN]:
                    self.pacman.move("DOWN", self.level_map)
                    moved = True

                if moved:
                    self.mqtt_manager.publish_move()
                    self.last_move = current_time

            for cheese in self.cheese_list:
                self.pacman.eat_cheese(cheese)

            for item in self.items:
                if isinstance(item, Cherry):
                    self.pacman.eat_cherry(item)

                if isinstance(item, PowerUp):
                    self.pacman.eat_powerup(item)

            if self.is_host:
                if current_time - self.last_ghost_move > self.ghost_move_delay:
                    for ghost in self.ghosts:
                        ghost.move_random(self.level_map)

                    self.mqtt_manager.publish_ghost_positions(self.ghosts)
                    self.last_ghost_move = current_time

            for ghost in self.ghosts:
                ghost.hit_pacman(self.pacman)

            self.draw()
            pygame.display.update()

        self.mqtt_manager.disconnect()
        pygame.quit()

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.level_map.draw(self.screen)

        for cheese in self.cheese_list:
            if not cheese.consumed:
                cheese.draw(self.screen)

        for item in self.items:
            if not item.consumed:
                item.draw(self.screen, (255, 0, 255))

        for pid, other in self.other_players.items():
            pygame.draw.circle(
                self.screen,
                (0, 0, 255),
                (
                    other["x"] * 30 + 15,
                    other["y"] * 30 + 15
                ),
                12
            )

        self.pacman.draw(self.screen)

        for ghost in self.ghosts:
            ghost.draw(self.screen)


if __name__ == "__main__":
    pygame.init()
    game = Main()
    game.loop()