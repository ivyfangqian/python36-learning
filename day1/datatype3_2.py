# --------------------------字符串String---------------------------------
# 字符串是最常见的类型之一，可以用单引号或者双引号包裹
string = 'Hello World!'
string = "Hello World!"
print(type(string))

# 可以灵活选择使用单引号还是双引号包裹
intr = "I'm peppa pig."

# 转义字符 \ , 还原特殊含义字符的原始意义
intr = 'I\'m peppa pig.'

path = "C:\\Users\\fqivy\\Desktop"

# 字符串中，有一些字符是具有特殊含义的
# \n 换行
# \r 回车
# \t 制表符
# \f 换页
# \b 退格
# r,原样输出字符串，输出字符串的原始格式
path = r"C:\Users\fqivy\Desktop"

# 正确区分字符串与数字
string = '123'
print(type(string))
number = 123
print(type(number))

# java中，1+"aaa"-->"1aaa"
# 数字与字符串不可以直接拼接
# print(1+"aaa")

# 数字强制转换为字符串
num_str = str(number)
print(type(num_str), num_str)

# -----------------------格式化输出字符串-----------------------
# 假如我们要输出一行字符串，xxx，你好，xx月份话费账单已出，您的话费为xxx.xx元，您的账户余额为xx.xx元。
# 如果用原始的方式，逗号拼接，或者加号拼接，实在是太费劲了
name = "xiaoming"
month = 8
tel_charge = 65.60
remaining = 20.50
print(name, "，你好，", month, "月份话费账单已出，您的话费为", tel_charge, "元，您的账户余额为", remaining, "元。")
print(name + "，你好，" + str(month) + "月份话费账单已出，您的话费为" + str(tel_charge) + "元，您的账户余额为" + str(remaining) + "元。")

# 用 %操作符  的方式
# %s 字符串
# %c 单个字符
# %b 二进制整数
# %d 十进制整数
# %i 十进制整数
# %f 浮点数
# %F 浮点数
# %.2f 保留两位小数的浮点数
# 我们可以使用如上内容进行字符串格式化，但是注意，
# 如果字符串中需要两个参数，传参必须为两个，多了少了都会报错
intr = "I am %s, I am %d years old." % ("tom", 3)
print(intr)

# 使用format函数进行格式化
# str.format(text)
# str中包含占位符，text中是要填充的内容
# 使用'{}'占位符
# 使用 '{0}', '{1}'形式的占位符
# 使用'{name}'形式的占位符
# 传参少于指定占位符个数会报错，多于占位符个数会被存储起来
intr = "I am {},I am {} years old!"
print(intr.format("candy", 20))

intr = "{1} I am {0},I am {1} years old!"
print(intr.format("candy", 20))

intr = "I am {name},I am {age} years old!"
print(intr.format(name="candy", age=20))

# -----------------------格式化输出字符串-----------------------
# 用 格式符  的方式
# %s 字符串
# %c 单个字符
# %b 二进制整数
# %d 十进制整数
# %i 十进制整数
# %f 浮点数
# %F 浮点数
# %.2f 保留两位小数的浮点数
intr = "I am %s, I am %d years old." % ("tom", 3)
print(intr)

# 使用format函数进行格式化
# str.format(text)
# str中包含占位符，text中是要填充的内容
# 使用'{}'占位符
# 使用 '{0}', '{1}'形式的占位符
# 使用'{name}'形式的占位符
# 传参少于指定占位符个数会报错，多于占位符个数会被存储起来
intr = "I am {},I am {} years old!"
print(intr.format("candy", 20))

intr = "{1} I am {0},I am {1} years old!"
print(intr.format("candy", 20))

intr = "I am {name},I am {age} years old!"
print(intr.format(name="candy", age=20))

# 练习：
# 1.
# 习题：编写一个get请求地址，参数protocol ="",url ="", domain ="", data = ""，根据以上参数返回一个get请求的完整链接

protocol = 'http'
domain = '192.168.2.111'
url = 'huice/event/api/add'
data = "title='python大会'&time='2018-01-06'"

# http: // 192.168.2.111 / huice / event / api / add?title = python大会 & time = 2018 - 01 - 06


url = "{protocol}://{domain}/{url}?{data}"
print(url.format(protocol=protocol, domain=domain, url=url, data=data))

# 2.拼接一个动态函数
# def test_Case(self):
#     '测试用例描述'
#     execute_case(data)
#
#
# 其中用例编号，用例描述，execute_case方法参数
# 均为变量
#
# case = 'case01'
# desc = '测试用例一'
# data = 'id=1'
#
#
# def test_case01(self):
#     '测试用例一'
#     execute_case('id=1')

