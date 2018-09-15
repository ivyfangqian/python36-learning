# 在程序运行过程中，总会遇到各种各样的错误。
# 有的错误是程序编写有问题造成的，比如本来应该输出整数结果输出了字符串，这种错误我们通常称之为bug，bug是必须修复的。
# 有的错误是用户输入造成的，比如让用户输入email地址，结果得到一个空字符串，这种错误可以通过检查用户输入来做相应的处理。
# 还有一类错误是完全无法在程序运行过程中预测的，比如写入文件的时候，磁盘满了，写不进去了，或者从网络抓取数据，网络突然断掉了。
# 这类错误也称为异常，在程序中通常是必须处理的，否则，程序会因为各种问题终止并退出。
# Python内置了一套异常处理机制，来帮助我们进行错误处理。

# Exception
# python标准异常：
# http://blog.csdn.net/wmj2004/article/details/53215939

# ImportError:导入模块错误
# import A

# IndexError:索引超出范围
# list1 = [1,2,3]
# print(list1[3])

# KeyError:字典中不存在的键
# dict1 = {'name':'ivy','age':20,'gender':'female'}
# print(dict1['height'])

# NameError：访问没有定义的变量
# print(a)

# IndentationError:缩进错误,缺少缩进或者是多余不必要的缩进

# 多余的缩进
# print "abc"

# 缺少缩进
# if 1==1:
# print('aaa')

# 同一个代码块中，缩进不一致
# if 1==1:
#     print('aaa')
#      print("bbb")

# SyntaxError:语法错误
# list2 = [1,2,3,4
# dict1 = {name:"xiaoming"}
# name = xiaoming

# TypeError:不同类型间的无效操作
# print(1 + '1')

# ZeroDivisionError:除数为0
# print(5/0)

# 无法预知的调用错误
def summ(a, b):
    print(a + b)


# print(summ(1, 2) + 2)

# 调试时我们关心
# 	什么类型的错误？  分类
# 	在哪儿出错的？    记录并显示堆栈信息
# 	为什么出错？      显示原因
#
# 	抛出的异常也是对象
# 		异常的分类
# 			系统定义的异常
# 				BaseException 所有异常的基类
# 					Exception 常规错误的基类
# 						StandardError 所有的内建标准异常的基类
# 							ImportError  导入模块错误
# 							ArithmeticError 所有数值计算错误的基类
# 								FloatingPointError 浮点计算错误
# 							AssertionError  断言语句失败
# 							AttributeError  对象没有这个属性
# 						Warning 警告的基类

# 异常处理
#
#     捕获 try except finally
#
#         格式：
#             try:
#                 可能会发生错误的语句块
#             except:
#                 发生错误后跳转到该语句块执行
#             else:
#                 当没有异常时，执行这块代码
#             finally:
#                 不管用没有发生错误，都会跳转到此处
try:
    print(5 / 0)
    print("try")
except:
    print("except")

print("正常执行代码")

# except：
#     0.不写异常代表捕获一些类型的错误
#     1.可以一次捕捉多个异常 (exception1, exception2)
#     2.多个except：
#         不要求从小到大捕捉
#     3.可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
#     4.e代表当前异常的实例 print可以显示错误信息  , e  or as e
#     5.如果想要输出详细堆栈信息，使用import traceback traceback.print_exc()
import traceback

try:
    print(a)
    print(5 / 0)
    print("try")
except ZeroDivisionError as e:
    print("zero except")
    print(e)
except (NameError, TypeError):
    print("multi error")
    print(traceback.print_exc())
else:
    print("else")
finally:
    print("finally")

print("异常后代码")
# 执行顺序：
#             当我们认为某些代码可能会出错时，就可以用try来运行这段代码
#             如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块
#             执行完except后，如果有finally语句块，则执行finally语句块
#             try except 语句块可以相互嵌套

# 练习：
#     1.从开发的代码库中得到一组数据，表示每个文件的代码变更情况
#       {'login.py': 'a 8 d 2 u 3', 'order.py': 'a 15 d 0 u 34', 'info.py': 'a 1 d 20 u 5'}
#       其中 a表示新增行数，d表示删除行数，u表示修改行数。login.py的变更行数为13
#       要求：统计出每个文件的变更行数
data = {'login.py': 'a 8 d 2 u 3', 'order.py': 'a 15 d 0 u 34', 'info.py': 'a 1 d 20 u 5'}

# 方法一：
for k, v in data.items():
    update_list = v.split()
    summ = 0
    for i in update_list:
        if i.isdigit():
            summ += int(i)
    print(k, "变更行数：", summ)

# 方法二：
for k, v in data.items():
    update_list = v.split()
    summ = 0
    for i in update_list:
        try:
            summ += int(i)
        except:
            pass
    print(k, "变更行数：", summ)

# 2.优化练习
#         接受用户输入的一个字符串，如果是正整数就判断是否能同时被3和7整除
# 方法一
num = input("请输入一个正整数：")
if num.isdigit():
    num = int(num)
    if num > 0:
        if num % 3 == 0 and num % 7 == 0:
            print("%d可以被3和7整除" % num)
        else:
            print("%d不可以被3和7整除" % num)
    else:
        print("非正整数")
else:
    print("非数字格式")

# 方法二：
num = input("请输入一个正整数：")
try:
    num = int(num)
    if num > 0:
        if num % 3 == 0 and num % 7 == 0:
            print("%d可以被3和7整除" % num)
        else:
            print("%d不可以被3和7整除" % num)
    else:
        print("非正整数")
except ValueError:
    print("非数字格式")


# 抛出
#     如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
#     raise 异常类名 (错误信息)
#
#     自定义异常
#         创建类，继承相应系统异常即可
#             选择性重写 __init__ 和  __str__

# raise TypeError("抛出新异常")

def summ(a, b):
    if a == 0 or b == 0:
        try:
            raise BaseException("a，b不能为0")
        except:
            return None
    else:
        return a + b


# 练习：
# 1.
# 编写一个计算减法的方法，当第一个数小于第二个数时，抛出“被减数不能小于减数
# "的异常
def sub(a, b):
    if a < b:
        raise ArithmeticError("被减数不能小于减数")
    else:
        return a - b


# 2.
# 编写一个计算加法的方法，接收键盘输入的两个数字，进行加法运算，当输入的有非数字时，通过异常处理机制使程序正常运行(返回0)
def summary():
    num1 = input("第一个数：")
    num2 = input("第二个数：")
    res = 0
    try:
        res = int(num1) + int(num2)
    except:
        pass
    return res

# 作业：3.
# 创建一个用户注册服务（server），其中有一个register方法。当用户名小于6位时，抛出自定义异常
# 系统异常NameError的子类UserNameError，显示错误信息：用户名不能小于6位


