import pygame


class Engine:
    def __init__(self, running, level, game_status, number_of_players):
        self.running = running
        self.level = level
        self.game_status = game_status
        self.number_of_players = number_of_players

        self.screen_width = 760
        self.screen_height = 840
        self.tile_size = 40

        self.screen = None
        self.clock = None

    def start_game(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height)
        )

        pygame.display.set_caption("Pacman Game")

        self.clock = pygame.time.Clock()
        self.running = True

    def draw_map(self, map_obj):
        for y, row in enumerate(map_obj.map):
            for x, tile in enumerate(row):
                rect = pygame.Rect(
                    x * self.tile_size,
                    y * self.tile_size,
                    self.tile_size,
                    self.tile_size
                )

                if tile == '1':
                    pygame.draw.rect(self.screen, (0, 0, 255), rect)
                else:
                    pygame.draw.rect(self.screen, (0, 0, 0), rect)

    def game_stop(self):
        self.running = False
    def if_win(self):
        pass

    def game_over(self):
        pass

    def resume(self):
        pass

    def game_stop(self):
        self.running = False