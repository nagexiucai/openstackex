#!/usr/bin/env python
#coding=utf-8

from core.ostsnitcher import Reporter

#todo: need run 2 times continuously to ensure ostserver going to die correctly
#      because ostserver using blocked method 'recvfrom'
#      the go flag had been clear when get exit at the first time
#      but the main thread is still blocked by 'recvfrom'
#      there must be some better means to resolve this problem

rptr = Reporter(*Reporter.UPD)
rptr.report(Reporter.EXIT, Reporter.ADDRESS)
rptr.report(Reporter.EXIT, Reporter.ADDRESS)
