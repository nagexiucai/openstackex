#!/usr/bin/env python
#coding=utf-8
#by nagexiucai

import eventlet

def coroutine(func, *things):
    pool = eventlet.GreenPool() #size=1000 by default

def simple(count, func, *args):
    import multiprocessing
    pool = multiprocessing.Pool(processes = count)
    results = [pool.apply_async(func, args) for _ in xrange(count)]
    pool.close()
    pool.join()
    return results

def test(x, y): #notice: must defined out of __main__
    print x + y

if __name__ == "__main__":
    simple(50, test, 9527, 9527)
