from game.character import Character


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
        self.start_position = start_position
        self.edible = False

    def make_edible(self, duration=None):
        self.edible = True
        self.duration = duration

    def make_normal(self):
        self.edible = False

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