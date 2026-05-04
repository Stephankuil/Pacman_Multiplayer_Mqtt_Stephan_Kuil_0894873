import pygame
import os
from character import Character


class Pacman(Character):
    def __init__(self, x, y, image_path, tile_size):
        super().__init__(x, y, "Pacman", 0)

        self.lives = 3
        self.tile_size = tile_size
        self.image_size = 30

        base_path = os.path.dirname(os.path.dirname(__file__))
        full_path = os.path.join(base_path, image_path)

        self.image = pygame.image.load(full_path)
        self.image = pygame.transform.scale(
            self.image,
            (self.image_size, self.image_size)
        )

    def draw(self, screen):
        screen.blit(
            self.image,
            (
                self.x_coordinate * self.tile_size + self.tile_size // 2 - self.image_size // 2,
                self.y_coordinate * self.tile_size + self.tile_size // 2 - self.image_size // 2
            )
        )

    def eat_cheese(self, cheese):
        if (self.x_coordinate, self.y_coordinate) in cheese.positions:
            cheese.positions.remove((self.x_coordinate, self.y_coordinate))
            self.add_score(10)
            print("Cheese eaten! Score: ", self.score)

    def eat_cherry(self, cherry):
        if cherry.consumed:
            return

        if self.x_coordinate == cherry.x_coordinate and self.y_coordinate == cherry.y_coordinate:
            cherry.consumed = True
            self.add_score(cherry.bonus_points)
            print("Cherry eaten! Score: ", self.score)


    def add_score(self, points):
        self.score += points

    def lose_life(self):
        self.lives -= 1