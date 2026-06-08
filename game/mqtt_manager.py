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
        self.world_state = None
        self.item_eaten_message = None
        self.cheese_eaten_message = None
        self.is_host = is_host

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

        if data["type"] == "world_state":
            self.world_state = data
            return

        if data["type"] == "item_eaten":
            self.item_eaten_message = data
            return

        if data["type"] == "cheese_eaten":
            self.cheese_eaten_message = data
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

        if data.get("type") == "join":
            self.publish_move()

    def publish_join(self):
        message = {
            "type": "join",
            "player_id": self.player_id,
            "x": self.pacman.x_coordinate,
            "y": self.pacman.y_coordinate,
            "score": self.pacman.score,
            "lives": self.pacman.lives
        }

        self.client.publish(TOPIC, json.dumps(message))

    def publish_move(self):
        message = {
            "type": "move",
            "player_id": self.player_id,
            "x": self.pacman.x_coordinate,
            "y": self.pacman.y_coordinate,
            "score": self.pacman.score,
            "lives": self.pacman.lives
        }

        self.client.publish(TOPIC, json.dumps(message))

    def publish_world_state(self, ghosts, cherry, powerup, cheese):
        message = {
            "type": "world_state",
            "ghosts": [
                {
                    "x": ghost.x_coordinate,
                    "y": ghost.y_coordinate,
                    "edible": ghost.edible
                }
                for ghost in ghosts
            ],
            "cherry": {
                "x": cherry.x_coordinate,
                "y": cherry.y_coordinate,
                "consumed": cherry.consumed
            },
            "powerup": {
                "x": powerup.x_coordinate,
                "y": powerup.y_coordinate,
                "consumed": powerup.consumed
            },
            "cheese_positions": list(cheese.positions)
        }

        self.client.publish(TOPIC, json.dumps(message))

    def publish_item_eaten(self, item_type):
        message = {
            "type": "item_eaten",
            "player_id": self.player_id,
            "item_type": item_type
        }

        self.client.publish(TOPIC, json.dumps(message))

    def publish_cheese_eaten(self, x, y):
        message = {
            "type": "cheese_eaten",
            "player_id": self.player_id,
            "x": x,
            "y": y
        }

        self.client.publish(TOPIC, json.dumps(message))

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()