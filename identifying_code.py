from random import randrange,choice

def identify()
    new_list = range(0,10)     #����������
    for i in range(97,123):    #Сд��ĸ׷�ӵ��б�
        abc = chr(i)
        new_list.append(abc)
        
    for i in range(65,90):     #��д��ĸ׷�ӵ��б�
        ABC = chr(i)
        new_list.append(ABC)

    #l = len(new_list)
    print '��ǰ��֤����:',
    for j in range(6):         #6λ�����֤��  
    #    print new_list[randrange(0,l)],
        print choice(new_list),