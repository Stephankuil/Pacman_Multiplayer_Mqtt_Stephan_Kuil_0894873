import ssl
import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connectie gelukt")
    else:
        print("Connectie mislukt:", reason_code)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set("pacman", "Wachtwoord1@")
client.tls_set(cert_reqs=ssl.CERT_REQUIRED)

client.on_connect = on_connect

client.connect("82a5f8bf120849f2bdecab4ac8ee5426.s1.eu.hivemq.cloud", 8883)

client.loop_start()
time.sleep(3)
client.loop_stop()