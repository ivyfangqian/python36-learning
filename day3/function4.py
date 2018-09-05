# 函数就是将一些语句集中在一起的一个部件，
# 目的是减少我们同一段代码的复制粘贴，需要的时候以函数调用来代替，实现代码的复用
# 函数定义语法：
# def 函数名(0个或多个参数):
#     函数内要执行的代码
#     return 返回值

# 函数可以只定义函数名，没有参数，也没有返回值
# 函数的命名规则：一个单词直接小写
# 多个单词，每个单词小写，以下划线分隔
def hello():
    print('Hello World!')


# 函数的调用
res = hello()
print(type(res))


# 文档化说明
# 函数首行加 ''  或 ''' '''
#     使用函数名.__doc__属性 可以查看函数文档
#     help(函数名)

def desc():
    """desc function"""
    pass


print(desc.__doc__)
help(desc)

# callable(函数名) --判断函数是否可以被调用
# 	debug的时候经常报错，xx is not callable --说明你应该在报错的地方给一个函数，结果你给的xxx不能当函数用
print(callable(desc))


# a = 0
# sorted([9, 4, 5, 6], key=a)

# 函数有返回值
def get_list():
    return [1, 2, 3, 4]


aList = get_list()
print(type(aList), aList)


# 函数没有返回值，也就是没有return语句，实际返回None
def get_list1():
    print([1, 2, 3, 4])


aList = get_list1()
print(type(aList), aList)


# 函数可以有多个return语句，遇到return语句，跳出函数
def get_smaller(x, y):
    if x < y:
        return x
        print('x is smaller')
    else:
        return y


smaller = get_smaller(1, 2)
print(smaller)


# return 1,2  实际是返回一个元组，返回值只有一个
def gen():
    return 1, 2


print(gen())


# 函数有参数
# 参数：形参和实参,形参和实参要一一对应
def add(x, y):
    return x + y


sum = add(1, 2)
print(sum)


# 参数传递不正确的情况
# sum = add()
# sum = add(1,2,3)

# 默认参数
# 为了提高程序的健壮性，
# 如果我们想在x，y值不传的时候，也给出一个默认的结果，就需要用到默认参数
# 参数有默认值之后，可以根据需要传递实参
def add(x=2, y=3):
    return x + y


sum = add()
print(sum)

sum = add(1)
print(sum)

sum = add(1, 2)
print(sum)


# *顺序
# 带默认值的参数往后放，后面不能再有必填参数
# def check_in(username,gender,age=20,id):
#     pass


# 函数的参数可以是任意类型
def print_item(x):
    print(x)


print_item(1)
print_item(1.0)
print_item('string')
print_item([1, 2, 3])
print_item((1, 2, 3))


# 函数的参数可以是不同类型
def print_userinfo(name, age):
    print('username is %s and age is  %d' % (name, age))


print_userinfo('xiaoming', 18)
print_userinfo(age=18, name='xiaoming')


# 传递参数过多,*param_tuple,可以将多传入的参数放到元组中
def print_userinfo1(name, age, *param_tuple):
    print('username is %s and age is  %d' % (name, age))
    print(param_tuple)


print_userinfo1('xiaoming', 18, 170, 130)

# 可以将要传递的参数放在tuple中
aTuple = ('xiaoming', 18)
print_userinfo(*aTuple)


# 传递参数过多,**param_dict,可以将多传入的参数放到字典中
def print_userinfo2(name, age=18, **param_dict):
    print('username is %s and age is  %d' % (name, age))
    print(param_dict)


print_userinfo2(name="zhangsan", age=20, height=170, weight=130)
# 要传递的参数放在字典中
aDict = {'age': 20, 'name': 'xiaoming'}
print_userinfo2(**aDict)


# key不对应的情况
# aDict = {'height':20,'name':'xiaoming'}
# print_userinfo(**aDict)

# 可变长度的参数
def print_userinfo3(name, age, *tuple_args, **dict_args):
    print('username is %s and age is  %d' % (name, age))
    print(tuple_args)
    print(dict_args)


print_userinfo3('xiaoming', 18)

# 传递参数有冗余时，直接传递会报错，如何解决
# 冗余参数会传递到tuple_args
print_userinfo3('xiaoming', 18, 170)

aTuple = ('xiaoming', 18, 170)
print_userinfo3(*aTuple)

# 冗余参数存放到dict_args
print_userinfo3(name='xiaoming', age=18, height=170)

# 重复传值给name参数
# print_userinfo('xiaoming',18, 170,name = 'xiaohong',height = 170)

# 冗余参数170，'xiaohong'存放到tuple_args,height = 170 存放到dict_args
print_userinfo('xiaoming', 18, 170, 'xiaohong', height=170)


# **参数定义的顺序必须是：必选参数、默认参数、可变参数

# 练习:
# 以下的代码的输出什么? 你将如何修改 extendList 的定义所带来的隐患问题
def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)


# 函数内部可以调用其他函数
def cal(x, y):
    print(x + y)


res = cal(1, 2)


# 如果一个函数在内部调用自身，这个函数叫做递归函数
# 递归函数一般都有两个条件，一个是基本条件，即结束条件
# 另一个是递归条件
# 递归调用的次数过多，会导致栈溢出
# 举例：求一个数n的阶乘
# n的阶乘为n*(n-1)*(n-2)...*1
# n! = n*(n-1)！
# n为1的时候，阶乘为1
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

# 变量的作用域问题
# 根据变量声明的位置的不同，变量存在不同的作用域：全局，局部
# 全局变量，局部变量
# 变量的作用域限制了你在哪个地方可以访问哪个变量
global_var = 'global'


def foo():
    local_var = 'local'
    print(global_var + local_var)


foo()

# foo中可以对所有的变量进行访问，但是函数外只能访问全局变量，无法访问函数的内部变量
# local_var是在函数体中定义的，只能在函数foo中使用
# global_var是在函数体外定义的，可以在脚本的任意一个位置访问
print(global_var)
# print local_var

# x = 'xiaoming'
# def fun():
#     x='xiaohong'
#     print x
# fun()
# print x

# 函数内部也可以定义全局变量
# 使用global关键字
# 注意：必须要先调用函数，函数体中定义的全局变量才能生效
# x = 'xiaoming'
# def fun():
#     x='xiaohong'
#     global global_y
#     global_y = 'xiaofang'
#     print x
# fun()
# print x
# print global_y

# 如何在函数中修改全局变量的值
x = 'xiaoming'


def fun():
    global x
    x = 'xiaohong'
    print(x)


fun()
print(x)


# 匿名函数,lambda
def func(x, y):
    return x + y


func = lambda x, y: x + y

# reduce()函数
list1 = [1, 2, 3]


def add(x, y):
    return x + y


# Guido大大原计划把 lambda, reduce 都干掉。
# 最后只干掉了 reduce
# 首先在python3版本中，直接使用reduce()的话，系统会报错，提示不存在reduce()函数。
# reduce(add, list1)
# 在Python 3里，reduce() 函数已经被从全局名字空间里移除了，它现在被放置在fucntools 模块里
# 使用前需要先引用
from functools import reduce

print(reduce(add, list1))
print(reduce(lambda x, y: x + y, range(1, 101)))
