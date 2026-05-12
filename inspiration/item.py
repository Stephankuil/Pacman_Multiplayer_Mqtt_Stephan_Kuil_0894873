from gameobject import GameObject


class Item(GameObject):
    def __init__(self, xcoordinate, ycoordinate, points):
        super().__init__(xcoordinate, ycoordinate)
        self.points = points
        self.consumed = False