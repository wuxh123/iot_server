#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import time
import signal
import threading

from common import gl
from cfg.Config import Cfg
from my_sql.mysqlHelper import MyDB
from mongo.mongo import MyMongoDB
from my_redis.CRedis import RedisHelper,CRedis
from my_mqtt.my_mqtt  import MqttClient
from my_epoll.my_epoll import my_epoll
from concurrent.futures import ThreadPoolExecutor
from bis.bis import parseDevData

filename=os.path.basename(os.path.realpath(__file__))

def init():
    pass

#启动mqtt接收服务
def start_mqtt():   
    gl.mqtt_client=MqttClient(gl.cfg.mqtt_ip, gl.cfg.mqtt_port,gl.cfg.mqtt_user,gl.cfg.mqtt_pass,gl.cfg.mqtt_timout)
    gl.mqtt_client.connect()
    task=gl.executor_main.submit(gl.mqtt_client._loop,(None))
    task.Daemon=True

#启动epoll接收服务
def start_epoll():
    gl.epoll=my_epoll(gl.cfg.sock_ip,gl.cfg.sock_port,gl.cfg.sock_timeout)
    task=gl.executor_main.submit(gl.epoll.run,(parseDevData))
    task.Daemon=True

if __name__ == "__main__":   
    gl.log.debug(filename+"-"*20)
    gl.log.debug(("pid={}".format(os.getpid())))
    gl.log.debug(filename+"-"*20) 
    init()
    start_epoll()
    start_mqtt()
 
    gl.log.debug("-------------run------------")
    '''while(True):
        print("start socket send..")
        #gl.epoll.send_event()
        time.sleep(20)
    sys.exit()'''
'''    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("11111")'''