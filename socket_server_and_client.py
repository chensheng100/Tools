#!/usr/bin/env python
#coding:utf-8



import socket

sk = socket.socket()
ip_port = ('192.168.75.131',9999)
sk.connect(ip_port)
flag = True
while flag:
    data = sk.recv(1024)
    print "Remote: ",data
    
    c_send = raw_input("Local_speak: ")
    if c_send == 'exit':
        flag = False
    else:
        sk.send(c_send) 

        
        
        
        
