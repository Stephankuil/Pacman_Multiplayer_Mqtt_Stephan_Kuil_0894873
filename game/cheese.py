from game.item import Item


class Cheese(Item):

    def __init__(self, x_coordinate=0, y_coordinate=0, rgb_color=(255, 255, 0)):
        super().__init__(name='Cheese', points=10, x_coordinate=x_coordinate, y_coordinate=y_coordinate)

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        self.image = None
        self.rgb_color = rgb_color

        cheese_list = []

    def how_many_left(self, cheese_list):

        amount_left = 0

        for cheese in cheese_list:

            if not cheese.consumed:
                amount_left += 1

        if amount_left <= 0:
            raise ValueError("No cheese left")

        return amount_left