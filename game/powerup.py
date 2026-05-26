from game.item import Item


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