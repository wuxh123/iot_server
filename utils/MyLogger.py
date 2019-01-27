#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import logging

class MyLogger(object):
    def __init__(self):
        handlers = {
            logging.NOTSET: "logs/notset.log",
            logging.DEBUG: "logs/debug.log",
            logging.INFO: "logs/info.log",
            logging.WARNING: "logs/warning.log",
            logging.ERROR: "logs/error.log",
            logging.CRITICAL: "logs/critical.log",
        }
        self.__loggers = {}
        logLevels = handlers.keys()
        fmt = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
        for level in logLevels:
            #创建logger
            logger = logging.getLogger(str(level))
            logger.setLevel(level)
            #创建hander用于写日日志文件
            log_path = os.path.abspath(handlers[level])
            fh = logging.FileHandler(log_path)
            #定义日志的输出格式
            fh.setFormatter(fmt)
            fh.setLevel(level)
            #再创建一个handler，用于输出到控制台
            ch=logging.StreamHandler()
            ch.setLevel(level)
            ch.setFormatter(fmt)

            #给logger添加hander
            logger.addHandler(fh)
            logger.addHandler(ch)
            self.__loggers.update({level: logger})
    def info(self, message):
        self.__loggers[logging.INFO].info(message)

    def error(self, message):
        self.__loggers[logging.ERROR].error(message)

    def warning(self, message):
        self.__loggers[logging.WARNING].warning(message)

    def debug(self, message):
        self.__loggers[logging.DEBUG].debug(message)

    def critical(self, message):
        self.__loggers[logging.CRITICAL].critical(message)

if __name__ == "__main__":
    logger = MyLogger()
    logger.debug("thisisdebug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
