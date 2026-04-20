import pygame
import sys

pygame.init()

width = 800
height = 800

circle_x_coordinate = 400
circle_y_coordinate = 400
circle_size = 50
screen = pygame.display.set_mode((width, height))

players = {}

if len(sys.argv) > 1:
    player_id = sys.argv[1]
else:
    player_id = "p1"  # default

players[player_id] = {"x": circle_x_coordinate, "y": circle_y_coordinate}


running = True

while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if keys[pygame.K_LEFT]:
        circle_x_coordinate -= 10
    if keys[pygame.K_RIGHT]:
        circle_x_coordinate += 10


    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (255,0,0), (circle_x_coordinate, circle_y_coordinate), circle_size)

    pygame.display.flip()