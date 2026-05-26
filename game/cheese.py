from game.item import Item

class Cheese(Item):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        image = None
        rgb_color = (255, 255, 0)

        cheese_list = []

    def how_many_left(self, cheese_list):
        amount_left = 0

        for cheese in cheese_list:
            if not cheese.consumed:
                amount_left += 1

        return amount_left



