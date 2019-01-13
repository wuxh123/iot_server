
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:wuxh
import redis
from cfg.Config import Cfg

class RedisHelper(object):
    def __init__(self,host,passowrd,port):
        self.__conn = redis.Redis(host=host,password=passowrd,port=6379)#连接Redis
        self.channel = 'monitor' #定义名称

    def publish(self,msg):#定义发布方法
        self.__conn.publish(self.channel,msg)
        return True

    def subscribe(self):#定义订阅方法
        pub = self.__conn.pubsub()
        pub.subscribe(self.channel)
        pub.parse_response()
        return pub

class CRedis():
    def __init__(self):
        pass

    def connect(self,_host,_password,_port):
        r = redis.Redis(host=_host,port=_port,password=_password,db=0)
        r.set('name', 'zhangsan')   #添加
        print (r.get('name'))   #获取
    
    def poll_connect(self,host,password,port):   
        pool = redis.ConnectionPool(host=host,password=password,port=port)
        r = redis.Redis(connection_pool=pool)
        r.set('name', 'zhangsan')   #添加
        print (r.get('name'))   #获取

    def pipeline(self,host,password,port):   
        pool = redis.ConnectionPool(host=host,password=password,port=port)
        r = redis.Redis(connection_pool=pool)
        pipe = r.pipeline(transaction=True)
        r.set('name', 'zhangsan')
        r.set('name', 'lisi')
        pipe.execute()
    
    def publish(self,):
        cfg=Cfg()
        obj = RedisHelper(cfg.redis_ip,cfg.redis_pass,cfg.redis_port)
        obj.publish('hello')#发布

    def subscribe(self,):
        cfg=Cfg()
        obj = RedisHelper(cfg.redis_ip,cfg.redis_pass,cfg.redis_port)
        redis_sub = obj.subscribe()#调用订阅方法

        while True:
            msg= redis_sub.parse_response()
            print (msg)

    #TODO 分布式锁的实现