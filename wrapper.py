#!/usr/bin/env python
#_*_ coding:utf-8 _*_


from functools import wraps  #���װ�����к������Ըı������
def my_wrapper(fun):
    
    @wraps(fun)             #���װ�����к������Ըı������
    def wrapper(*args,**kwargs):    #����������ٻ����޵�����
        print "Hello new leader!!!"
        fun(*args,**kwargs)         #����������ٻ����޵�����
    return wrapper                  #���غ���ʵ�壬�����Ǻ�����ʵ��

@my_wrapper     #�﷨��
def otopus(addr):
    print "name: %s" %otopus.__name__   #װ�����к�������
    print "The otopus live in the %s." %addr

@my_wrapper     #�﷨��
def jarryfish(num,color):
    print "name: %s" %jarryfish.__name__    #װ�����к�������
    print "jarryfish have so many legs,about %d hands and legs." %num
    print "It can change itself to be: %s" %color

print "what 's the of this function1? it's %s" %(otopus.__name__)
print "what 's the of this function2? it's %s" %(jarryfish.__name__)
print 
otopus('sea')
print "/\\" * 40
jarryfish(20,'multicolor')