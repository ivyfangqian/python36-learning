# --------------------------字典-----------------------------------
# 什么是字典？
# 字典是python中内置的无序的可变容器模型，可以存储任意类型的对象，
# 如字符串、数字、元组等其他的容器模型

# 如何创建字典？
my_dict = {"name": "andy", "age": 20}

# 字典中的元素以key：value的格式存储，一个key:value我们称之为一个键值对，
# 是字典中的一个元素，多个键值对之间，用逗号分隔,字典整体用花括号包裹
# 因为我们字典是无序的，所以我们无法使用之前list、tuple中的索引来对字典取值
# 字典使用key来唯一区分多个元素，因此字典中key是唯一的，且是不可变类型，如字符串，数字，元组
# 值可以为任意类型，甚至可以是程序员自定义的类型
print(my_dict["name"])

# dict.fromkeys(seq, val=None) 创建并返回一个新字典，以seq中的元素做该字典的键，val做该字典中所有键对应的初始值（默认为None）
print({}.fromkeys(["name", "age"], 0))
print({}.fromkeys(("name", "age"), 0))
print({}.fromkeys("abcd", 0))

print({"height": 170, "name": "zhangsan"}.fromkeys(["name", "age"], 0))

# 向字典中添加一个key,dict[key]=value,key不存在
adict = {"name": "candy", "age": 20}
adict["height"] = 170
print(adict)

# 如果key存在的，就更新key所对应的值
adict["height"] = 180
print(adict)

# adict.update(bdict) 将字典bdict的键值对添加到字典adict中
#     key存在，就更新value。key不存在就新增数据项
#     字典合并
append_dict = {"city": "beijing", "birthday": "2000-10-10", "height": 182}
adict.update(append_dict)
print(adict)

# 字典方法
# 判断key存在
#     has_key(key)
#     in 、not in
adict = {"name": "candy", "age": 20}

# print(adict.has_key("name"))
print(adict.__contains__("name"))
print("name" in adict)

# dict.keys() 返回一个包含字典所有KEY的列表
print(adict.keys())

# dict.values() 返回一个包含字典所有value的列表
print(adict.values())

# dict.items() 返回一个包含所有（键，值）元祖的列表
print(adict.items())

# str(dict)返回一个字典的字符串表示
print(str(adict))

# dict.get(key, default=None) 返回字典中key对应的值，若key不存在字典中，则返回default的值（default默认为None）
print(adict.get("name"))
# 不存在key，默认返回None
print(adict.get("height"))
print(adict.get("height", "Never"))

# dict.setdefault(key, default=None)
# 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
address = {"baidu": "百度", "google": "谷歌"}
print(address.setdefault("baidu"))
print(address)
print(address.setdefault("sougo"))
print(address)
print(address.setdefault("lagou", "拉勾"))
print(address)

# 删除数据项
# dict.pop(key)
#     (1)删除键key的项并返回key对应的 value值
#     如果key不存在，报错
#    (2) del dic[key]  删除键是'key'的条目
print(adict.pop("age"))

# 	popitem()
# 随机返回并删除字典中的一对键和值。
address.popitem()
print(address)

# del dic[key]  删除键是'key'的条目
adict = {"name": "candy", "age": 20}
del adict["age"]
print(adict)

# del dict      删除词典，将dict从内存中删除
# del adict

# dict.clear() 删除字典中的所有项或元素
print(adict.clear())

# dict.copy() 返回一个字典浅拷贝的副本
adict = {"name": ["candy", "tom"], "age": 20}
new_dict = adict.copy()
print(new_dict)

# 深拷贝
from copy import deepcopy

dc = deepcopy(adict)

# 1.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
string = "To be, or not to be: that is the question:\
            Whether 'tis nobler in the mind to suffer"
stats = {}.fromkeys(["alphas", "digits", "spaces", "others"], 0)
if string is None or string == "" or len(string) == 0:
    print("string不能为空")
else:
    for letter in string:
        if letter.isalpha():
            stats["alphas"] += 1
        elif letter.isdigit():
            stats["digits"] += 1
        elif letter.isspace():
            stats["spaces"] += 1
        else:
            stats["others"] += 1
print(stats)

# 练习：
# 编写一组数据，记录组内每个人的语文成绩
#     data = {
#          'JiaNaiLiang': 60,
#          'LiXiaoLu': 75,
#          'TianLaoShi': 99,
#          'MaSu': 88,
#          'KongLingHui': 35,
#          'LiuLaoShi': 100
#     }
#     a.算出平均分
#     b.再找出学霸

data = {
    'JiaNaiLiang': 60,
    'LiXiaoLu': 75,
    'TianLaoShi': 99,
    'MaSu': 88,
    'KongLingHui': 35,
    'LiuLaoShi': 100
}

sum_score = 0
max_score = 0
max_stu = ""

for key in data.keys():
    sum_score += data[key]
    if data[key] > max_score:
        max_score = data[key]
        max_stu = key

print
"平均分是%f，学霸是：%s" % (float(sum_score) / len(data), max_stu)

print(sum(data.values()) / len(data))

print(max(data.values()))

# 给定一个字符串，例如abcabcd，请你求得到该字符串中所有的长度大于等于2的子串，并统计每个字串出现的次数
string = "abcabcd"

if not isinstance(string, str):
    print
    "请输入一个字符串"
else:
    if len(string) == 0 or len(string) == 1:
        print
        "字符串长度小于2"
    else:
        sub_count = {}
        for i in range(len(string) - 1):
            for j in range(i + 1, len(string)):
                sub_string = string[i:j + 1]
                if sub_string in sub_count:
                    sub_count[sub_string] += 1
                else:
                    sub_count[sub_string] = 1

print(sub_count)
