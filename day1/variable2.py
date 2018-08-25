# 什么是变量？a就是一个变量
a = 2

# 请回忆初中数学所学的代数基础知识：
# 设正方形为a，则正方形的面积为a x a。把边长a看做一个变量，我们就可以根据a的值计算正方形的面积，比如：
# 若a=2，则面积为a x a = 2 x 2 = 4；
# 若a=3，则面积为a x a = 3.x 3 = 9。
# 在计算机程序中，变量是计算机内存中的一块区域，存储程序规定范围内的值，值可以改变，可以认为变量就是给数据起名。
# 变量不仅可以为整数或浮点数，还可以是字符串，因此，name作为一个变量就是一个字符串。
name = 'ivy'
print(name)

# 变量命名规则
# 1、变量名由字母、数字、下划线组成
# 2、不能以数字开头
# 3、不可以使用关键字
a1 = 1
a_1 = 2
_a1 = 3
# 1aaaa =1

# 哪些是关键字？
import keyword

print(keyword.kwlist)
# 判断一个字符串是不是关键字
print(keyword.iskeyword('int'))
print(keyword.iskeyword('while'))

# 变量赋值
# 每个变量在使用前都必须要赋值，赋值后变量才会被创建
# 用赋值运算符（=）来进行变量的赋值，等号左边是变量名，右边是变量的值。
name = "tom"
print(name)

# c与java中，允许定义变量，但是不进行赋值，是强类型语言
# python中只有赋值时，才能确定变量的值与类型，是弱类型语言，python中所有的数据类型都是引用数据类型
# 如果使用一个没有赋值的变量，会报NameError:name 'xxx' is not defined
# age
# print(age)

# python内置函数id()，可以获取变量的内存地址
# python中所有的数据类型为引用数据类型变量对应的内存格子中存储的是一个内存地址，
# 内存地址对应的内存中存储的才是对应数据
print(id(name))
username = "tom"
print(id(username))

# 可以多个变量同时赋值，但是可读性不好，不推荐这么做
a = b = c = 1
print(a, b, c)

a, b, c = 1, 2, 3
print(a, b, c)

# 交换两个变量的值
# c与java中，必须通过一个中间变量，才能进行变量的交换，但是python就很简单，不需要我们设定中间变量
a, b = b, a
print(a, b)
