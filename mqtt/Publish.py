import paho.mqtt.client as mqtt
import time 
import sys
import random

class Mqtt_publish():
    def __init__(self,host,usr,passowrd,port):
        self.host=host
        self.usr=usr
        self.password=passowrd
        self.port=port

    # The function after connected with Broker
    def on_Connect(self,client, userdata, flags, rc):
        print ("Connected with result code " + str(rc))

    # The function while publishing MQTT message
    def on_Publish(self,client, userdata, mid):
        print("Publish OK")  

    def run(self):
        client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        client = mqtt.Client(client_id=client_id)
        # Set up call back functions
        #client = mqtt.Client()       
        # If broker asks user/password.
        client.username_pw_set(self.usr, self.password)

        client.on_connect = self.on_Connect
        client.on_publish = self.on_Publish

        # Connect with Broker
        client.connect(self.host,61613,60)

        while True:
            try:
                print("start")
                # Publish MQTT message
                client.publish("OnOffLineTopic", '\x51\x52\x53\x54\x55')
                #print("start.2");
                time.sleep(2)
            except:
                print("EXIT")
                sys.exit(0)