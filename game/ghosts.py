from game.character import Character
from inspiration.levelmap import LevelMap

class Ghost(Character):

    def __init__(self, color, x_coordinate, y_coordinate, start_position, image=None):
        super().__init__(
            name="Ghost",
            score=0,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate,
            image=image
        )

        self.color = color
        self.start_position = (x_coordinate, y_coordinate)
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