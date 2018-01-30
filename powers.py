#!/usr/bin/env python
#coding:utf-8

s = 1
def fun(x,y): 
    global s
    while y > 0:
        s = s*x
        y -= 1
    return s

while True:
    x = raw_input('Input the number x is: ').strip()
    x = int(x)
    y = raw_input('Input the number y is: ').strip()
    y = int(y)
    
    result = fun(x,y)
    print "The result is: %d" %result

