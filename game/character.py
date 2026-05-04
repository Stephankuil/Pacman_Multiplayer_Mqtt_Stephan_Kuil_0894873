from gameobject import GameObject
from levelmap import LevelMap

class Character(GameObject):   # 👈 inheritance
    def __init__(self, xcoordinate, ycoordinate, name, score):
        super().__init__(xcoordinate, ycoordinate)  # 👈 belangrijk
        self.name = name
        self.score = score
        self.just_teleported = False

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

    def teleport_if_needed(self, level_map):
        current_tile = level_map.get_tile(self.x_coordinate, self.y_coordinate)

        if current_tile == 'q' and not self.just_teleported:
            new_x, new_y = level_map.get_other_teleport(
                self.x_coordinate,
                self.y_coordinate
            )

            self.x_coordinate = new_x
            self.y_coordinate = new_y
            self.just_teleported = True

        elif current_tile != 'q':
            self.just_teleported = False