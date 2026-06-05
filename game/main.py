import pygame
from game.engine import Engine
from game.level_map import LevelMap
from game.character import Character
from game.ghosts import Ghost
from game.pacman import Pacman
from game.gameobject import GameObject
from game.cheese import Cheese
from game.cherry import Cherry
from game.powerup import PowerUp
from game.item import Item


class Main():
    def __init__(self):

        self.level_map = LevelMap(LevelMap.MAP1, 19, 21, 1)
        self.cheese_list = [Cheese(x, y) for x, y in self.level_map.find_cheese_positions()]
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
        self.screen = pygame.display.set_mode((600, 700))
        pygame.display.set_caption("Pacman")

    def loop(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False



            # toetsenbord input
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.pacman.move("LEFT", self.level_map)

            if keys[pygame.K_RIGHT]:
                self.pacman.move("RIGHT", self.level_map)

            if keys[pygame.K_UP]:
                self.pacman.move("UP", self.level_map)

            if keys[pygame.K_DOWN]:
                self.pacman.move("DOWN", self.level_map)

            # game logica
            for cheese in self.cheese_list:
                self.pacman.eat_cheese(cheese)

            for item in self.items:
                if isinstance(item, Cherry):
                    self.pacman.eat_cherry(item)

                if isinstance(item, PowerUp):
                    self.pacman.eat_powerup(item)

            for ghost in self.ghosts:
                ghost.hit_pacman(self.pacman)

            self.draw()

            pygame.display.update()

        pygame.quit()

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.level_map.draw(self.screen)

        for cheese in self.cheese_list:
            cheese.draw(self.screen)

        for cherry in self.items:
            cherry.draw(self.screen, (255, 0, 255))

        self.pacman.draw(self.screen)

        for ghost in self.ghosts:
            ghost.draw(self.screen)






if __name__ == "__main__":
    pygame.init()
    game = Main()
    game.loop()