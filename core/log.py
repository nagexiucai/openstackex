#!/usr/bin/env python
#coding=utf-8

from core.base import Base
import traceback
from pprint import pprint

class Log(Base):
    LEVEL = 9527 #below this level will be printed
    FATAL = 0
    SERIOUS = 1
    ORDINARY = 2
    VORBOSE = 3
    @staticmethod
    def _(msg, level):
        if level <= Log.LEVEL:
            print msg
    @staticmethod
    def exception():
        traceback.print_exc()
    @staticmethod
    def beauty(data):
        print '!!! by pprint !!!'
        pprint(data)
    @classmethod
    def simplest(cls, msg):
        return msg
    def create(self, absolutepath):
        self.__log = file(absolutepath, 'a')
    def update(self, data, level):
        if level <= Log.LEVEL:
            self.__log.write(Log.simplest(data))
            self.__log.flush()
    def destroy(self):
        self.__log.close()
