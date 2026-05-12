

class GameObject:
    def __init__(self, x_coordinate, y_coordinate, image):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.image = image

    def draw(self, screen):
        if screen is None:
            return

        if self.image is None:
            return

        screen.blit(self.image, (self.x_coordinate, self.y_coordinate))
