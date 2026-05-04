from gameobject import GameObject
from levelmap import LevelMap

class Character(GameObject):   # 👈 inheritance
    def __init__(self, xcoordinate, ycoordinate, name, score):
        super().__init__(xcoordinate, ycoordinate)  # 👈 belangrijk
        self.name = name
        self.score = score

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