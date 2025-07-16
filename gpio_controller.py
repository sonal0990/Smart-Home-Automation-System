import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    client.subscribe("home/device/LED")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    GPIO.output(17, GPIO.HIGH if payload == "ON" else GPIO.LOW)
    print(f"LED turned {payload}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
