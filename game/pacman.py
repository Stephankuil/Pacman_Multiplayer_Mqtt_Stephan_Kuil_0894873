from game.character import Character
from game.cheese import Cheese
from game.cherry import Cherry
from game.powerup import PowerUp
from game.ghosts import Ghost
import pygame
class Pacman(Character):
    def __init__(self, x_coordinate=0, y_coordinate=0):
        super().__init__(
            name="Pacman",
            score=0,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate,
            image=None
        )

        self.lives = 3

    def eat_cheese(self, cheese):
        if self.x_coordinate == cheese.x_coordinate and self.y_coordinate == cheese.y_coordinate:
            if not cheese.consumed:
                cheese.consumed = True
                self.add_score(10)
            return True
        return False

    def eat_cherry(self, cherry):
        if self.x_coordinate == cherry.x_coordinate and self.y_coordinate == cherry.y_coordinate:
            if not cherry.consumed:
                cherry.consumed = True
                self.add_score(cherry.points)
            return True
        return False

    def eat_ghost(self, ghost):
        if ghost.edible and self.x_coordinate == ghost.x_coordinate and self.y_coordinate == ghost.y_coordinate:
            self.add_score(200)
            return True
        return False

    def eat_powerup(self, powerup):
        if self.x_coordinate == powerup.x_coordinate and self.y_coordinate == powerup.y_coordinate:
            if not powerup.consumed:
                powerup.consumed = True
                self.add_score(50)
            return True
        return False

    def lose_life(self):
        self.lives -= 1

        # Pacman terug naar startpositie
        self.x_coordinate = 10
        self.y_coordinate = 15

        if self.lives < 0:
            raise ValueError("Lives cannot be negative")

    def hit_by_ghost(self, ghost):
        if ghost.edible:
            return

        if self.x_coordinate == ghost.x_coordinate and self.y_coordinate == ghost.y_coordinate:
            self.lose_life()

    def draw(self, screen):
        tile_size = 30

        pygame.draw.circle(
            screen,
            (255, 255, 0),
            (
                self.x_coordinate * tile_size + tile_size // 2,
                self.y_coordinate * tile_size + tile_size // 2
            ),
            12
        )