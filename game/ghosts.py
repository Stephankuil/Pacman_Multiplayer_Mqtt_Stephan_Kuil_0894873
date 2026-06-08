from game.character import Character
from inspiration.levelmap import LevelMap
import random
import pygame
class Ghost(Character):

    def __init__(self, color, x_coordinate, y_coordinate, image=None):
        super().__init__(
            name="Ghost",
            score=0,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate,
            image=image
        )

        self.color = color
        self.edible = False
        self.edible_timer = 0

    def make_edible(self, duration=None):
        self.edible = True
        self.edible_timer = duration

    def update_edible_timer(self, time_passed):
        if self.edible and self.edible_timer is not None:

            self.edible_timer -= time_passed

            # Timer afgelopen
            if self.edible_timer <= 0:
                self.make_normal()

    def make_normal(self):
        self.edible = False
        self.edible_timer = 0

    def hit_pacman(self, pacman):
        if self.edible:
            return

        if self.x_coordinate == pacman.x_coordinate and self.y_coordinate == pacman.y_coordinate:
            pacman.lose_life()

    def turn_blue(self):
        if self.edible:
            self.color = "blue"

    def eaten_by_pacman(self, pacman):
        same_position = (
            self.x_coordinate == pacman.x_coordinate
            and self.y_coordinate == pacman.y_coordinate
        )

        if self.edible and same_position:
            pacman.add_score(200)
            self.x_coordinate, self.y_coordinate = self.start_position
            self.make_normal()

    def wall_check(self, new_position, level_map):
        x, y = new_position

        # Buiten map links/boven
        if x < 0 or y < 0:
            return False

        # Buiten map rechts/onder
        if x >= level_map.width or y >= level_map.height:
            return False

        # Muur geraakt
        if level_map.is_wall(x, y):
            return False

        return True

    def draw(self, screen):
        tile_size = 30

        pygame.draw.circle(
            screen,
            self.color,
            (
                self.x_coordinate * tile_size + tile_size // 2,
                self.y_coordinate * tile_size + tile_size // 2
            ),
            12
        )

    def move_random(self, level_map):
        directions = ["LEFT", "RIGHT", "UP", "DOWN"]
        random.shuffle(directions)

        for direction in directions:
            old_x = self.x_coordinate
            old_y = self.y_coordinate

            self.move(direction, level_map)

            if self.x_coordinate != old_x or self.y_coordinate != old_y:
                break