case = 'case01'
desc = '测试用例一'
data = 'id=1'

test_case = """def test_{case}(self):
    '{desc}'
    execute_case('{data}')"""
print(test_case.format(case=case, desc=desc, data=data))

# --------------------------字符串索引与切片----------------------------------------------------
# 字符串为有序集合，我们可以按照顺序给字符串中的每个字符添加编号，称为索引
# 分为正向索引与反向索引
# 正向索引为从左往右分别编号为0,1,2...n-1
# 反向索引为从右往左分别编号为-1,-2,-3...-n
# 知道了索引，我们可以直接通过索引来取值
string = "hello python"
print(string[0])

# 索引值不能超出索引范围，不然会报IndexError: string index out of range
# print(string[100])

# 或者通过切片操作来取值，[start:end:step],start<=x<end
print(string[0:3])

# 取值包含末尾最后一个字符
print(string[1:len(string)])
print(string[2:])
# 取值从字符串第一个值开始
print(string[:-1])

# 切片时，start,end值如果超出索引范围，不会报错
print(string[5:100])

print(string[85:100])

# 可以设置步长,每隔一个步长取一个字符
print(string[1:-1:2])

# 得到翻转字符串
reverse = string[::-1]

# 练习:
# 判断一个字符串是否是回文字符串
# string = "madam"

# 成员运算符 in/not in ，查看字符串中是否含有某个值
print('e' in string)
print('ll' in string)

# 如何查看字符串长度
length = len(string)
print(length)
# 空字符串长度为0
print(len(""))

# 字符串是不可变的
# string[0] = 'U'

# 如何清空与删除字符串
string = ''  # 空值
print(string)

del string  # str为空，Null--》None
# print(string)

# ------------------------字符串拼接--------------------------------
# 用加号+来拼接字符串,或者用str.join(string)函数来进行拼接
# 用*来进行重复操作
string = 'ab' + 'cd'
print(string, type(string))

# 使用"sep".join()
join_string = string.join("123")
print(join_string, type(join_string))
print("-".join(["hi", "jk"]))
print('.'.join("helloworld"))

str1 = 'qwe'
print(str1 * 2)
print(str1 * 3)

# 如何清空与删除字符串
string = ''  # 空值
print(string)

del string  # str为空，Null--》None
# print(string)

# ------------------------常用内置的字符串处理函数-----------------------
string = "helloworld"
print(dir(string))

# 字符串查找
# (1)find
# str.find(target, [start, end) )
# 在字符串中查找指定字符串首次出现的index，找不到时返回 - 1
# 找到的是首次出现的索引
# (2)index
# str.index(target, [start, end) )
# 在字符串里查找子串第一次出现的位置, 找不到子串会抛出异常
# (3)使用成员运算符
# str1 in str2
# 存在则返回True，不存在则返回False
name = "candy"
print(name.find("can"))

print(name.index("an"))

print("can" in name)

# 字符串分割
# str.split(sep, [, max])
# 将一个字符串分裂成多个字符串组成的列表
# 不带参数时以空格进行分割
# 带参数时，以该参数进行分割
# 未查询到分隔符时，列表只包含原始字符串
ip = "192.168.2.3"
print(ip.split("."))

print(ip.split(".", 2))

# 练习：
# 检查get请求的参数中是否包含sign, 如果包含将参数值替换为空格，重新拼接为参数字符串
# title = 华为春季新品发布会 & sign = 0 & limit = 100 & status = 0 & address = 国家会议中心 & time = 2018 - 03 - 28

# 字符串大小写
# str.upper() - -转大写
# str.lower() - -转小写
# str.capitalize() - -首字母大写
# str.istitle() - -是否是首字母大写的
# str.isupper() - -字母是否全是大写
# str.islower() - -字母是否全是小写
#
# 字符串去空格
# str.strip() - -去掉字符串的左右空格
# str.lstrip() - -去掉字符串的左边空格
# str.rstrip() - -去掉字符串的右边空格
#
# 其他
# str.isalnum() - -是否全是字母和数字，并至少有一个字符
# str.isalpha() - -是否全是字母，并至少有一个字符
# str.isdigit() - -是否全是数字，并至少有一个字符
# str.isspace() - -是否全是空白字符，并至少有一个字符
string = " "
print(string.isspace())
# str.count(target, [min, max))   --统计某个字符在字符串中出现的次数
print(intr.count("candy"))
# str.startswith(target) - -判断字符串是否以某个字符串开始
print(intr.startswith("I"))
# str.endswith(target) - -判断字符串是否以某个字符串结尾
print(intr.endswith("!"))
