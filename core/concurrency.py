#!/usr/bin/env python
#coding=utf-8

import eventlet

if __name__ == "__main__":
    import multiprocessing
    import time

    def func(msg):
        print "msg:", msg
        time.sleep(3)
        print "end."

    pool = multiprocessing.Pool(processes = 50)
    for i in xrange(50):
        msg = "hi %d." %(i)
        pool.apply_async(func, (msg, ))

    print "!!!Mark~ Mark~ Mark!!!"
    pool.close()
    pool.join()
    print "Sub-process(es) done."
