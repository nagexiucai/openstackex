#!/usr/bin/env python
#coding=utf-8

from core.base import Base
from os import mkdir, path

class FS(Base):
    @staticmethod
    def is_file(path):
        return path.isfile(path)
    @staticmethod
    def is_folder(path):
        return path.isdir(path)
    @staticmethod
    def maybe_path(path):
        return path.exists(path)
    @staticmethod
    def join_path(*paths):
        return path.join(*paths)
    @staticmethod
    def mkdirs(path, mode=0777):
        mkdir(path, mode)
    def __init__(self, *args, **kws):
        super(FS, self).__init__()
    
