from game.character import Character
from game.cheese import Cheese
from game.cherry import Cherry
from game.powerup import PowerUp
class Pacman(Character):
    def __init__(self):
        super().__init__(
            name="Pacman",
            score=0,
            x_coordinate=0,
            y_coordinate=0,
            image=None
        )

        self.lives = 3


    def eat_cheese(self, cheese):
        if self.x_coordinate == cheese.x_coordinate and self.y_coordinate == cheese.y_coordinate:
            self.add_score(10)
            return True
        return False

    def eat_cherry(self, cherry):
        if self.x_coordinate == cherry.x_coordinate and self.y_coordinate == cherry.y_coordinate:
            self.add_score(50)
            return True
        return False

    def eat_ghost(self, ghost):
        if ghost.edible and self.x_coordinate == ghost.x_coordinate and self.y_coordinate == ghost.y_coordinate:
            self.add_score(200)
            return True
        return False

    def eat_powerup(self, powerup):
        if self.x_coordinate == powerup.x_coordinate and self.y_coordinate == powerup.y_coordinate:
            self.add_score(50)

    def lose_life(self):
        self.lives -= 1
        if self.lives < 0:
            raise ValueError("Lives cannot be negative")
