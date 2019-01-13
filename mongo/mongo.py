#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient

class MyMongoDB(object):
    def __init__(self,ip,port,db_name,set_name):
        try:
            self.conn = MongoClient(ip, port)
        except Exception as e:
            print(e)
        self.db = self.conn[db_name]
        self.my_set = self.db[set_name]

    def insert(self,dic):
        print("inser...")
        self.my_set.insert(dic)

    def update(self,dic,newdic):
        print("update...")
        self.my_set.update(dic,newdic)

    def delete(self,dic):
        print("delete...")
        self.my_set.remove(dic)

    def dbfind(self,dic):
        print("find...")
        data = self.my_set.find(dic)
        for result in data:
            print(result["name"],result["age"])

