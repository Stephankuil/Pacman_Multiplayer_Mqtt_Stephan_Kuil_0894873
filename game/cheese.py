import pygame
import os


class Cheese:
    def __init__(self, image_path, positions, tile_size):
        base_path = os.path.dirname(os.path.dirname(__file__))
        full_path = os.path.join(base_path, image_path)

        self.image_size = 10
        self.image = pygame.image.load(full_path)
        self.image = pygame.transform.scale(
            self.image,
            (self.image_size, self.image_size)
        )

        self.positions = positions
        self.tile_size = tile_size

    def draw(self, screen):
        for (x, y) in self.positions:
            screen.blit(
                self.image,
                (
                    x * self.tile_size + self.tile_size // 2 - self.image_size // 2,
                    y * self.tile_size + self.tile_size // 2 - self.image_size // 2
                )
            )

    def how_many_left(self):
        return len(self.positions)