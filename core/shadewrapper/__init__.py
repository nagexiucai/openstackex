#!/usr/bin/env python
#coding=utf-8

from core.base import Base
import shade
import os

class Cloud(Base):
    @staticmethod
    def update_environment_variables(**kws):
        os.environ.update(kws)
    def __init__(self, *args, **kws):
        super(Cloud, self).__init__(*args, **kws)
    def create(self, *args, **kws):
        self.backend = shade.openstack_cloud()

class Net(Base):
    pass

class VM(Base):
    def __init__(self, platform):
        self.platform = platform
    def create(self, **kws):
        self.platform.create_server(**kws)
    def _start(self):
        pass
    def _stop(self):
        pass
    def remove(self, *args, **kws):
        pass

if __name__ == '__main__':
    Cloud()
