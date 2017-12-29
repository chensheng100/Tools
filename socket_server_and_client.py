#!/usr/bin/env python
#coding:utf-8

import socket

sk = socket.socket()
ip_port = ('192.168.75.131',9999)
sk.bind(ip_port)
sk.listen(5)

while True:
    conn,addr = sk.accept()
    conn.send("Welcome to login!!!")
    flag = True
    while flag:
        data = conn.recv(1024)
        if data == "exit":
            print "This threading is shutdown!!!"
            flag = False
        else:
            print "Remote: ",data
            s_send = raw_input("Local_speak: ")
            conn.send(s_send)
    conn.close()        

    
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

        
        
        
        
