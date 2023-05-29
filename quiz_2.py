#如何在一个函数内部修改全局变量
a = 10
def gb():
    global a
    a = 100
gb()
print (a)    
