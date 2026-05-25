from gameobject import GameObject
class Items(GameObject):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.points = 0
        self.consumed = False