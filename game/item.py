from game.gameobject import GameObject


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