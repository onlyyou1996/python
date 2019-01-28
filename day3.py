'''
【Day 3】
【dict字典】
定义
创建
字典的相关方法

【set集合】
特性
创建
方法

【file文件读取】
打开文件方式（读写两种方式）
文件对象的操作方法
学习对excel及csv文件进行操作

【作业】
学习代码200-300行
读取一个文件【文件将在之后给出】，将文件中转换为字典，并判断字典中是否有value值对应多个key值。
'''


# 【dict字典】
'''
方法详见：http://www.runoob.com/python3/python3-dictionary.html
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
两个重要的点需要记住：
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print ("dict['Name']: ", dict['Name'])
以上实例输出结果：
dict['Name']:  小菜鸟
2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
dict = {['Name']: 'Runoob', 'Age': 7}
print ("dict['Name']: ", dict['Name'])
'''

# 定义及访问方法
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

# 修改方法
dict['Age'] = 8;             # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

# 字典的删除
del dict['Name'] # 删除键 'Name'
dict.clear()     # 清空字典
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del dict         # 删除字典

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
str(dict)        # 输出字典，以可打印的字符串表示。
len(dict)        # 计算字典元素个数，即键的总数 
del dict         # 删除字典

# 【set集合】
'''
详见：http://www.runoob.com/python3/python3-set.html
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''

# 集合初始化及元素添加
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
# 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等
thisset.update({1,3})
print(thisset)
thisset.update([1,4],[5,6])  
print(thisset)

# 移除元素
thisset.remove("Taobao")
# 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。
thisset.discard("Facebook")
# 随机删除集合中的一个元素
x = thisset.pop() 
print(x)

# 计算集合元素个数
len(thisset)

# 判断元素是否在集合中存在
"Runoob" in thisset

# 清空集合
thisset.clear()


# 【file文件读取】
'''
详细见：http://www.runoob.com/python3/python3-file-methods.html
open() 方法
Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。
注意：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。
open(file, mode='r')
完整的语法格式为：
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

#file 是文件路径，mode 是文件打开模式，常用的应该还有一个encoding 编码格式。
#这个是文件打开模式
    'r'       open for reading (default)  默认只读
    'w'       open for writing, truncating the file first 以写的方式打开文件，会覆盖源文件
    'x'       create a new file and open it for writing，创建一个新的文件打开并进行写入操作，如果这个文件已经存在，则会报错
    'a'       open for writing, appending to the end of the file if it exists 以写的方式打开文件，当执行写入操作时，会将写入的内容追加在原文件之后
    'b'       binary mode 以二进制方式打开文件
    't'       text mode (default) 以文本模式打开
    '+'       open a disk file for updating (reading and writing) 可读写模式，可添加到其他模式中用
    'U'       universal newline mode (deprecated) 通用换行符

'''

# 【作业】
# 读取一个文件【文件将在之后给出】，将文件中转换为字典，并判断字典中是否有value值对应多个key值。

# 文件打开一般使用/而不是\，避免出现歧义
f=open('E:/github/python/homework.txt','r', encoding='UTF-8')
file=f.read()
print(file)
print(type(file))
# 以字符串形式保存
dict = {}
# 定义一个word缓冲列表
word=[]
l=len(file)
flag=0
# 定义两个字符串用于保存字典中的key以及用于拼接的str
key=''
str=''
value=[]
#以下方法为最基本方案，可以多种方式进行优化，但此方案可以对每个字符进行控制。
for i in range(l):                  #遍历file
    if file[i].isspace():           #如果是空格或者换行
        l2=len(word)                #获取列表长度
        for j in range(l2):         #将列表中的字符串拼接
            str = str+word[j]
        word.clear()                #清空列表
        flag += 1                   #标志位+1
        if flag==1:                 #第一个空格
            key=str                 #将str赋值给key
            str=''                  #情况str
        elif flag==2:               #第二个空格
            value.append(str)       #将str赋值给value
            str=''
        elif flag==3:               #这个是换行符
            value.append(str)       #将str赋值给value
            dict[key] = value       #添加信息到字典里面
            key=''                  #清空所有数值
            str=''
            value=[]
            flag=0
    else:                           # 将字符串一个一个加入到列表
        word.append(file[i])
print (dict)
f.close()

#遍历字典
for key in dict:
    for i in range(2):
        for key2 in dict:
            for j in range(2):
                if dict[key][i]==dict[key2][j]:
                    cnt=1;
if cnt==1:
    print("有重复")
                    