'''
【Day 4】
判断语句（要求掌握多条件判断）
循环语句
三目表达式
容器
可迭代对象
迭代器
生成器
【作业】
学习代码200-300行
请对方输入一个0-9之间的数字，进行检查，
若不是数字提示：您输入的不是数字，请输入0-9间的数字，
若数字不在0-9范围内，提示用户输入0-9之间的数字，直至用户输入正确。
系统随机生成一个长度为3的数字列表，且列表中元素在0-9之间并且不相等。
将用户输入与该列表进行比较，若为列表第一个元素，则荣获第一名，列表第二个元素，则荣获第二名，列表第三个名字，则荣获第三名，
否则提示用户未得奖，输入1重新开始游戏，输入2则结束游戏。
注意：每次游戏中列表中数字要求随机生成，每轮游戏都不相等。
'''

# 判断语句
'''
Python中if语句的一般形式如下所示：
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
如果 "condition_1" 为False，将判断 "condition_2"
如果"condition_2" 为 True 将执行 "statement_block_2" 块语句
如果 "condition_2" 为False，将执行"statement_block_3"块语句
Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。
注意：
1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在Python中没有switch – case语句。
'''
num=int(input("输入一个数字："))
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")


# 循环语句
# 此部分与C++相似不进行赘述
# pass 语句
# Python pass是空语句，是为了保持程序结构的完整性。
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")

for letter in 'Runoob':     # 第一个实例
   if letter == 'b':
      break
   print ('当前字母为 :', letter)
  
var = 10                    # 第二个实例
while var > 0:              
   print ('当期变量值为 :', var)
   var = var -1
   if var == 5:
      break
 
print ("Good bye!")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')


# 三目表达式

x = int(input("please enter first integer:"))
y = int(input("please enter second integer:"))
#一般的写法
if (x == y):
     print("两数相同！")
elif(x > y):
     print("较大的数为：",x)
else:
     print("较大的数为：",y)            
# 三目运算符写法
print(x if(x>y) else y)


'''
迭代器
迭代是Python最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器：
'''

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
 
myclass = MyNumbers()
myiter = iter(myclass)
 
for x in myiter:
  print(x)


'''
生成器
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
调用一个生成器函数，返回的是一个迭代器对象。
'''

import sys
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()


'''
【作业】
学习代码200-300行
请对方输入一个0-9之间的数字，进行检查，
若不是数字提示：您输入的不是数字，请输入0-9间的数字，
若数字不在0-9范围内，提示用户输入0-9之间的数字，直至用户输入正确。
系统随机生成一个长度为3的数字列表，且列表中元素在0-9之间并且不相等。
将用户输入与该列表进行比较，若为列表第一个元素，则荣获第一名，列表第二个元素，则荣获第二名，列表第三个名字，则荣获第三名，
否则提示用户未得奖，输入1重新开始游戏，输入2则结束游戏。
注意：每次游戏中列表中数字要求随机生成，每轮游戏都不相等。
'''
import random
flag = 1
while flag!=2 :
    while 1:
        num=input('请输入一个0-9之间的数字')
        if num.isdigit():   #判断是否为数字
            num=int(num)
            if num in range(10):
                break
            else:
                print('范围不再0-9中，请输入0-9之间的数字')
        else:
            print('您输入的不是数字，请输入0-9间的数字')
            continue 
    alist = random.sample(range(0,9),3) #random.sample()生成不相同的随机数
    print(alist)
    if num==alist[1]:
        print('荣获第一名')
    elif num==alist[2]:
        print('荣获第二名')
    elif num==alist[3]:
        print('荣获第三名')
    else:
        print('未得奖')
    flag = input('输入1重新开始游戏，输入2则结束游戏')
    flag = int(flag)




