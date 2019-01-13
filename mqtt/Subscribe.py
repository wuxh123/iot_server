import time, signal
import paho.mqtt.client as mqtt
import binascii

client = None
mqtt_looping = False

class Mqtt_client():

    def __init__(self,host,usr,passowrd,port):
        self.host=host
        self.usr=usr
        self.password=passowrd
        self.port=port
    
    def GetSubscribeData(self,data):
        print(data)
        return data 

    def on_connect(self,mq, userdata, rc, _):   
        print("connected")     
        # subscribe when connected.
        mq.subscribe("mqtt/test/#")
    
    def on_message(self,mq, userdata, msg):
       # print ("topic: %s" % msg.topic)
       # print ("payload: %s" % msg.payload.decode('utf8'))
       data = msg.payload.decode('ascii')
       #data= str(binascii.b2a_hex(msg.payload)) #十六进制显示方法2
       #print(data)
       data1=binascii.b2a_hex(data.encode('ascii'))

       self.GetSubscribeData(data1)        
       #print( "qos: %d" % msg.qos)
    
    def mqtt_client_thread(self,):
        global client, mqtt_looping
        client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        client = mqtt.Client(client_id=client_id)
    
        # If broker asks user/password.
        user = "admin"
        password = "123456aa??"
        client.username_pw_set(user, password)
    
        client.on_connect = self.on_connect
        client.on_message = self.on_message
    
        try:
            client.connect(host,61613,600)
        except:
            print( "MQTT Broker is not online. Connect later.")
    
        mqtt_looping = True
        print ("Looping...")
    
        #mqtt_loop.loop_forever()
        cnt = 0
        while mqtt_looping:
            client.loop_forever()    
            cnt += 1
            if cnt > 20:
                try:
                    client.reconnect() # to avoid 'Broken pipe' error.
                except:
                    time.sleep(1)
                cnt = 0
    
        print ("quit mqtt thread")
        client.disconnect()
    
    def stop_all(self,*args):
        global mqtt_looping
        mqtt_looping = False

if __name__ == '__main__':
    mqttfunc = Mqtt_client()
    mqttfunc.mqtt_client_thread()

    print ("exit program")
    