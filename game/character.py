from game.gameobject import GameObject
class Character(GameObject):
    def __init__(self, name, score, x_coordinate, y_coordinate, image=None):
        super().__init__(x_coordinate, y_coordinate, image)
        self.name = name
        self.score = score
        self.image = image


    def move(self, direction, level_map):
        if direction == "LEFT":
            new_x = self.x_coordinate - 1
            new_y = self.y_coordinate

        elif direction == "RIGHT":
            new_x = self.x_coordinate + 1
            new_y = self.y_coordinate

        elif direction == "UP":
            new_x = self.x_coordinate
            new_y = self.y_coordinate - 1

        elif direction == "DOWN":
            new_x = self.x_coordinate
            new_y = self.y_coordinate + 1

        else:
            return

        if not level_map.is_wall(new_x, new_y):
            self.x_coordinate = new_x
            self.y_coordinate = new_y

    def add_score(self, points):
        if points < 0:
            raise ValueError("Score cannot be negative")

        self.score += points

