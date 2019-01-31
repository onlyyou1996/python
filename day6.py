'''
函数关键字
函数的定义
函数参数与作用域
函数返回值
【作业】
实现random.sample方法
实现Max方法
实现判断两个字符串是否相等的方法
'''
'''
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
函数能提高应用的模块性，和代码的重复利用率。
你已经知道Python提供了许多内建函数，比如print()。
但你也可以自己创建函数，这被叫做用户自定义函数。
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
'''
def area(width, height):
    return width * height
 
def print_welcome(name):
    print("Welcome", name)
 
print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))


'''
参数传递
在 python 中，类型属于对象，变量是没有类型的
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
python 函数的参数传递：
不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。
比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
匿名函数
python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
'''
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))

'''
变量作用域
Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域
Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
也就是说这些语句内定义的变量，外部也可以访问。
global 和 nonlocal关键字
当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
以下实例修改全局变量 num：
'''
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) 
    num = 123
    print(num)
fun1()
print(num)

#!/usr/bin/python3
 
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()


'''
【作业】
实现random.sample方法
实现Max方法
实现判断两个字符串是否相等的方法
'''

import random
def random_sample(list2, length):
    temp=[]
    for i in range(length*3):
        x=int(random.uniform(0,len(list2)))
        temp.append(list2[x])
    temp2= list(set(temp))
    temp2.sort(key=temp.index) 
    return temp2[:length]

print(random_sample(range(10),3))

def i_max(list3):
    length=len(list3)
    max=list3[0]
    for i in range(1,length):
        if list3[i]>list3[i-1]:
            max=list3[i]
    return max
print(i_max(range(10)))


def cmp_str(str1,str2):
    l1=len(str1)
    l2=len(str2)
    if l1==l2:
        for i in range(l1):
            if str1[i]==str2[i]:
                continue
            else:
                print(str1,'和',str2,"不相等")
                return False
        print(str1,'和',str2,"相等")
        return True
    else:
        print(str1,'和',str2,"不相等")
        return False

print(cmp_str("Hello","Hello"))