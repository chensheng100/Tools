from random import randrange,choice

def identify()
    new_list = range(0,10)     #阿拉伯数字
    for i in range(97,123):    #小写字母追加到列表
        abc = chr(i)
        new_list.append(abc)
        
    for i in range(65,90):     #大写字母追加到列表
        ABC = chr(i)
        new_list.append(ABC)

    #l = len(new_list)
    print '当前验证码是:',
    for j in range(6):         #6位随机验证码  
    #    print new_list[randrange(0,l)],
        print choice(new_list),