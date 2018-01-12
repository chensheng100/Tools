#!/usr/bin/env python
#coding:utf-8

import socket 
def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    client.send("<div style='height:100px;length:300px;background-color:#FF82AB'>Create a simple HTTP server!!</div>")

def main():
    sock = socket.socket()
    sock.bind(('localhost',8000))
    sock.listen(5)
    
    while True:
        connection,address = sock.accept()
        print "The new socket connection is: \n",connection
        print "The visitor address is: \n",address
        handle_request(connection)
        connection.close()
        
if __name__ == '__main__':
    main()
    
    
    
#sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)