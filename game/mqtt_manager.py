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

TOPIC = "pacman/inspiration"


class MQTTManager:
    def __init__(self, player_id, pacman, players, is_host):
        self.player_id = player_id
        self.pacman = pacman
        self.players = players
        self.is_host = is_host

        self.world_state = None
        self.item_eaten_message = None
        self.cheese_eaten_message = None

        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.username_pw_set(USERNAME, PASSWORD)
        self.client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
        self.client.on_message = self.on_message

    def connect(self):
        self.client.connect(BROKER, PORT)
        self.client.subscribe(TOPIC)
        self.client.loop_start()
        self.publish_join()

    def on_message(self, client, userdata, msg):
        data = json.loads(msg.payload.decode())

        message_type = data.get("type")

        if message_type == "world_state":
            self.world_state = data
            return

        if message_type == "cheese_eaten":
            self.cheese_eaten_message = data
            return

        if message_type == "item_eaten":
            self.item_eaten_message = data
            return

        if message_type not in ["join", "move"]:
            return

        pid = data["player_id"]

        if pid == self.player_id:
            return

        self.players[pid] = {
            "x": data["x"],
            "y": data["y"],
            "score": data.get("score", 0),
            "lives": data.get("lives", 3)
        }

        if message_type == "join":
            self.publish_move()

    def publish_join(self):
        self.client.publish(TOPIC, json.dumps({
            "type": "join",
            "player_id": self.player_id,
            "x": self.pacman.x_coordinate,
            "y": self.pacman.y_coordinate,
            "score": self.pacman.score,
            "lives": self.pacman.lives
        }))

    def publish_move(self):
        self.client.publish(TOPIC, json.dumps({
            "type": "move",
            "player_id": self.player_id,
            "x": self.pacman.x_coordinate,
            "y": self.pacman.y_coordinate,
            "score": self.pacman.score,
            "lives": self.pacman.lives
        }))

    def publish_cheese_eaten(self, x, y):
        self.client.publish(TOPIC, json.dumps({
            "type": "cheese_eaten",
            "player_id": self.player_id,
            "x": x,
            "y": y
        }))

    def publish_item_eaten(self, item_type, x, y):
        self.client.publish(TOPIC, json.dumps({
            "type": "item_eaten",
            "player_id": self.player_id,
            "item_type": item_type,
            "x": x,
            "y": y
        }))

    def publish_world_state(self, ghosts, items, cheese_list):
        self.client.publish(TOPIC, json.dumps({
            "type": "world_state",
            "ghosts": [
                {
                    "color": ghost.color,
                    "x": ghost.x_coordinate,
                    "y": ghost.y_coordinate,
                    "edible": ghost.edible
                }
                for ghost in ghosts
            ],
            "items": [
                {
                    "type": item.__class__.__name__,
                    "x": item.x_coordinate,
                    "y": item.y_coordinate,
                    "consumed": item.consumed
                }
                for item in items
            ],
            "cheese": [
                {
                    "x": cheese.x_coordinate,
                    "y": cheese.y_coordinate,
                    "consumed": cheese.consumed
                }
                for cheese in cheese_list
            ]
        }))

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()