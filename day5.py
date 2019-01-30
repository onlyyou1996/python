'''
【Day 5】
正则表达式re
os模块
datetime模块
http请求
【作业】
请用户输入一个时间，输出选项所对应的现在时间，告诉用户这两个时间相隔的天数，小时数，分钟数和秒数。
请用户输入电话及邮箱，判断用户输入是否合法。
对http://www.baidu.com 进行请求，并用正则化匹配图片内容。将百度图标爬取下来保存至本地
'''


#正则表达式re 
#详情见：http://www.runoob.com/python3/python3-reg-expressions.html
'''
正则表达式(Regular Expression)是一种文本模式，包括普通字符（例如，a 到 z 之间的字母）和特殊字符（称为"元字符"）。
正则表达式使用单个字符串来描述、匹配一系列匹配某个句法规则的字符串。
正则表达式是繁琐的，但它是强大的，学会之后的应用会让你除了提高效率外，会给你带来绝对的成就感。
只要认真阅读本教程，加上应用的时候进行一定的参考，掌握正则表达式不是问题。
许多程序设计语言都支持利用正则表达式进行字符串操作。
尽管这种搜索方法很有用，但它还是有限的。
通过理解 * 通配符的工作原理，引入了正则表达式所依赖的概念，但正则表达式功能更强大，而且更加灵活。
简介：http://www.runoob.com/regexp/regexp-intro.html
^ 为匹配输入字符串的开始位置。
[0-9]+匹配多个数字， [0-9] 匹配单个数字，+ 匹配一个或者多个。
abc$匹配字母 abc 并以 abc 结尾，$ 为匹配输入字符串的结束位置。
语法：http://www.runoob.com/regexp/regexp-syntax.html
正则表达式(regular expression)描述了一种字符串匹配的模式（pattern），
可以用来检查一个串是否含有某种子串、将匹配的子串替换或者从某个串中取出符合某个条件的子串等。
例如：
runoo+b，可以匹配 runoob、runooob、runoooooob 等，+ 号代表前面的字符必须至少出现一次（1次或多次）。
runoo*b，可以匹配 runob、runoob、runoooooob 等，* 号代表字符可以不出现，也可以出现一次或者多次（0次、或1次、或多次）。
colou?r 可以匹配 color 或者 colour，? 问号代表前面的字符最多只可以出现一次（0次、或1次）。
构造正则表达式的方法和创建数学表达式的方法一样。
也就是用多种元字符与运算符可以将小的表达式结合在一起来创建更大的表达式。
正则表达式的组件可以是单个的字符、字符集合、字符范围、字符间的选择或者所有这些组件的任意组合。
正则表达式是由普通字符（例如字符 a 到 z）以及特殊字符（称为"元字符"）组成的文字模式。
模式描述在搜索文本时要匹配的一个或多个字符串。正则表达式作为一个模板，将某个字符模式与所搜索的字符串进行匹配。
元字符：http://www.runoob.com/regexp/regexp-metachar.html
运算符优先级:http://www.runoob.com/regexp/regexp-operator.html
匹配规则：http://www.runoob.com/regexp/regexp-rule.html
在线工具：https://c.runoob.com/front-end/854
'''
'''
Python3 正则表达式
正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。
re 模块使 Python 语言拥有全部的正则表达式功能。
compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。
re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。

re.match(pattern, string, flags=0)

函数参数说明：
参数	描述
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志
匹配成功re.match方法返回一个匹配的对象，否则返回None。
我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
匹配对象方法	描述
group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
'''
import re
 
line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
'''
re.search 扫描整个字符串并返回第一个成功的匹配。
函数语法：

re.search(pattern, string, flags=0)

函数参数说明：
参数	描述
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志
匹配成功re.search方法返回一个匹配的对象，否则返回None。
我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
匹配对象方法	描述
group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()    	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
'''
import re
 
line = "Cats are smarter than dogs";
 
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")

#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
#而re.search匹配整个字符串，直到找到一个匹配。
 
import re
 
line = "Cats are smarter than dogs";
 
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")
 
matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print ("search --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

# OS模块
# 详见：http://www.runoob.com/python3/python3-os-file-methods.html

'''
import datetime
1.返回当前时间
datetime.datetime.now()
datetime.datetime(2017, 5, 9, 17, 7, 0, 514481)
2.时间戳转换成日期
datetime.date.fromtimestamp(1178766678)
datetime.date(2007, 5, 10)
3.当前时间+3天
datetime.datetime.now() + datetime.timedelta(+3)
datetime.datetime(2017, 5, 12, 17, 12, 42, 124379)
4.当前时间-3天
datetime.datetime.now() + datetime.timedelta(-3)
datetime.datetime(2017, 5, 6, 17, 13, 18, 474406)
5.当前时间+3小时
datetime.datetime.now() + datetime.timedelta(hours=3)
datetime.datetime(2017, 5, 9, 20, 13, 55, 678310)
6.当前时间+30分钟
datetime.datetime.now() + datetime.timedelta(minutes=30)
datetime.datetime(2017, 5, 9, 17, 44, 40, 392370)
'''

#http请求
'''
import requests
from requests.auth import HTTPBasicAuth
response = requests.post('http://localhost:8080/jenkins/job/check_python_version/build',auth=('admin','wangmin'))
print (response.status_code)
print (response.reason)
print(response.headers)
'''


'''
【作业】
请用户输入一个时间，输出选项所对应的现在时间，告诉用户这两个时间相隔的天数，小时数，分钟数和秒数。
请用户输入电话及邮箱，判断用户输入是否合法。
对http://www.baidu.com 进行请求，并用正则化匹配图片内容。将百度图标爬取下来保存至本地
'''
#请用户输入一个时间，输出选项所对应的现在时间，告诉用户这两个时间相隔的天数，小时数，分钟数和秒数。
import datetime
str=input("请输入一个时间(格式如2019, 1, 30, 8, 35, 9, 6127)：")
x=[]
time=''
l=len(str)
for i in range(l):
    if str[i]==',':
        time=int(time)
        x.append(time)
        time=''
    else:
        time=time+str[i]
time=int(time)
x.append(time)
del time
z=datetime.datetime(x[0],x[1],x[2],x[3],x[4],x[5])
del x
y=datetime.datetime.now()
x=y-z
print("您输入的时间是：",z)
print("现在的时间是：",y)
print("两者的时间差是：",x)

# 请用户输入电话及邮箱，判断用户输入是否合法。

import re

n = input("请输入一个手机号：")
if re.match(r'1[3,4,5,7,8]\d{9}',n):
    print("您输入的的手机号码是：\n",n)
    #中国联通：
    # 130，131，132，155，156，185，186，145，176
    if re.match(r'13[0,1,2]\d{8}',n) or \
        re.match(r"15[5,6]\d{8}",n) or \
        re.match(r"18[5,6]",n) or \
        re.match(r"145\d{8}",n) or \
        re.match(r"176\d{8}",n):
        print("该号码属于：中国联通")
    #中国移动
    # 134, 135 , 136, 137, 138, 139, 147, 150, 151,
    # 152, 157, 158, 159, 178, 182, 183, 184, 187, 188；
    elif re.match(r"13[4,5,6,7,8,9]\d{8}",n) or \
        re.match(r"147\d{8}|178\d{8}",n) or \
        re.match(r"15[0,1,2,7,8,9]\d{8}",n) or \
        re.match(r"18[2,3,4,7,8]\d{8}",n):
        print("该号码属于：中国移动")
    else:
        #中国电信
        #133,153,189
        print("该号码属于：中国电信")
else:
    print("请输入正确的手机号")
del n
n = input("请输入一个邮箱号：")
if re.match(r"^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$",n):
    print(n,"是一个邮箱")
else:
    print(n,"这不是一个邮箱")

#对http://www.baidu.com 进行请求，并用正则化匹配图片内容。将百度图标爬取下来保存至本地
#coding=utf-8

#urllib模块提供了读取Web页面数据的接口
import urllib.request
#re模块主要包含了正则表达式
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#定义一个getHtml()函数
def getHtml(url):
    page = urllib.request.urlopen(url)  #urllib.request.urlopen()方法用于打开一个URL地址
    html = page.read() #read()方法用于读取URL上的数据
    html = html.decode('utf-8') #python3
    return html

def getImg(html):
    reg = r'src="(.+?\.png)"'    #正则表达式，得到图片地址
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.   
    imglist = re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的数据
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.request.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    x = 0

    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'D:\E\%s.png' % x)
        x += 1


html = getHtml("https://www.baidu.com/")
print(getImg(html))