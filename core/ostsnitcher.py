#!/usr/bin/env python
#coding=utf-8
#todo: run as soon as OS ready
#todo: configurable
#todo: time difference between host and vm

import socket
import time

class Reporter(object):
    UPD = (socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    OSTSERVER = 'robert' #notice: make sure that this hostname is same with ostserver
    ADDRESS = (socket.gethostbyname(OSTSERVER), 9527)
    MSG = 'timestamp#ready@%s' % time.time() #notice: make sure that this format is same with ostserver
    EXIT = 'exit#wayward'
    def __init__(self, *args):
        super(Reporter, self).__init__()
        self.skt = socket.socket(*args)
    def report(self, *args):
        self.skt.sendto(*args)
    def __del__(self):
        self.skt.close()

if __name__ == '__main__':
    rptr = Reporter(*Reporter.UPD)
    rptr.report(Reporter.MSG, Reporter.ADDRESS)
