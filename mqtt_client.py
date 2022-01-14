#Ethan Shirk
#14/01/2022

#Please note this is a work in progress :)

import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc): #callbacks
    print("Connected with result code", rc)
    
def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)

clientID = "" #Please put your MQTT Client ID here :)

client = mqtt.Client(client_id=clientID, clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp") #Setup TCP & protocol

client.on_connect = on_connect #define callbacks
client.on_message = on_message

mqtt_username = ""
mqtt_password = ""

client.username_pw_set(username=mqtt_username, password=mqtt_password) #set user and pass
print("Connecting...")

raptorIP = ""
client.connect(raptorIP, 1883, 10)

client.subscribe("/x/y") #this is how you subscribe!
#connect to Raptor locally hosted on Pi on port 1883

while True: 
    try:   
        client.loop(1) #note the argument blocks for x number of seconds
        client.publish("topic goes here","payload goes here") #this is how you publish!
           
    except Exception as e:
        print(e)
        time.sleep(0.5)

