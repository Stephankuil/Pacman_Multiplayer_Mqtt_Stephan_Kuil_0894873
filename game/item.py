from game.gameobject import GameObject
import pygame

class Item(GameObject):

    def __init__(self, name, points=0, x_coordinate=0, y_coordinate=0, image=None):

        super().__init__(
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate,
            image=image
        )

        self.name = name
        self.points = points
        self.consumed = False

    def consume(self):
        self.consumed = True

    def draw(self, screen, color):
        tile_size = 30

        pygame.draw.circle(
            screen,
            color,
            (
                self.x_coordinate * tile_size + tile_size // 2,
                self.y_coordinate * tile_size + tile_size // 2
            ),
            4
        )