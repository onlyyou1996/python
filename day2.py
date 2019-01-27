'''
【Day 2】
1.列表
标志
基本操作(创建，append( )，pop( ) ,del( ), 深浅拷贝）
列表相关方法

2.元组
标志
基本操作（创建及不可变性）
提升
序列类型，相互转换及方法

【作业】
学习代码200-300行
定义一个列表，包含自己的家庭成员，并在指定位置插入给定元素，例如你的男女朋友名称等。再将男女朋友名字移除等操作。
'''

#【练习】
# 列表
'''
序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
Python有6个序列的内置类型，但最常见的是列表和元组。
序列都可以进行的操作包括索引，切片，加，乘，检查成员。
此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
列表的数据项不需要具有相同的类型
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：
详细见 http://www.runoob.com/python3/python3-list.html
'''
list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print("list1:",list1)
print("list2:",list2)
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
print("第三个元素为 : ", list2[2])
list2[2] = 2001
print("更新后的第三个元素为 : ", list2[2])
del list2[2]
print("删除第三个元素 : ", list2)

#在末尾添加元素
list1 = ['Google', 'Runoob', 'Taobao']
print("更新前的列表 : ", list1)
list1.append('Baidu')
print("更新后的列表 : ", list1)

# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
list1 = ['Google', 'Runoob', 'Taobao']
print ("列表现在为 : ", list1)
list1.pop()
print ("pop()后列表现在为 : ", list1)
list1.pop(1)
print ("pop(1)后列表现在为 : ", list1)

'''
深浅拷贝
在 Python 中，对象赋值实际上是对象的引用。当创建一个对象，然后把它赋给另一个变量的时候，
Python 并没有拷贝这个对象，而只是拷贝了这个对象的引用，我们称之为浅拷贝。
在 Python 中，为了使当进行赋值操作时，两个变量互补影响，可以使用 copy 模块中的 deepcopy 方法，称之为深拷贝。
'''
#浅复制
names = ["小明", "小红", ["张三", "李四", "王五"], "小黑", "小黄", "小白"]      # 复制一份列表
names2 = names.copy()       # 把李四 改成英文
names[2][1] = "Lisi"
print(names)
print(names2)

#深复制
import copy
names = ["小明", "小红", "小黑", ["粉色"], "小黄", "小白"]
deep_names = copy.deepcopy(names)
# 修改粉色为 Pink
names[3][0] = "Pink"
# 分别打印输出两个列表
print(names)
print(deep_names)


# 元组
'''
Python 的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
'''
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
#元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup3 = tup1 + tup2;
print (tup3)
#元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
del tup1;
len(tup3)       #计算元组元素个数。
max(tup2)       #返回元组中元素最大值。
min(tup2)       #返回元组中元素最小值。
tuple(list1)     #将列表转换为元组。


'''
【作业】
学习代码200-300行
定义一个列表，包含自己的家庭成员，并在指定位置插入给定元素，例如你的男女朋友名称等。再将男女朋友名字移除等操作。
'''
#采用类进行管理
class familymember:                           #定义类

    def __init__(self, name, sex, age, relationship):
        self.name = name
        self.sex = sex
        self.age = age
        self.relationship = relationship
    def __del__(self):
        print("over")

    def displayEmployee(self):
        print("名字：%s 性别：%s 年龄：%s 与我的关系：%s" %(name,sex,age,relationship))
        pass


person=[]                               #定义列表person
flag=1                                  #定义符号标志位
dir(familymember)
help(familymember)

while flag!='q':
    name = input("名字：")
    sex  = input("性别：")
    age  = input("年龄：")
    relationship = input("与我的关系")
    people = familymember(name,sex,age,relationship)
    people.displayEmployee()
    person.append(people)
    del people
    flag = input("按q退出，其他任意键继续")

length=len(person)
for i in range(length):                 #遍历列表
    print("人员%d的名字：%s 性别：%s 年龄：%s 与我的关系：%s" %(i+1,person[i].name,person[i].sex,person[i].age,person[i].relationship))

print('数据录入成功')
flag=1 
while flag!='q':
    flag = input('是否需要修改，添加按a，删除按d,退出按q：')
    if flag == 'a':
        local = input("插入的位置<%d" %(length))
        name = input("名字：")
        sex  = input("性别：")
        age  = input("年龄：")
        relationship = input("与我的关系")
        people = familymember(name,sex,age,relationship)
        people.displayEmployee()
        person.insert(int(local)+1,people)
        del people
        length=len(person)
        for i in range(length):                 #遍历列表
            print("人员%d的名字：%s 性别：%s 年龄：%s 与我的关系：%s" %(i+1,person[i].name,person[i].sex,person[i].age,person[i].relationship))
    elif flag == 'd':
        local = input("删除的位置<%d" %(length))
        del person[int(local)]
        length=len(person)
        for i in range(length):                 #遍历列表
            print("人员%d的名字：%s 性别：%s 年龄：%s 与我的关系：%s" %(i+1,person[i].name,person[i].sex,person[i].age,person[i].relationship))
    else:
        continue