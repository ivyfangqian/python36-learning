# ---------------字符串String,字符串是最常见的类型之一，可以用单引号或者双引号包裹-------------
string = 'Hello World!'
string = "Hello World!"
print(type(string))

# 正确区分字符串与数字
string = '123'
print(type(string))
number = 123
print(type(number))

# 字符串为有序集合，我们可以按照顺序给字符串中的每个字符添加编号，称为索引
# 分为正向索引与反向索引
# 正向索引为从左往右分别编号为0,1,2...n-1
# 反向索引为从右往左分别编号为-1,-2,-3...-n
# 知道了索引，我们可以直接通过索引来取值
print(string[0])

# 或者通过切片操作来取值，[start:end],start<=x<end
print(string[0:3])
print(string[2:])
print(string[:-1])

# 得到翻转字符串
reverse = string[::-1]

# 成员操作符 in/not in ，查看字符串中是否含有某个值
print('e' in string)
print('ll' in string)

# 如何查看字符串长度
length = len(string)
print(length)

# 字符串是不可变的
# string[0] = 'U'

# ------------------------字符串拼接--------------------------------
# 用加号+来拼接字符串,或者用str.join(string)函数来进行拼接
# 用*来进行重复操作

string = 'ab' + 'cd'
print(string, type(string))

join_string = string.join("efg")
print(join_string, type(join_string))
print(join_string.join(["hi", "jk"]))
'.'.join(join_string)

str1 = 'qwe'
print(str1 * 2)
print(str1 * 3)

# 转义字符\
me = 'I\'m Ivy.'
print(me)

me = 'I\'m Ivy.\\'
print(me)

# -----------------------格式化字符串-----------------------
# 用 %操作符  的方式
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

# 如何清空与删除字符串
string = ''  # 空值
print
string

del string  # str为空，Null--》None
print
string

# ------------------------常用内置的字符串处理函数-----------------------
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
