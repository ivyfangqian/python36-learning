#  1、编写一组数据，记录组内每个人的语文成绩、数学成绩、英语成绩
#  	data = {
#  	     'WeiYingLuo': [60, 68, 45],
#  	     'FuCha': [10, 28, 5],
#  	     'FuHeng': [44, 86, 73],
#  	     'XianFei': [99, 95, 95],
#  	     'ErQing': [98, 65, 100],
#  	     'HongZhou': [77, 97, 65]
#   	}
#  	a.找到平均分不足60分的人
#  	b.找出各科的最高分
#  	c.算出各科的平均分，再找出各科的学霸
#   	}

# data = {
#     'WeiYingLuo': [60, 68, 45],
#     'FuCha': [10, 28, 5],
#     'FuHeng': [44, 86, 73],
#     'XianFei': [99, 95, 95],
#     'ErQing': [98, 65, 100],
#     'HongZhou': [77, 97, 65]
# }
#
# chs = []
# maths = []
# ens = []
# for v in data.values():
#     chs.append(v[0])
#     maths.append(v[1])
#     ens.append(v[-1])
#
#


#
#
# print("语文平均分%.2f" % avg(chs))
# print("数学平均分%.2f" % avg(maths))
# print("英语平均分%.2f" % avg(ens))
#
#
# # 再找出各科的学霸
# # sorted(iter, key ,reverse)
# # iter 可迭代序列，key 排序规则 ，从小往大排序（默认）,reverse=True从大往小排
# def ch(item):
#     return item[1][0]
#
#
# # 匿名函数
# # lambda 参数:函数返回值
# lambda item: item[1][0]
#
# max_yuwen = sorted(data.items(), key=lambda item: item[1][0], reverse=True)[0][0]
# print("语文最高分", max_yuwen)
#
# max_shuxue = sorted(data.items(), key=lambda item: item[1][1], reverse=True)[0][0]
# print("数学最高分", max_shuxue)
#
# max_yingyu = sorted(data.items(), key=lambda item: item[1][2], reverse=True)[0][0]
# print("英语最高分", max_yingyu)


# 作业：
# 	1.编写一组数据，记录组内每个人的语文成绩、数学成绩、英语成绩
# 		data = {
#             '魏璎珞':{'语文':60, '数学':68, '英语':45},
#             '富察':{'语文':10, '数学':28, '英语':5},
#             '傅恒':{'语文':44, '数学':86, '英语':73},
#             '娴妃':{'语文':99, '数学':95, '英语':95},
#             '尔晴':{'语文':98, '数学':65, '英语':100},
#             '弘昼':{'语文':77, '数学':97, '英语':65}
#        	}
# 		a.找到平均分不足60分的人，
# 		b.找出各科的最高分,平均分
# 		c.找出各科的学霸
data = {
    '魏璎珞': {'语文': 60, '数学': 68, '英语': 45},
    '富察': {'语文': 10, '数学': 28, '英语': 5},
    '傅恒': {'语文': 44, '数学': 86, '英语': 73},
    '娴妃': {'语文': 99, '数学': 95, '英语': 95},
    '尔晴': {'语文': 98, '数学': 65, '英语': 100},
    '弘昼': {'语文': 77, '数学': 97, '英语': 65}
}

for k, v in data.items():
    avg = sum(v.values()) / len(v)
    if avg < 60:
        print(k)


# b.找出各科的最高分,平均分
def avg(scores):
    if scores is None or scores == []:
        return 0

    return sum(scores) / len(scores)


chs = []
maths = []
ens = []
for v in data.values():
    chs.append(v["语文"])
    maths.append(v["数学"])
    ens.append(v["英语"])

print("语文最高分%d,数学最高分%d，英语最高分%d" % (max(chs), max(maths), max(ens)))
avg_ch = avg(chs)
avg_math = avg(maths)
avg_en = avg(ens)
print("语文平均分%.2f,数学平均分%.2f，英语平均分%.2f" % (avg_ch, avg_math, avg_en))

# c.找出各科的学霸
# 语文学霸
print(sorted(data.items(), key=lambda item: item[1]["语文"], reverse=True)[0][0])

# 2.统计一篇英文文章每个单词的出现频率，并返回出现频率最高的前5个单词及其出现次数(字典形式)
# A small sample of texts from Project Gutenberg appears in the NLTK corpus collection.
# However, you may be interested in analyzing other texts from Project Gutenberg.
# You can browse the catalog of 25,000 free online books at http://www.gutenberg.org/catalog/,
# and obtain a URL to an ASCII text file. Although 90% of the texts in Project Gutenberg are in English,
# it includes material in over 50 other languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian

string = """A small sample of texts from Project Gutenberg appears in the NLTK corpus collection.
However, you may be interested in analyzing other texts from Project Gutenberg.
You can browse the catalog of 25,000 free online books at http://www.gutenberg.org/catalog/,
and obtain a URL to an ASCII text file. Although 90% of the texts in Project Gutenberg are in English,
it includes material in over 50 other languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian"""
# 先把所有单词转成大写/小写
# 切割 -- 空格
str_list = string.lower().split()
print(str_list)
# 统计 ， 某些单词后面跟了，或者. ，需要特殊处理
counts = {}
for i in str_list:
    if i.endswith(",") or i.endswith("."):
        i = i[:-1]
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
print("统计结果：", counts)

# 并返回出现频率最高的前5个单词及其出现次数
top5 = sorted(counts.items(), key=lambda item: item[-1], reverse=True)[:5]
print(top5)

# 3.给定一个字符串，例如abcabcd，请你求得到该字符串中所有的长度大于等于2的子串，并统计每个字串出现的次数
string = "abcabcd"

if len(string) < 2:
    print("字符串不包含子串")
else:
    subs = {}
    n = len(string)
    for i in range(0, n - 1):
        for j in range(i + 2, n):
            sub_string = string[i:j]
            if sub_string in subs:
                subs[sub_string] += 1
            else:
                subs[sub_string] = 1
print(subs)

# 请你按照从大到小排序
print(sorted(subs.items(), key=lambda item: item[-1], reverse=True))
