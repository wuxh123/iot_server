#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
from cfg.Config import Cfg
from concurrent.futures import ThreadPoolExecutor
sys.path.append("..") 
from my_mqtt.my_mqtt  import MqttClient
from my_epoll.my_epoll import my_epoll
from utils.MyLogger import MyLogger

#mqtt 主题
#如果单独发送给某一台设备，则加上"/deviceid"
mqtt_up='up/device'
mqtt_down='down/device/#'

#config
cfg = Cfg()

#mqtt client
mqtt_client=None #MqttClient(cfg.mqtt_ip, cfg.mqtt_port,cfg.mqtt_user,cfg.mqtt_pass,cfg.mqtt_timout)

#线程池
executor_main=ThreadPoolExecutor(max_workers=cfg.thread_pool_cnt_main)
#epoll 线程池
executor_e=ThreadPoolExecutor(max_workers=cfg.thread_pool_cnt_epoll)
#mqtt 线程池
executor_mqtt=ThreadPoolExecutor(max_workers=cfg.thread_pool_cnt_mqtt)

#fd <-> socket 字典
fd_to_socket={}

#devid <-> fd  字典
dev_to_fd={}

#epoll 连接
epoll=None #my_epoll(cfg.sock_ip,cfg.sock_port,cfg.sock_timeout)

#log
log=MyLogger()

#厂商列表
cs=["3G",]
print("gl init complete.......")