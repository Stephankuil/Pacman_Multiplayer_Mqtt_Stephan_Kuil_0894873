import pygame
import os
from character import Character


class Ghost(Character):
    def __init__(self, x, y, image_path, blue_image_path, tile_size, color=(255, 0, 0)):
        super().__init__(x, y, "Ghost", 0)

        self.image_path = image_path
        self.blue_image_path = blue_image_path
        self.tile_size = tile_size
        self.image_size = 30
        self.color = color
        self.starting_position = (x, y)
        self.edible = False

        base_path = os.path.dirname(os.path.dirname(__file__))

        full_path = os.path.join(base_path, image_path)
        blue_full_path = os.path.join(base_path, blue_image_path)

        self.image = pygame.image.load(full_path)
        self.image = pygame.transform.scale(
            self.image,
            (self.image_size, self.image_size)
        )

        self.blue_image = pygame.image.load(blue_full_path)
        self.blue_image = pygame.transform.scale(
            self.blue_image,
            (self.image_size, self.image_size)
        )

    def draw(self, screen):
        x_pixel = self.x_coordinate * self.tile_size + self.tile_size // 2 - self.image_size // 2
        y_pixel = self.y_coordinate * self.tile_size + self.tile_size // 2 - self.image_size // 2

        if self.edible:
            screen.blit(self.blue_image, (x_pixel, y_pixel))
        else:
            screen.blit(self.image, (x_pixel, y_pixel))
    def make_edible(self):
        self.edible = True

    def make_normal(self):
        self.edible = False

    def hit_pacman(self, pacman):
        if self.edible:
            return

        if self.x_coordinate == pacman.x_coordinate and self.y_coordinate == pacman.y_coordinate:
            pacman.lose_life()
            print("Pacman hit by ghost! Lives:", pacman.lives)

    def eaten_by_pacman(self, pacman):
        if not self.edible:
            return

        if self.x_coordinate == pacman.x_coordinate and self.y_coordinate == pacman.y_coordinate:
            pacman.add_score(200)

            self.x_coordinate = self.starting_position[0]
            self.y_coordinate = self.starting_position[1]

            self.make_normal()

            print("Ghost eaten! Score:", pacman.score)