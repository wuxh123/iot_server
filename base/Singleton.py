#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:wuxh

import threading
r=threading.Lock()

#如果是单例可以直接使用modle定义，modle是单例并且线程安全。
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_the_instance'):
            r.acquire()
            print("not hasattr")
            cls._the_instance=object.__new__(cls,*args, **kwargs)
            r.release()
        return cls._the_instance