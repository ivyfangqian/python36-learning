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

data = {
    'WeiYingLuo': [60, 68, 45],
    'FuCha': [10, 28, 5],
    'FuHeng': [44, 86, 73],
    'XianFei': [99, 95, 95],
    'ErQing': [98, 65, 100],
    'HongZhou': [77, 97, 65]
}

# a.找到平均分不足60分的人
for name, scores in data.items():
    avg_score = sum(scores) / len(scores)
    if avg_score < 60:
        print(name, avg_score)

# b.找出各科的最高分
# scores = data.values()
# chinese = sorted(scores, key=lambda item: item[0], reverse=True)[0][0]
# print(chinese)
# math_max = sorted(scores, key=lambda item: item[1], reverse=True)[0][1]
# print(math_max)
# english = sorted(scores, key=lambda item: item[2], reverse=True)[0][2]
# print(english)
chs = []
maths = []
ens = []
for v in data.values():
    chs.append(v[0])
    maths.append(v[1])
    ens.append(v[2])
print("语文最大成绩为%d,数学最大成绩为%d,英语最大成绩为%d" % (max(chs), max(maths), max(ens)))

# c.算出各科的平均分，再找出各科的学霸
avg_ch = sum(chs) / len(data)
avg_math = sum(maths) / len(data)
avg_en = sum(ens) / len(data)

print("语文平均分为%.2f,数学平均分为%.2f,英语平均分为%.2f" % (avg_ch, avg_math, avg_en))

# 找出学霸
best_yuwen = sorted(data.items(), key=lambda item: item[-1][0], reverse=True)[0][0]
best_shuxue = sorted(data.items(), key=lambda item: item[-1][1], reverse=True)[0][0]
best_yingyu = sorted(data.items(), key=lambda item: item[-1][2], reverse=True)[0][0]
print("语文学霸是%s，数学学霸是%s，英语学霸是%s" % (best_yuwen, best_shuxue, best_yingyu))

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
# a.找到平均分不足60分的人，
for k, v in data.items():
    avg = sum(v.values()) / len(v)
    if avg < 60:
        print(k)

# b.找出各科的最高分,平均分
yuwen = []
shuxue = []
yingyu = []
for v in data.values():
    yuwen.append(v["语文"])
    shuxue.append(v["数学"])
    yingyu.append(v["英语"])

print("语文最高分为%d，数学最高分为%d，英语最高分为%d" % (max(yuwen), max(shuxue), max(yingyu)))
print("语文平均分为%.2f，数学平均分为%.2f，英语平均分为%.2f"
      % (sum(yuwen) / len(yuwen), sum(shuxue) / len(shuxue), sum(yingyu) / len(yingyu)))

# c.找出各科的学霸
best_yuwen = sorted(data.items(), key=lambda item: item[-1]["语文"], reverse=True)[0][0]
best_shuxue = sorted(data.items(), key=lambda item: item[-1]["数学"], reverse=True)[0][0]
best_yingyu = sorted(data.items(), key=lambda item: item[-1]["英语"], reverse=True)[0][0]
print("语文学霸是%s，数学学霸是%s，英语学霸是%s" % (best_yuwen, best_shuxue, best_yingyu))

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

counts = {}
str_list = string.lower().split()
print(str_list)
for i in str_list:
    if i.endswith(",") or i.endswith("."):
        i = i[:-1]
    if i in counts and i:
        counts[i] += 1
    else:
        counts[i] = 1
print(counts)

print(sorted(counts.items(), key=lambda item: item[-1], reverse=True)[0:5])

# 3.给定一个字符串，例如abcabcd，请你求得到该字符串中所有的长度大于等于2的子串，并统计每个字串出现的次数
string = "abcabcd"

if len(string) == 0 or len(string) == 1:
    print("字符串长度小于2")

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

# 按照出现的次数从高到低倒叙排序
print(sorted(sub_count.items(), key=lambda item: item[-1], reverse=True))
