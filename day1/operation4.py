# 算术运算符：+ ，- ，*，/，% 取余，** 幂，// 取整除
# 比较运算符 ：==，!=<,>,<=,>=
# 赋值运算符 ：=，+=，-=，*=，/=,%=,**=,//=
# 位运算符：&，|，^,~,<<,>>
# 逻辑运算符：and，or，not
# 标识运算符：is，is not
# 成员运算符 in ，not in

# 算术运算符中需要注意除法的结果跟数字的类型相关
# python2.x中，5/2 -->2 ,只取得整数部分5.0/2-->2.5
# python3.x中，5/2-->2.5
a = 5 / 2
print(a)

print(5.0 / 2.0)
print(5 / 2.0)
print(5.0 / 2)

# %为取模或者取余数操作
b = 5 % 2
print(b)

# ** 取幂
c = 2 ** 8
print(c)

# 取整除/地板除
d = 5 // 2
print(d)

print(5.0 // 2.0)
print(-10.0 // 3.0)

# 比较运算符 ：==比较的是两个变量的值是否相等
list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [1, 2, 3]
print(list1 == list2)
print(list1 == list3)

# python2.x,不等可以有两种写法，!=,<>推荐使用第一种
# python3.x中已经将<>移除，只有!=可以使用
print(list1 != list2)

print(list1[0] < list2[0])
print(list1[0] <= list2[0])
print(list1[0] > list2[0])
print(list1[0] >= list2[0])

# 赋值运算符 ：=，+=，-=，*=，/=，%=,**=,//=
# python中没有++，--
anInt = 1
anInt = anInt + 1
print(anInt)

anInt += 1
print(anInt)

anInt **= 2
print(anInt)

# 逻辑运算符：and，or，not，逻辑运算符两边是布尔值
t = 2 > 1
f = 3 < 2

print(t and f)
print(t or f)
print(not t)

# 逻辑短路
# java中逻辑短路&& ||
# python中 and or就是逻辑短语运算符
# 只要a为false，b与c就不会再执行了
# if a and b and c:
#     xxxx
# 只要a为true，b与c就不会再执行了
# if a or b or c:
#     xxxx

# 练习：写出下面程序的执行结果
def a():
    print("A")
    return 0
def b():
    print("B")
def c():
    print("C")
    return []
def d():
    print("D")
    return False

if a() or b() or c() or d():
    print("OK")

if a() and b() and c() and d():
    print("OK")

# 标识运算符：is，is not,比较的是变量的地址
list1 = list3 = [1, 2, 3]
list2 = [2, 3, 4]

print(list1 == list2)
print(list1 == list3)

print(list1 is list2)
print(list1 is list3)

print(id(list1))
print(id(list2))
print(id(list3))

# 成员运算符 in ，not in
isInList = 1 in list1
print(isInList)
print(5 not in list1)

# 运算符的优先级
# **	幂（指数）
# ~ + -	补码，一元加号和减号（方法名的最后两个+@和 - @）
# * / % //	乘，除，取模和地板除
# + -	加法和减法
# >> <<	左，右按位转移
# &	按位“与”
# ^ |	按位异或`'和`定期'或'
# <= < > >=	比较运算符
# <> == !=	等式运算符
# = %= /= //= -= += *= **=	赋值运算符
# is is not	运算符标识
# in not in	成员运算符
# not or and	逻辑运算符
# 先乘除后加减，有括号的时候先计算括号中的运算

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("(a + b) * c / d =", e)

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("((a + b) * c) / d = ", e)

e = (a + b) * (c / d)  # (30) * (15/5)
print("(a + b) * (c / d) = ", e)

e = a + (b * c) / d  # 20 + (150/5)
print("a + (b * c) / d = ", e)
