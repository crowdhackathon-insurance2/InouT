import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import obd

    #OBD STARTS HERE
# connection = obd.OBD() # auto-connects to USB or RF port
#
# cmd = obd.commands.SPEED # select an OBD command (sensor)
#
# response = connection.query(cmd) # send the command, and parse the response
#
# print(response.value) # returns unit-bearing values thanks to Pint
# print(response.value.to("mph")) # user-friendly unit conversions

    #OBD ENDS HERE
#import RPi.GPIO as GPIO

Broker = "iot.eclipse.org"

#sub_topic = "sensor/instructions"    # receive messages on this topic

pub_topic = "crowdhackathon/inout"       # send messages to this topic


############### sensehat inputs ##################

# def read_temp():
#     t = sense.get_temperature()
#     t = round(t)
#     return t
#
# def read_humidity():
#     h = sense.get_humidity()
#     h = round(h)
#     return h
#
# def read_pressure():
#     p = sense.get_pressure()
#     p = round(p)
#     return p
#
# def display_sensehat(message):
#     sense.show_message(message)
#     time.sleep(10)

############### MQTT section ##################

# when connecting to mqtt do this;
# Needs to be BCM. GPIO.BOARD lets you address GPIO ports by periperal
# connector pin number, and the LED GPIO isn't on the connector
#GPIO.setmode(GPIO.BCM)



def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/crowdhackathon/inout")
    # set up GPIO output channel
    #GPIO.setup(16, GPIO.OUT)

# when receiving a mqtt message do this;

# def on_message(client, userdata, msg):
#     message = str(msg.payload)
#     print(msg.topic+" "+message)
#     display_sensehat(message)

def on_publish(client, userdata, msg):
    print("mid: " + str(msg))


client = mqtt.Client("rpi3")
client.on_connect = on_connect
#client.on_message = on_message
client.connect(Broker, 1883, 60)
for x in range(0,3):
    client.publish("/crowdhackathon/inout", "Car mph",2)
client.loop_forever()

# while True:
#     print("In loop")
#     #sensor_data = [read_temp(), read_humidity(), read_pressure()]
#     client.publish("/crowdhackathon/inout", "First message")
#     # time.sleep(1*60)
