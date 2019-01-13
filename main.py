#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
from cfg.Config import Cfg
from my_sql.mysqlHelper import MyDB
from mongo.mongo import MyMongoDB
from my_redis.CRedis import RedisHelper,CRedis
import mqtt

def _log(fn):
    def logme(*args):
        print("_"*20)
        fn(*args)
    
    return logme 

@_log
def test_single_cfg():
    cfg=Cfg()
    cfg=Cfg()
    print(cfg.db_host,cfg.db_user,cfg.db_pass,cfg.db_port,cfg.db_database)
    #print others

@_log
def test_mysql():
    print("test mysql")
    cfg=Cfg()
    mydb = MyDB(cfg.db_host,cfg.db_user,cfg.db_pass,cfg.db_port,cfg.db_database)
    #创建表
    #mydb.create_table('create table user (id varchar(20) primary key, name varchar(20))')
    #插入数据
    id=mydb.execute_update_insert("insert into user (name) values  ('Michael')")
    print("lastid="+str(id))
    # 查询数据表
    results = mydb.query("SELECT * FROM user")
    print(results)
    for row in results:
        id = row[0]
        name = row[1]
        print("id=%s,name=%s" % \
               (id, name))
    list = mydb.query_formatrs("SELECT * FROM user")
    for i in list:
        print ("记录号：%s   值：%s" % (list.index(i) + 1, i))
    #关闭数据库
    mydb.close()

@_log
def test_mongo():
    cfg=Cfg()
    dic={"name":"zhangsan","age":18}
    mongo = MyMongoDB(cfg.mongo_ip,cfg.mongo_port,cfg.mongo_db_name,cfg.mongo_set_name)
    mongo.insert(dic)
    print("insert complete")
    
    mongo.dbfind({"name":"zhangsan"})

    mongo.update({"name":"zhangsan"},{"$set":{"age":"25"}})
    mongo.dbfind({"name":"zhangsan"})

    mongo.delete({"name":"zhangsan"})
    mongo.dbfind({"name":"zhangsan"})

@_log
def test_redis():
    cfg=Cfg()
    _redis = CRedis()
    _redis.connect(cfg.redis_ip,cfg.redis_pass,cfg.redis_port)    

@_log
def test_mqtt():
    publish=mqtt.Publish.Mqtt_publish()

if __name__ == "__main__":
    test_single_cfg()
    test_mysql()
    test_mongo()
    test_redis()


