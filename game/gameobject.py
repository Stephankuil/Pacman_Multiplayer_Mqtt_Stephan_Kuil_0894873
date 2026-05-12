

class GameObject:
    def __init__(self, xcoordinate, ycoordinate, image):
        self.x_coordinate = xcoordinate
        self.y_coordinate = ycoordinate
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
