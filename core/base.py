#!/usr/bin/env python
#coding=utf-8

class Base(object):
    def __init__(self, *args, **kws):
        super(Base, self).__init__()
    def create(self, *args, **kws):
        raise
    def update(self, *args, **kws):
        raise
    def remove(self, *args, **kws):
        raise
    def destroy(self, *args, **kws):
        raise
    def show(self, *args, **kws):
        raise
