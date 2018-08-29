# 我们的第一个程序
print('Hello World!')

# python2.x默认字符集为ASCII，打印中文需要设置coding为utf-8
# python3.x默认字符集为UTF-8
import sys

print(sys.getdefaultencoding())

print('你好!')

# 'print 可以同时打印多个字符串，两个字符串之间以逗号隔开
print('小明，', '你好!')

# python单行注释为#，
# 多行注释也推荐使用#
# print 'Hello World!'
# print 'Hello World!'
# print 'Hello World!'

# 多行注释用三个单引号 ''' 或者三个双引号 """ 将注释括起来\
'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号
这是多行注释，用三个单引号
'''

"""
这是多行注释，用三个双引号
这是多行注释，用三个双引号
这是多行注释，用三个双引号
"""


# ''' 或者三个双引号 """ 可以作为类/函数中作为说明文档
class A(object):
    '''class A desc'''
    pass


print(A().__doc__)


def hello():
    """function hello desc"""
    pass


print(hello.__doc__)

# Python允许用'''...'''，"""..."""的格式表示多行内容，并且保留内容格式
print('''单引号，第一行
单引号，第二行''')

print("""双引号，第一行
双引号，第二行""")

# 输出数字
print(1)

# 输出运算结果
print(1 + 2)

# 输出组合结果,需要注意的是，这里1+2=是字符串
print('1+2=', 1 + 2)

# 等待用户输入input(),input()会将输入内容全部转换为字符串

# name = input("请输入你的名字：")
# print name,'你好！'
#
# result = input("请输入1+2的结果：")
# print result

# 为了让程序员有一个良好的代码习惯，python强制要求用缩进来标识一个函数或者类的范围
# java中代码块一般使用{}包裹，不需要进行缩进
# python中代码块必须要进行缩进，同一个代码块的代码缩进数量要一致
# notepad++ ：一个tab=4个空格
# pycharm：一个tab=8个空格
# windows下tab的空格数与linux下tab的空格数不一致
# 解决方法：一般缩进为4个空格，pycharm在settings--》code style --》python  --》use tab character 取消勾选
# 输出一个数字的绝对值
a = 1
if a >= 0:
    print(a)
else:
    print(-a)

