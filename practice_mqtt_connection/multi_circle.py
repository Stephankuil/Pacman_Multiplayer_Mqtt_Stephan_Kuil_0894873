import pygame
import sys
import ssl
import json
import os
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import random

load_dotenv()

BROKER = os.getenv("MQTT_BROKER")
PORT = int(os.getenv("MQTT_PORT"))
USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")

TOPIC = "game/circles"

PLAYER_COLORS = [
    (255, 0, 0),      # rood
    (0, 0, 255),      # blauw
    (0, 255, 0),      # groen
    (255, 255, 0),    # geel
    (255, 165, 0),    # oranje
    (128, 0, 128),    # paars
    (0, 255, 255),    # lichtblauw
    (255, 192, 203),  # roze
    (165, 42, 42),    # bruin
    (0, 0, 0)         # zwart
]

def get_player_color(player_id):
    totaal = 0

    for letter in player_id:
        totaal += ord(letter)

    kleur_index = totaal % len(PLAYER_COLORS)
    return PLAYER_COLORS[kleur_index]


def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    pid = data["player_id"]
    x = data["x"]
    y = data["y"]
    message_type = data.get("type", "move")

    if pid not in players:
        players[pid] = {
            "x": x,
            "y": y,
            "color": get_player_color(pid)
        }
    else:
        players[pid]["x"] = x
        players[pid]["y"] = y

    if message_type == "join" and pid != player_id:
        client.publish(TOPIC, json.dumps({
            "type": "move",
            "player_id": player_id,
            "x": players[player_id]["x"],
            "y": players[player_id]["y"]
        }))



pygame.init()

width = 800
height = 800
circle_size = 20

font = pygame.font.SysFont(None, 30)

pacman_img = pygame.image.load("../images/pacman2.png")
pacman_img = pygame.transform.scale(pacman_img, (circle_size*2, circle_size*2))

circle_x_coordinate = random.randint(circle_size, width - circle_size)
circle_y_coordinate = random.randint(circle_size, height - circle_size)

screen = pygame.display.set_mode((width, height))

players = {}

player_id = sys.argv[1] if len(sys.argv) > 1 else "p1"
players[player_id] = {
    "x": circle_x_coordinate,
    "y": circle_y_coordinate,
    "color": get_player_color(player_id)
}

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe(TOPIC)
client.loop_start()

join_message = {
    "type": "join",
    "player_id": player_id,
    "x": players[player_id]["x"],
    "y": players[player_id]["y"]
}
client.publish(TOPIC, json.dumps(join_message))


running = True

while running:
    moved = False
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keys[pygame.K_LEFT]:
        players[player_id]["x"] -= 5
        moved = True
    if keys[pygame.K_RIGHT]:
        players[player_id]["x"] += 5
        moved = True
    if keys[pygame.K_UP]:
        players[player_id]["y"] -= 5
        moved = True
    if keys[pygame.K_DOWN]:
        players[player_id]["y"] += 5
        moved = True

    if moved:
        message = {
            "type": "move",
            "player_id": player_id,
            "x": players[player_id]["x"],
            "y": players[player_id]["y"]
        }
        print(message)
        client.publish(TOPIC, json.dumps(message))

    screen.fill((255, 255, 255))

    for play_id, pos in players.items():
        screen.blit(pacman_img, (pos["x"] - circle_size, pos["y"] - circle_size))

        color = pos["color"]
        name_text = font.render(play_id, True, color)
        screen.blit(name_text, (pos["x"] - 20, pos["y"] - 40))

    pygame.display.flip()

client.loop_stop()
client.disconnect()
pygame.quit()

