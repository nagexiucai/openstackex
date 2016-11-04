#!/usr/bin/env python
#coding=utf-8

from core.base import Base
import os_client_config
import shade

class Cloud(Base):
    def __init__(self, *args, **kws):
        super(Cloud, self).__init__(*args, **kws)
        self.__config = os_client_config.OpenStackConfig
    def create(self, *args, **kws):
        self.__cloud = shade.OpenStackCloud

class VM(Base):
    def create(self, *args, **kws):
        pass
    def _start(self):
        pass
    def _stop(self):
        pass
    def remove(self, *args, **kws):
        pass

if __name__ == '__main__':
    Cloud()
