import pygame
import json
import ssl
import os
import paho.mqtt.client as mqtt
from dotenv import load_dotenv


class Scoreboard:
    def __init__(self):
        self.players = {}
        self.messages = []

    def draw(self, screen):
        font = pygame.font.SysFont(None, 28)

        x = 20
        y = 20

        title = font.render("SCOREBOARD", True, (255, 255, 255))
        screen.blit(title, (x, y))

        y += 40

        for player_id, data in self.players.items():
            text = f"{data['name']}: {data['score']}"
            rendered = font.render(text, True, (255, 255, 0))
            screen.blit(rendered, (x, y))
            y += 30

        y += 20

        for message in self.messages[-8:]:
            rendered = font.render(message, True, (0, 255, 255))
            screen.blit(rendered, (x, y))
            y += 26

    def add_player(self, player_id, name):
        if player_id not in self.players:
            self.players[player_id] = {
                "name": name,
                "score": 0
            }

    def add_score(self, player_id, points, reason):
        self.add_player(player_id, player_id)
        self.players[player_id]["score"] += points
        self.add_message(f"{player_id} kreeg {points} punten voor {reason}")

    def add_message(self, message):
        self.messages.append(message)
        self.messages = self.messages[-8:]

    def to_dict(self):
        return {
            "players": self.players,
            "messages": self.messages
        }

    def from_dict(self, data):
        self.players = data["players"]
        self.messages = data["messages"]


if __name__ == "__main__":
    load_dotenv()

    BROKER = os.getenv("MQTT_BROKER")
    PORT = int(os.getenv("MQTT_PORT"))
    USERNAME = os.getenv("MQTT_USERNAME")
    PASSWORD = os.getenv("MQTT_PASSWORD")

    TOPIC = "pacman/inspiration"

    pygame.init()
    screen = pygame.display.set_mode((400, 600))
    pygame.display.set_caption("Scoreboard")

    scoreboard = Scoreboard()

    def on_message(client, userdata, msg):
        data = json.loads(msg.payload.decode())

        if data["type"] == "scoreboard_update":
            scoreboard.from_dict(data["scoreboard"])

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(USERNAME, PASSWORD)
    client.tls_set(cert_reqs=ssl.CERT_REQUIRED)

    client.on_message = on_message
    client.connect(BROKER, PORT)
    client.subscribe(TOPIC)
    client.loop_start()

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((20, 20, 20))
        scoreboard.draw(screen)
        pygame.display.flip()

        clock.tick(30)

    client.loop_stop()
    client.disconnect()
    pygame.quit()