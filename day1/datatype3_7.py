# ------------------------------------------------数据类型转换----------------------------------
# 不同数据类型之间的转换
# 字典可以转换为字符串，列表，元组类型
dic = {'name': 'ivy', 'age': 20}
print(type(str(dic)), str(dic))

print(type(list(dic)), list(dic))

print(type(tuple(dic)), tuple(dic))

# 元组可以转换为字符串，也可以转换为列表，但不可以转换为字典
tu = (1, 2, 3)
tu2str = tu.__str__()
print(type(tu2str), tu2str)

tu2list = list(tu)
print(type(tu2list), tu2list)

# 列表可以转换为字符串，也可以转换为元组，但也不可以转换为字典
li = ['w', 'o', 'r', 'l', 'd']
li2str = li.__str__()
print(type(li2str), li2str)

li2tuple = tuple(li)
print(type(li2tuple), li2tuple)

print(''.join(li))
print('-'.join(li))

# 字符串转换为列表、元组、字典
s = 'world'

str2list = list(s)
print(type(str2list), str2list)

str2tuple = tuple(s)
print(type(str2tuple), str2tuple)

s1 = "{'name':'ivy','age':20}"
str2dict = eval(s1)
print(type(str2dict), str2dict)
