from game.character import Character

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

    def lose_life(self):
        self.lives -= 1
