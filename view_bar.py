#!/usr/bin/env python
#coding=utf-8

from time import sleep
def viewBar(i): 
    for count in range(0,i+1):
        second = 0.05
        sleep(second)
        print 'complete percent:%9.2f%%\r' % count,
       
viewBar(100)