# scraping the mqtt sub client
# and saving to "C:\Dev\MQTT\data\pythonlog.json"
#
# 06.04.2020

import paho.mqtt.client as mqtt
import time
import clean_json

# TODO -- add clean data script to call and clean file

#create functions
def on_log(client, userdata, level, buf):
    print("log: " + buf)

# sends message when connected
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected")
    else:
        print("Bad connection, returned code =", + rc)

# sends message when disconnected
def on_disconnect(client, userdata, rc = 0, period = .5):
    print(" Disconnected result code: " + str(rc))
    client1.loop()
    time.sleep(period)

# waiting for flag 
def wait_for(client,msgType,period=0.25):
 if msgType == "SUBACK":
  if client.on_subscribe:
    while not client.suback_flag:
      print("waiting suback")
      client.loop()  #check for messages
      time.sleep(period)

# creating message
def on_message(client, userdata, message):
    payload_message = str(message.payload.decode("utf-8"))
    print("message recieved: {0}\nmessage topic: {1}\nmessage qos: {2}\nmessage retain flag: {3}"
    .format(payload_message, message.topic, message.qos, message.retain))
    f = open(r"C:\Dev\MQTT\data\pythonlog.txt", "a")
    f.write(payload_message + "\n")
    f.close()

# establish broker and port
broker = "192.168.99.127"
port = 1883

# creating a client instance (only client_id is necessary)
client1 = mqtt.Client("jake_client1")
client1.on_connect = on_connect
client1.on_disconnect = on_disconnect
client1.on_log = on_log
client1.on_message = on_message #attach function to callback
client1.connect(broker, port, 60)
client1.subscribe("/gw/ac233fc01142/status")
client1.loop_forever()
