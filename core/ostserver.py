#!/usr/bin/env python
#coding=utf-8
#by nagexiucai

from core.base import Base
from core.dbwrapper import MiniDBMS
from core.log import Log
from core.fs import FS
import socket
import threading
import atexit
import sys
sys.path.append(FS.inner_root())

class Command(Base): #todo: for extending
    DBS = {
        'timestamp': {
            'fields': ('status', 'at'),
            'types':('TEXT', 'TEXT')
            }
        }
    def __init__(self):
        super(Command, self).__init__()
        self.__db = MiniDBMS()
    def create(self):
        self.__db.create('timestamp', Command.DBS['timestamp']['fields'], Command.DBS['timestamp']['types'])
    def destroy(self):
        self.__db.destroy()
    def router(self, data_or_skt, addr):
        Log._('%s from %s' % (data_or_skt, addr), Log.VORBOSE)
        method = lambda _:_
        dick = ':)'
        try:
            data_or_skt.__class__.__name__.index('socket')
        except ValueError: #todo: udp pure string data
            method, dick = data_or_skt.split('#')
            Log._(method, Log.ORDINARY)
            method = getattr(self, method)
        else: #todo: tcp socket object, maybe queues or new threads are needed here for detail handling
            pass
        finally:
            method(dick, addr)
    def exit(self, reason, addr):
        Log._(reason, Log.SERIOUS)
        Listener.GO = False
    def timestamp(self, data, addr):
        self.__db.insert('timestamp', [data.split('@')])
        self.__db.show('timestamp')

class Listener(Base): #todo: support tcp as well
    GO = True
    UDP = (socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    BUFFER = 65535
    OSTSERVER = 'robert'
    PORT = 9527
    def __init__(self, *args):
        super(Listener, self).__init__()
        self.__skt = socket.socket(*args)
        self.__cmd = Command()
    def create(self):
        host = socket.gethostbyname(socket.gethostname())
        Log._(host, Log.ORDINARY)
        self.__skt.bind((host, Listener.PORT))
        self.__cmd.create()
    def strict(self):
        hostname = socket.gethostname()
        assert Listener.OSTSERVER == hostname or hostname.startswith(Listener.OSTSERVER)
    def start(self):
        self.create()
        while Listener.GO:
            data_or_skt, addr = self.__skt.recvfrom(Listener.BUFFER)
            self.despatch(data_or_skt, addr)
    def stop(self):
        self.__skt.close()
        self.__cmd.destroy()
    def despatch(self, data_or_skt, addr):
        threading.Thread(target=self.__cmd.router, args=(data_or_skt, addr)).start()

if __name__ == '__main__':
    server = Listener(*Listener.UDP)
    atexit.register(server.stop)
    server.start()
