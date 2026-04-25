import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os
import time
load_dotenv()

BROKER = os.getenv("MQTT_BROKER")
PORT = int(os.getenv("MQTT_PORT"))
USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")
class MQTT_Connection_Check():
    def __init__(self):
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.username_pw_set(USERNAME, PASSWORD)
        self.client.tls_set()

    def on_connect(self, client, userdata, flags, reason_code, properties):
        if reason_code == 0:
            print(" CONNECTIE GELUKT")
        else:
            print(f" CONNECTIE MISLUKT: {reason_code}")


    def check_connection(self):
        self.client.on_connect = self.on_connect
        self.client.connect(BROKER, PORT)
        self.client.loop_start()
        time.sleep(3)
        self.client.loop_stop()
        self.client.disconnect()

if __name__ == "__main__":

    mqtt_checker = MQTT_Connection_Check()
    mqtt_checker.check_connection()

