#!/usr/bin/env python
#_*_ coding:utf-8 _*_


from functools import wraps  #解决装饰器中函数属性改变的问题
def my_wrapper(fun):
    
    @wraps(fun)             #解决装饰器中函数属性改变的问题
    def wrapper(*args,**kwargs):    #解决参数多少或有无得问题
        print "Hello new leader!!!"
        fun(*args,**kwargs)         #解决参数多少或有无得问题
    return wrapper                  #返回函数实体，而不是函数的实例

@my_wrapper     #语法糖
def otopus(addr):
    print "name: %s" %otopus.__name__   #装饰器中函数属性
    print "The otopus live in the %s." %addr

@my_wrapper     #语法糖
def jarryfish(num,color):
    print "name: %s" %jarryfish.__name__    #装饰器中函数属性
    print "jarryfish have so many legs,about %d hands and legs." %num
    print "It can change itself to be: %s" %color

print "what 's the of this function1? it's %s" %(otopus.__name__)
print "what 's the of this function2? it's %s" %(jarryfish.__name__)
print 
otopus('sea')
print "/\\" * 40
jarryfish(20,'multicolor')