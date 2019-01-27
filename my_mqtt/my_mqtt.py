#!/usr/bin/python
# coding=utf-8
import threading
import paho.mqtt.client as mqtt
import time
import sys
sys.path.append("..") 
from common import gl
from bis.bis import parseMqttData

class MqttClient:
    client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    client = mqtt.Client(client_id)

    def __init__(self, host, port,user,password,timeout):
        self._host = host
        self._port = port
        self._user=user
        self._password=password
        self._timeout=timeout
        self.client.on_connect = self._on_connect  # 设置连接上服务器回调函数
        self.client.on_message = self._on_message  # 设置接收到服务器消息回调函数
        self.client.on_publish = self._on_publish  # publish之后的回调
        self.client.on_disconnect = self._on_disconnect  # 断线时回调

    def connect(self,):
        self.client.username_pw_set(self._user, self._password)  # 必须设置，否则会返回「Connected with result code 4」
        while True:
            try:
                self.client.connect(self._host, self._port, self._timeout)
                break
            except:
                gl.log.error("MQTT connect error,waitting for reconnect")
                time.sleep(3)
                continue
        

    def publish(self, topic, data):
        print("publish:"+topic)
        #todo 将所有的id从数据库中取出，到mqtt上定于该id的主题
        self.client.publish(topic, data)

    def loop(self, timeout=None):
        thread = threading.Thread(target=self._loop, args=(timeout,))
        thread.setDaemon(True)
        thread.start()
        thread.join()

    def _loop(self, timeout=None):
        if not timeout:
            self.client.loop_forever()
        else:
            self.client.loop(timeout)

    def _on_connect(self, client, userdata, flags, rc):
        print("\nConnected with result code " + str(rc))
        self.client.subscribe(gl.mqtt_down)

    def _on_message(self, client, userdata, msg):  # 从服务器接受到消息后回调此函数
        print(msg.topic+" "+msg.payload.decode("gbk"))
        gl.executor_mqtt.submit(parseMqttData,({'topic':msg.topic,'data':msg.payload}))

    def _on_publish(self,client, userdata, mid):
        print("data sended.")

    def _on_disconnect(self,client, userdata, rc):
        print("connect disconnected")

'''    def run(self):
        client = MqttClient("172.29.140.58", 63613,"test","test",60)
        client.connect()'''


'''client1 = MqttClient("172.29.140.58", 63613,"test","test",60)
client1.connect()
client1.publish('mqtt/test/test', '1234567890!')
client1.loop()
while (True):
    if (len( common.mqtt_send)>0):
            print("pop")
            val= common.mqtt_send.pop(0)
            client1.publish(val.topic, val.val)
            print(val)
            time.sleep(1)'''
        
