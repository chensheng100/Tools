



from random import randint

list_a = []
for i in range(10):
    n = randint(1,10)
    list_a.append(n)
print "随机序列: \n",list_a
length = len(list_a)
print "The length of list_a is :%d" %length 

for i in xrange(length-1,0,-1):
    for j in xrange(i):
        if list_a[j] > list_a[j+1]:
            list_a[j],list_a[j+1] = list_a[j+1],list_a[j]
    print "执行冒泡排序后: \n",list_a