#!/usr/bin/env python
#coding:utf-8    
    
    import Queue
    from threading import Thread
    from time import sleep
    
    q = Queue.Queue()
    for i in xrange(1,101):
        q.put(i)
    print "The queue size is %d " %q.qsize()
    
    print """Now,
    I want to get the even number,
    and push to the list named even_list, 
    The others push into list named other_list!!!"""
    
    even_l = []
    other_l = []
    def new_list(que):
        while True:
            try:
                element = que.get_nowait()
                size = que.qsize()
                
                if (element % 2 == 0) and (size != 0):
                    even_l.append(element)
                elif (element %2 != 0) and (size != 0):
                    other_l.append(element)
                else:
                    print "Have no element!!!"
            except:
                break
    
    if __name__ == "__main__":
        for i in range(5):
            t = Thread(target=new_list,args=(q,))
            t.start()
            print "This threading --- %s" %t.getName()
            sleep(0.5)
    print "The list even is: ",even_l
    
    print "The list other is: ",other_l