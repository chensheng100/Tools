#!/usr/bin/env python 
#coding:utf-8

from time import sleep
import hashlib,getpass

def password():
    while True:
        passwd = getpass.getpass("\nPlease input the password: ").strip()
        hash = hashlib.md5()
        hash.update(passwd)
        passwd_true = hash.hexdigest()
        if passwd_true == '734d330b41a56b232eeb579352a5e103':
            print "*" * 80
            print " " * 20,"Welcome to use the super system."
            print "*" * 80
            break
        else:
            print "The password is incorrect!!!"
            
def username():
    while True:
        name = raw_input("Please input the username: ").strip()
        if name == 'chensheng':
            password()
            break
        else:
            print "The username is incorrect,please try again!"
            
if __name__ == "__main__":

    username()