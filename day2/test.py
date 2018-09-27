# 函数
# 复用--同样的代码不用写第二遍
# 实现同一个功能的代码，写到一起，起一个函数名字，其他地方要使用这个功能，直接调用函数
# def 函数名(参数--0到多个):
#     函数代码块
#     [return 返回值]

# 函数定义
def hello():
    """hello function
        print("hello world")
        :return None
    """
    print("hello world")


# 函数必须要调用才会执行,函数定义必须要在函数调用之前
var = hello()


# 没有return语句，没有返回值，返回None
def hello1():
    """hello function
        print("hello world")
        :return None
    """
    return "hello world"


var = hello1()
print(var)


# var是返回值"hello world"
# print，内存中没有变量，
# return，返回值可以赋给一个变量，保存在内存中，需要的时候可以再次取出进行计算

# 返回值是一个变量
def f():
    return 1, 2


res = f()
print(res, type(res))


# 参数,函数定义时，括号中参数叫形参
def add(x, y=0):
    return x + y


# 调用函数的时候，参数叫实参
print(add(x=1))


