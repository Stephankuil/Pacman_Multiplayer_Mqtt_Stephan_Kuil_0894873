from game.cheese import Cheese
from game.pacman import Pacman
import pygame

class Engine():
    def __init__(self):
        self.level = 1
        self.game_over = False
        self.running = False
        self.paused = False
        self.number_of_players = 1


        self.pacman = Pacman()


    def if_win(self):

        for cheese in self.cheese_list:

            if not cheese.consumed:
                return False

        self.level += 1
        return True

    def if_game_over(self):
        if self.pacman.lives <= 0:
            self.game_over = True
            return True

        self.game_over = False
        return False

    def game_status(self):
        if self.game_over:
            return "Game Over"
        elif self.running:
            return "Running"
        elif self.paused:
            return "Paused"
        else:
            return "Not started"

    def resume(self):

        if self.paused and not self.game_over:
            self.running = True
            self.paused = False


    def pauze(self):
        if self.running:
            self.running = False
            self.paused = True

    def restart(self):

        self.running = True
        self.paused = False
        self.game_over = False

        self.level = 1

        self.pacman.lives = 3
        self.pacman.score = 0

    def stop(self):
        self.running = False
        self.paused = False

    import pygame

    def draw(self, screen):
        tile_size = 30

        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):

                if tile == '1':
                    pygame.draw.rect(
                        screen,
                        (0, 0, 255),
                        (x * tile_size,
                         y * tile_size,
                         tile_size,
                         tile_size)
                    )
