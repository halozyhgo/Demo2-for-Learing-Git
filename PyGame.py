#第一次修改後的PyGame.py文件
'''
from __future__ import absolute_import

import os
import sys

# If we are running from a wheel, add the wheel to sys.path
# This allows the usage python pip-*.whl/pip install pip-*.whl
if __package__ == '':
    # __file__ is pip-*.whl/pip/__main__.py
    # first dirname call strips of '/__main__.py', second strips off '/pip'
    # Resulting path is the name of the wheel itself
    # Add that to sys.path so we can import pip
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

from pip._internal import main as _main  # noqa

if __name__ == '__main__':
    sys.exit(_main())
'''
# coding:UTF-8
'''
num = complex(10,2)     #复数
print(num)
print(num.real)
print(num.imag)
print(num.conjugate())

num_a = 0;
num_b = 1;
while num_b<1000:
    print(num_b,end="、")
    num_a,num_b = num_b,num_a+num_b

for i in {1,2,3}:
    print(i)
for i in  range(50,100):
    if(i%10==0):
        print()
    print(i,end="、")
sum = 0;
for num in range(101):
    sum+=num
else:
    print("%s"%sum)

msg = "www.abcdefg.com"
for item in msg:
    if 97<=ord(item)<=122:
        upper_num = ord(item)-32
        print(chr(upper_num),end = "、")
    else:       #如果不是字母
        print(item,end="、")

for x in range(1,10):
    for y in range(1,x+1):
        print("%d*%d=%d"%(x,y,x*y),end ="\t")
    print()

#输出三角形
line = 5
for x in range(line):
    for z in range(0,line-x):
        print("",end=" ")
    for y in range(0,x+1):
        print("*",end=" ")
    print()

line =5
for x in range(0,line):
    print(" "*(line-x))
    print("* "*(x+1))
    print()

#列表的使用
info = ["zyh","123","halo"]
info[1] = "aiosjdoiaj"
for i in range(len(info)):
    print(info[i],end="、")

info = [];
print("列表长度：%d" % len(info))
info.append("大辉")
print("列表信息：%s" % info)
info.insert(0,0)
print("列表长度:%d,列表信息：%s"%(len(info),info))   #需要将后面的参数全部放进括号内
print("地址：%s,内容：%s"%(id(info),info))
print("***************************")
plus = [1,2,3,4]
info.extend(plus)
info.extend(["2",2,3,4])
print("地址：%s,内容：%s"%(id(info),info))    #列表扩充是在源地址上扩充

infos = []
for item in range(10):
    infos.append("大辉+%d"%item)

print("列表信息：%s" % infos)
for item in range(len(infos)):
    print("被删除的信息为：%s" % infos.pop(0))

#format 函数
name = "zyh"
age  = 20
gender = "男"
message = "姓名：{}、年龄：{}、性别：{}".format(name,age,gender)
print(message)


info = "新乡学院abc.d.ef"
print(info.center(50))
print(info.upper())
print(info.lower())
print("zyhhdffohfoahfoqh".capitalize())     #首字母大写
print(info.find("abc")) #返回查找字符串在info中出现的第一个位置
print(info.find("12"))#如果找不到就返回-1

url = ".".join(["www","abcdef","com"])
author = "_".join("Halo")
print("作者：{author_param},网站：{url_param}".format(author_param=author,url_param=url))


# 数据的拆分
ip = "192.168.1.123"
print("数据全部拆分：%s" % ip.split("."))
print("数据全部拆分：%s" % ip.split(".",2))
date = "2020-02-17 21:56:33"    #日期时间
result = date.split(" ")    #按照空格进行拆分
print("日期时间拆分：%s" % result[0].split("-"))
print("日期时间拆分：%s" % result[1].split(":"))


str_a = "www abc com"
mtr_a = str_a.maketrans(" ",".")
print(str_a)
print(str_a.translate(mtr_a))
print(mtr_a)

str_b = "www_abc_com;\t\t www_iidihai_com";
mt_b = str_b.maketrans("_",".",";")
print(str_b.translate(mt_b))

login_info = input("请输入登陆信息（格式：用户名：密码）：").strip()
if (len(login_info)==0 or login_info.find(":")==-1):
    print("输入信息有错误请重新输入")
else:
    result = login_info.split(":")
    if(result[0]=="zyh" and result[1]=="123"):
        print("欢迎%s的到来" % result[0])


number = dict(name = "大辉",age = "21",score = "361")
for key in number:
    print("key 为：%s " % key)
if "name" in number:
    print("name: %s " % number["name"])


# 字典的迭代：
member = dict(name = "dahui",age = "1212",score = "361")
for ke,val in member.items():
    print("%s = %s " % (ke,val))

info = {"mldn":"www.abc.com","teacher":"dahui",None:"ubaiusdiuahdoash"}
print("mldn---->/t %s" % info["mldn"])
print("teacher---->/t %s" % info["teacher"])
print("None---->/t %s" % info[None])

info = {"mldn":"www.abc.com","teacher":"dahui",None:"ubsh",None : "就他妈的空"}
print("空的是否覆盖了呢  %s" % info[None])

# 将列表转化成字典，每一个列表由两部分组成
info = dict([["名字","张大头"],["外号","小乌龟"]]);   #此时将列表转换成字典
member = dict(name = "李永乐",surname = "永乐大帝")    #此时将元组转换成字典
print(info)
print(member)
#if "name" in member:
#    print("key为 %s  value 为：%s" % ("name",member["name"]))
#if "名字" in info:
#    print("key为 %s  value 为：%s" % ("名字",info["名字"]))
#else:
#   print("不在")
info.update({"名字":"张小辉","123":"qeuohshdoh"})
print(info)

nums = dict(one = 1,two = 2,three = 3)
print("字典元素个数：%d" % len(nums))
print("字典Value 的总和：%d " % sum(nums.values()))
print("字典Value 的最大值：%d " % max(nums.values()))
print("字典Value 的最小值：%d " % min(nums.values()))
print("字典Key 的最大值：%s " % max(nums.keys()))
print("字典Key 的最小值：%s " % min(nums.keys()))

def get_info():
    """
        定义一个信息获取的功能函数操作
    :return: 返回给调用出显示的内容
    """
    return "abcdefghijklmnopqrstuvwxyz"
print(get_info())
print(type(get_info()),type(len("hwdohq")))

def print_data(count):
    def out(data):
        nonlocal count    #前面加上 nonlocal 表示非本地变量
        count+=1;       #count不加任何修饰的时候就表示本地变量
        return "第{}次输出：{}".format(count,data)
    return out
oa = print_data(0)
print(oa("www.abc.com"))
print(oa("www.edf.com"))

#lambda表达式
def sum1(x,y):
    return x+y

sum2 = lambda x,y:x+y
print(sum1(2,3))
print(sum2(5,5))
'''
class Math:
    def add(self, num_a, num_b):
        return num_a + num_b
    def sub(self, num_a, num_b):
        return num_a - num_b


















