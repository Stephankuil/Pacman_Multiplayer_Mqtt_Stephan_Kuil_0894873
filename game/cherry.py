import pygame
import os
import random

from item import Item


class Cherry(Item):
    def __init__(self, image_path, tile_size, bonus_points=100):
        super().__init__(0, 0, bonus_points)

        self.image_path = image_path
        self.tile_size = tile_size
        self.image_size = 25
        self.bonus_points = bonus_points
        self.consumed = True
        self.image = None

    def load_image(self):
        base_path = os.path.dirname(os.path.dirname(__file__))
        full_path = os.path.join(base_path, self.image_path)

        self.image = pygame.image.load(full_path).convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (self.image_size, self.image_size)
        )

    def respawn(self, level_map):
        free_positions = []

        for y, row in enumerate(level_map.map):
            for x, tile in enumerate(row):
                if tile == ' ':
                    free_positions.append((x, y))

        if free_positions:
            self.x_coordinate, self.y_coordinate = random.choice(free_positions)
            self.consumed = False
            print(f"Cherry spawned at ({self.x_coordinate}, {self.y_coordinate})")
        else:
            print("Geen vrije plekken voor cherry!")

    def draw(self, screen):
        if self.consumed or self.image is None:
            return

        screen.blit(
            self.image,
            (
                self.x_coordinate * self.tile_size + self.tile_size // 2 - self.image_size // 2,
                self.y_coordinate * self.tile_size + self.tile_size // 2 - self.image_size // 2
            )
        )