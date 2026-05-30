from game.item import Item

import pygame

class PowerUp(Item):

    def __init__(self, x_coordinate, y_coordinate):

        super().__init__(
            name="PowerUp",
            points=50,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate
        )

        self.active = False
        self.amount = 0
        self.spawn_points = 0
        self.image = None

    def draw(self, screen):
        tile_size = 30

        pygame.draw.circle(
            screen,
            (255, 0, 255),
            (
                self.x_coordinate * tile_size + tile_size // 2,
                self.y_coordinate * tile_size + tile_size // 2
            ),
            10
        )
