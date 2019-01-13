#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import configparser
from base.Singleton import Singleton

class Cfg(Singleton):
    print("Init config once")

    #获取文件的当前路径（绝对路径）
    cur_path=os.path.dirname(os.path.realpath(__file__))
     
     
    #获取config.ini的路径
    config_path=os.path.join(cur_path,'config.ini')
     
     
    cf=configparser.ConfigParser()
    cf.read(config_path)

    #db config
    db_host = cf.get("db", "host")    
    db_port = cf.getint("db", "port")
    db_user = cf.get("db", "username")
    db_pass = cf.get("db", "password")
    db_database = cf.get("db", "database")

    #epoll config
    sock_ip=cf.get("socket", "ip") 
    sock_port=cf.getint("socket","port")
    sock_timeout=cf.getint("socket","timeout")
    epoll_max_conn=cf.getint("socket","epoll_max_conn")
    rcv_data_len=cf.getint("socket","rcv_data_len")

    #mqtt config
    mqtt_ip=cf.get("mqtt","ip")
    mqtt_port=cf.getint("mqtt","port")
    mqtt_timout=cf.getint("mqtt","timeout")
    mqtt_user=cf.get("mqtt","user")
    mqtt_pass=cf.get("mqtt","password")
    mqtt_pub_prefix=cf.get("mqtt-publish","prefix")
    mqtt_subscrib_prefix=cf.get("mqtt-subscrib","prefix")

    #redis-cfg
    redis_ip=cf.get("redis","ip")
    redis_port=cf.getint("redis","port")
    redis_pass=cf.get("redis","password")

    #mongo-cfg
    mongo_ip = cf.get("mongo", "ip")    
    mongo_port = cf.getint("mongo", "port")
    mongo_db_name = cf.get("mongo", "db_name")
    mongo_set_name = cf.get("mongo", "set_name")

    def __init__(self):
        return
