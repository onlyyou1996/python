"""
2019.1.26
IDE:VS2017  Python 3.6 anaconda 5.2.0
【1】命名规则
1.变量名的长度不受限制，但其中的字符必须是字母、数字、或者下划线（_），而不能使用空格、连字符、标点符号、引号或其他字符。
2.变量名的第一个字符不能是数字，而必须是字母或下划线。
3.Python区分大小写。
4.不能将Python关键字用作变量名
【2】dir( )及和help( )
dir函数：查看变量可用的函数或方法
help函数：查看模块、函数、变量的详细说明：
【3】pep8规范
1 缩进与换行 每级缩进使用四个空格
2 限制每行的最大长度为79个字符
3 空行
    顶层函数和类之间使用两个空行
    类的方法之间用一个空行
    在函数中使用空行表示不同逻辑段落
4 导入位于文件的顶部
5 避免多余空格
6 注释
    注释要保持与时俱进 一句后面两个空格 跟注释
7 命名规范
    除了正常的命名规范外
    不要使用 大小写的L 大写的O 作为变量名
    类名首字母大写 内部类 加上前导下划线
    函数名应该小写 增强可读性可以使用下划线分割
8 其他
    别用 ‘==‘ 进行布尔值 和 True 或者 False 的比较 应该用 is
"""

#【练习】
#print and input
name=input("your name:")
print("Hello %s"%(name))
#运算符 绝大部分于C相同，故不全部列出
a=3
b=5
c=7
# 取余 备注%也是转义字符
d = c % a
print("7%%3=%d" %(d))
# 幂赋值
d = c ** a
print("7^3=%d" %(d))
# 整除
d = c // a
print("7整除3=%d" %(d))
# E记法
d = 7e3
print("7*10^3=%d" %(d))

'''
Python成员运算符
in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
'''
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]; 
if ( a in list ):
   print ("1 - 变量 a 在给定的列表中 list 中")
else:
   print ("1 - 变量 a 不在给定的列表中 list 中") 
if ( b not in list ):
   print ("2 - 变量 b 不在给定的列表中 list 中")
else:
   print ("2 - 变量 b 在给定的列表中 list 中") 
# 修改变量 a 的值
a = 2
if ( a in list ):
   print ("3 - 变量 a 在给定的列表中 list 中")
else:
   print ("3 - 变量 a 不在给定的列表中 list 中")
'''
Python身份运算符
is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
'''
a = 20
b = 20
if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")
if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识") 
# 修改变量 b 的值
b = 30
if ( a is b ):
   print ("3 - a 和 b 有相同的标识")
else:
   print ("3 - a 和 b 没有相同的标识") 
if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")
else:
   print ("4 - a 和 b 有相同的标识")


# 字符串 详解：http://www.runoob.com/python3/python3-string.html
a = "Hello"
b = "Python"
 
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
 
if( "H" in a) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")
 
if( "M" not in a) :
    print("M 不在变量 a 中")
else :
    print("M 在变量 a 中")
 
print (r'\n')
print (R'\n')

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

#字符串复制
s1 = 'hello'
s2 = s1          # s2 = 'hello'
#若指定长度
s1 = 'hello'
s2 = s1[0:2]     #s2 = 'he'

#字符串比较 
'''
（1）利用operator模块方法比较（python3.X取消了cmd函数）
包含的方法有：
lt(a, b) ———— 小于
le(a, b) ———— 小于等于
eq(a, b) ———— 等于
ne(a, b) ———— 不等于
ge(a, b) ———— 大于等于
gt(a, b) ———— 大于
'''
import operator
operator.eq('abc','edf') #根据ASCII码比较
operator.gt('abc','ab')
 
#（2）关系运算符比较（>,<,>=,<=,==,!=）
s1 = 'abc'
s2 = 'ab'
s1 > s2
s1 == s2

#字符串翻转
s1 = 'hello'
s2=s1[::-1]
print(s1)
print(s2)

'''
字符串内查找 
find方法：
检测字符串内是否包含子串str
语法为：
    str.find(str[,start,end])
    str为要查找的字符串；
    strat为查找起始位置，默认为0；
    end为查找终止位置，默认为字符串长度。
    若找到返回起始位置索引，否则返回-1
 '''

s1 = 'today is a fine day'
s1.find('is')       
s1.find('is',3)
s1.find('is',7,10)

'''
字符串内替换 
replace方法：
把字符串中的旧串替换成新串
语法为：
    str.replace(old,new[,max]) #old为旧串，new为新串，max可选，为替换次数
'''
s1 = 'today is a find day'
print(s1)
s2=s1.replace('find','rainy')
print(s2)

#【作业】
#最基础方案input（）函数+print（）函数
name=input("你的名字：")
sex=input("你的性别：")
age=input("你的年龄：")
print("你的名字：%s\n你的性别：%s\n你的年龄：%s" %(name,sex,age))


#采用类进行管理
class people:                           #定义类

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.year= 2019-int(age)
    def __del__(self):
        print("over")

    def displayEmployee(self):
        print("你的名字：%s 你的性别：%s 你的年龄：%s" %(name,sex,age))
        pass


person=[]                               #定义列表person
flag=1                                  #定义符号标志位
dir(people)
help(people)

while flag!='q':
    name = input("你的名字：")
    sex  = input("你的性别：")
    age  = input("你的年龄：")
    people1 = people(name,sex,age)
    people1.displayEmployee()
    person.append(people1)
    del people1
    flag = input("按q退出，其他任意键继续")

length=len(person)

for i in range(length):                 #遍历列表
    print("人员%d的名字:%s 性别:%s 出生年份分别是：%d" %(i+1,person[i].name,person[i].sex,person[i].year))