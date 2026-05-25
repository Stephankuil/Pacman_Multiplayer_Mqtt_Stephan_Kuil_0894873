from game.item import Item


class Cherry(Item):

    def __init__(
            self,
            x_coordinate=0,
            y_coordinate=0,
            respawn_time=30
    ):

        super().__init__(
            name='Cherry',
            points=50,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate
        )

        if respawn_time < 0:
            raise ValueError("Respawn time cannot be negative")

        self.symbol = 'C'
        self.bonus_points = 50
        self.respawn_time = respawn_time

    def respawn(self, new_x_coordinate=0, new_y_coordinate=0):

        if new_x_coordinate < 0 or new_y_coordinate < 0:
            raise ValueError("Coordinates cannot be negative")

        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

        self.consumed = False


