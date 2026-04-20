import pygame
import sys
import ssl
import json
import os
import paho.mqtt.client as mqtt
from dotenv import load_dotenv

load_dotenv()

BROKER = os.getenv("MQTT_BROKER")
PORT = int(os.getenv("MQTT_PORT"))
USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")

TOPIC = "game/circles"

def on_message(client, userdata, msg):
    pass

pygame.init()

width = 800
height = 800

circle_x_coordinate = 400
circle_y_coordinate = 400
circle_size = 50
screen = pygame.display.set_mode((width, height))

players = {}

player_id = sys.argv[1] if len(sys.argv) > 1 else "p1"
players[player_id] = {"x": circle_x_coordinate, "y": circle_y_coordinate}

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe(TOPIC)
client.loop_start()

running = True

while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keys[pygame.K_LEFT]:
        players[player_id]["x"] -= 10
    if keys[pygame.K_RIGHT]:
        players[player_id]["x"] += 10
    if keys[pygame.K_UP]:
        players[player_id]["y"] -= 10
    if keys[pygame.K_DOWN]:
        players[player_id]["y"] += 10

    screen.fill((255, 255, 255))

    for play_id, pos in players.items():
        pygame.draw.circle(screen, (255, 0, 0), (pos["x"], pos["y"]), circle_size)

    pygame.display.flip()

client.loop_stop()
client.disconnect()
pygame.quit()