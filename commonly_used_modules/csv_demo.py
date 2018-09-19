import csv
import os

# 获取csv文件对象
f = open(r".\demo.csv", encoding="utf-8")
csv_file = csv.reader(f)

# 读取表头
headers = next(csv_file)

# 循环读取csv内容
for line in csv_file:
    print(line)

# 但是这样的话，读到的每一行是一个列表，要是想要读取每一行的每个具体值，
# 就需要使用line[0],line[1]这种方法
# 所以我们可以换一种方法，把csv文件读取到一个字典中去
f = open(r".\demo.csv", encoding="utf-8")
csv_f = csv.DictReader(f)

# 循环读取每一行内容，每一行得到一个OrderedDict对象
# OrderedDict([('id', '1'), ('name', '张三'), ('age', '20'), ('height', '170'), ('gender', '男')])
for row in csv_f:
    print(row["id"])
    print(row["name"])

# csv文件写入
headers = ["id", "name", "age", "height"]
content = [(1, "小明", 18, 175),
           (2, "小红", 18, 160)]

# 注意：打开文件时，要用w模式，并且设置newline="",否则，在写入时，总会多加一个空行
f = open(r".\demo.csv", "w", encoding="utf-8", newline="")
csv_w = csv.writer(f)
csv_w.writerow(headers)
csv_w.writerows(content)

# 如果内容是存放在字典中，写入csv文件，需要在使用DictWriter
headers = ["id", "name", "age", "height"]
content = [{"id": 1, "name": "小明", "age": 18, "height": 175},
           {"id": 2, "name": "小红", "age": 18, "height": 165},
           {"id": 3, "name": "小刚", "age": 17, "height": 185},
           ]

f = open(r".\demo.csv", "w", encoding="utf-8", newline="")
csv_w = csv.DictWriter(f, headers)
# 写入表头信息
csv_w.writeheader()
# 写入内容
csv_w.writerows(content)

# 如果你读取CSV数据的目的是做数据分析和统计的话， 你可能需要看一看 Pandas 包。
# Pandas 包含了一个非常方便的函数叫 pandas.read_csv() ， 它可以加载CSV数据到一个 DataFrame 对象中去。
# 然后利用这个对象你就可以生成各种形式的统计、过滤数据以及执行其他高级操作了。
# import pandas
#
# users = pandas.read_csv(r".\demo.csv", encoding="utf-8")
# print(users)
# print(users.nunique())
# print(users["id"].unique())
# print(users["id"].size)

# Pandas是一个拥有很多特性的大型函数库，我在这里不可能介绍完。
# 但是只要你需要去分析大型数据集合、对数据分组、计算各种统计量或其他类似任务的话，这个函数库真的值得你去看一看。
