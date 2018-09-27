import re

# 正则表达式 regular expression
# 正则表达式是一种用来匹配字符串的强有力的武器。
# 它的设计思想是用一种描述性的语言来给字符串定义一个规则，
# 凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。
# 正则表通常被用来检索、替换那些符合某个模式(规则)的文本。
# python中用re模块实现了正则的所有功能

# 定义一个字符串作为正则表达式
reg_str = r'123'

# 使用re.findall()来根据匹配规则查找对应的字符串，
# 返回一个符合规则的列表
print(re.findall(reg_str, '12345678901234456'))

# 当然，正则字符串也可以使用如下表示
re_string = r"[0-9]{3,5}"
string = "12345fsgregh3trh234gggrg34t5654"

res = re.findall(re_string, string)
print(res)

# 如果我们就是要取出一个.，怎么办呢
# . * + ^ $ ？ \ | [] {} 都称之为元字符，需要匹配查找元字符时，需要添加\
r = r'huicewang\.'
print(re.findall(r, 'http://www.huicewang.com'))

# ^代表以什么开头
r = r'^123'
print(re.findall(r, '12334455677123'))

# $代表以什么结尾
r = r'123$'
print(re.findall(r, '12345123'))

# .代表任意字符
r = r'1.2'
print(re.findall(r, '123451321432'))

# [0-9]代表任意数字
r = r'a[0-9]b'
print(re.findall(r, 'a9b,afb,a23b,ae3b'))

# [a-z]任意小写字母，[A-Z]任意大写字母
reg_str = r'[a-z][A-Z][0-9]'
print(re.findall(reg_str, 'aQ1 rE5 ear e6 E7r'))

# [^]不在区间范围内的值
r = r'a[^0-9]b'
print(re.findall(r, 'a9b,afb,a23b,ae3b'))

# \d代表数字
reg_str = r'1[\d]{10}'
print(re.findall(reg_str, '13412345678,qwertyui'))

# \D非数字
reg_str = r'a\Dz'
print(re.findall(reg_str, 'awz a1z'))

# \s空白字符
reg_str = r'a\sz'
print(re.findall(reg_str, 'a z a1z'))

# \S非空白字符
reg_str = r'a\Sz'
print(re.findall(reg_str, 'a z a1z'))

# \w 单词字符[a-zA-Z0-9]
reg_str = '\w\d\w'
print(re.findall(reg_str, 'hello a1b a b'))

# \W 非单词字符
reg_str = 'a\Wb'
print(re.findall(reg_str, 'hello a1b a b a+b'))

# {重复次数},限定前一个字符的重复次数
reg_str = '1[\d]{10}'
print(re.findall(reg_str, '13412345678,qwertyui'))

# {a,b}前一个字符出现重复次数的一个范围
reg_str = '[\d]{3,8}'
print(re.findall(reg_str, '13412345678,12345,12,sdfgh'))

# *匹配大于等于0次
reg_str = '1[\d]*'
print(re.findall(reg_str, '13412345678,qwertyui 1'))

reg_str = '1[a]*'
print(re.findall(reg_str, '13412345678,qwertyui 1aa 1 1a'))

# +匹配大于等于1次
reg_str = '1[a]+'
print(re.findall(reg_str, '13412345678,qwertyui 1aa 1 1a'))

# ?匹配0或者1次
reg_str = '1[a]?'
print(re.findall(reg_str, '13412345678,qwertyui 1aa 1 1a'))

# 北京市电话号码
tel_reg = '^010-?[1-9]\d{7}$'
print(re.findall(tel_reg, '010-82456356'))
print(re.findall(tel_reg, '01054236987'))
print(re.findall(tel_reg, '010-07894561'))
print(re.findall(tel_reg, '01012345'))

# 校验手机号
mobile_phone = '^1[3578][0-9][0-9]{8}'
print(re.findall(mobile_phone, '13412345678'))
print(re.findall(mobile_phone, '15098765432'))
print(re.findall(mobile_phone, '17300000000'))
print(re.findall(mobile_phone, '18736589741'))
print(re.findall(mobile_phone, '10736589741'))

# ()分组
r = '(\.com\.cn|\.com|\.cn)'
print(re.findall(r, 'test@126.com.cn test@126.com test@qq.cn'))

# 练习：匹配邮箱
email_reg = '(\w+@\w+[\.\w+]+)'
print(re.findall(email_reg, 'test@126.com test@qq.com test@sina.com.cn'))

email_reg = '(\w+@(\w+[\.\w+]+))'
print(re.findall(email_reg, 'test@126.com test@qq.com test@sina.com.cn'))

# compile()编译后可以提高执行速度
# findall返回匹配列表
re_com = re.compile(r'1[3578][0-9][0-9]{8}')
print(re_com.findall('134aff12345678 13487654321 13512345678'))

# match匹配正则的开头内容，返回第一个符合的字符串
# 如果开头不符合正则表达式条件，就返回None
print(re_com.match('13412345678 13487654321 13512345678').group())

# search匹配全文，返回第一个符合的字符串，不一定是开头
print(re_com.search('134123ssd45678 13487654321 13512345678').group())

# sub函数可以根据正则表达式对字符串进行替换，返回替换后的字符串
print(re.sub(r"123", "456", "123 123 asd", 1))

# subn函数可以根据正则表达式对字符串进行替换，
# 返回一个元组，元组包含两项，第一项是替换后的字符串，第二项是替换的次数
print(re.subn(r"123", "456", "123 123 asd"))

# split函数可以根据指定的正则表达式对字符串进行切割，返回一个列表
print(re.split("\s+", "123  gdg  893 grr"))
