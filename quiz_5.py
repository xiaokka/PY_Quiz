#使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
print(sorted(foo,key=lambda x:(x<0,abs(x))))
