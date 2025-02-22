import random

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic = "bci/game/training"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'emqx'
password = 'public'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.subscribe("bci/game/training/start/Up")
    client.subscribe("bci/game/training/stop/Up")
    client.subscribe("bci/game/training/start/Down")
    client.subscribe("bci/game/training/stop/Down")
    client.subscribe("bci/game/training/start/Left")
    client.subscribe("bci/game/training/stop/Left")
    client.subscribe("bci/game/training/start/Right")
    client.subscribe("bci/game/training/stop/Right")
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()