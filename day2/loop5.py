# 当我们需要重复执行某一代码块的时候，会用到循环操作
# 循环语句包含 while ，for
# while 条件表达式:
#   条件表达式为真时执行代码
# 例如：输出1-10
i = 0
while i <= 10:
    print(i)
    i += 1

# range(start,end,step),step为空默认为1
# 从0到10(不包含10)
print(range(10))
# 从1到10(不包含10)
print(range(1, 10))
# 从1到10，间隔2(不包含10)
print(range(1, 10, 2))

# 举例：求1-10的所有数字的和
num = 0
sum = 0
while num <= 10:
    sum = sum + num
    num += 1
print('sum =' + sum.__str__())

# 无限循环/死循环
# i=0
# while True:
#     print i
#     i+=1

# python提供给我们另一个最强大的循环机制就是for循环语句，它可以遍历序列成员（字符串、数组、元组）
# 迭代序列有三种方法
# 第一种：通过序列项迭代，类似于Java中的for each
# 语法：for  iter_var in iterable:
#              要循环执行的代码块
# 例如：我们要遍历一个字符串中的所有字符
aStr = 'rabbit'
for eachLetter in aStr:
    print(eachLetter)

# 遍历列表中的每一个元素
nameList = ['xiaoming', 'xiaohong', 'xiaofang', 'xiaogang']
for eachName in nameList:
    print(eachName)

# 第二种，通过序列的索引来遍历序列
# 通过序列的索引,nameIndex从0开始，0=<nameIndex<3
for nameIndex in range(len(nameList)):
    print(nameIndex, nameList[nameIndex])

# 第三种，同时使用项和索引迭代
for j, eachName in enumerate(nameList):
    print(j, eachName)

# 举例：求1-10的所有数字的和
summary = 0
for num in range(1, 11):
    summary = summary + num
print('sum is %d' % (summary))

# 练习:分别使用while与for循环输出1-100之间的所有偶数

# python循环中使用else语句
# 其他语言中，只在分支语句中才能见到else，
# python则不然，循环语句中使用else，代表在循环正常结束后，执行else中的代码块，
# break语句也会跳过else
summary = 0
for num in range(1, 11):
    summary = summary + num
else:
    print('sum is %d' % (summary))

# 强制结束循环，遇到break结束循环的情况时，不执行else
# import time
# for num in range(30):
#     print num
#     time.sleep(1)
# else:
#     print 'bye'


while True:
    print(i)
    if i >= 100:
        break
    i += 1
else:
    print('break跳出循环')

# python中使用pass，pass是占位语句，什么都不做，只是为了保证程序结构的完整性
for num in range(1, 11):
    print(num)
    if num >= 8:
        pass
    print('=' * 20)

# break与continue
# break，结束循环
# continue，跳出本次循环

for x in range(10):
    if x > 5:
        break
    print(x)

for x in range(10):
    if x < 5:
        continue
    print(x)

# 0.输入n, 计算1到n的阶乘之和
n = input("请输入一个正整数：")
res = 1
# 判断n是否为正整数
if n.isdigit():
    n = int(n)
    # 求1-n阶乘
    for i in range(1, n + 1):
        res *= i
else:
    print("对不起，您输入的不是正整数")

print(res)

# 1.分别使用while与for循环输出1-100之间的所有偶数
# 提示:# for i in range()
# 方法一:
i = 1
while i < 101:
    if i % 2 == 0:
        print(i)
    i += 1

# 方法二：
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# 方法三：
for i in range(2, 101, 2):
    print(i)

# 2.找100以内最大平方数
#     提示：from math import sqrt  sqrt(n)
from math import sqrt

for i in range(99, 0, -1):
    root = sqrt(i)
    if root == int(root):
        print(i)
        break

# 3.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
string = "To be, or not to be: that is the question:\
            Whether 'tis nobler in the mind to suffer"
alphas = 0
digits = 0
spaces = 0
others = 0

# 如果字符串不为空才进行统计
if string:
    for letter in string:
        if letter.isalpha():
            alphas += 1
        elif letter.isdigit():
            digits += 1
        elif letter.isspace():
            spaces += 1
        else:
            others += 1
else:
    print("string不能为空")
print("字符串中英文字母个数%d，数字个数%d，空格个数%d，其它字符的个数%d" % (alphas, digits, spaces, others))

# 4.一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
# 方法一：
number = "12321"
for i in range(len(number) // 2):
    if number[i] != number[-i - 1]:
        print("不是回文数")
        break
else:
    print("是回文数")

# 方法二：
if number == number[::-1]:
    print("是回文数")
else:
    print("不是回文数")

# 方法三：

number = 12321
num = number
reverse_num = 0
while number != 0:
    reverse_num = reverse_num * 10 + number % 10
    number //= 10
if num == reverse_num:
    print("是回文数")
else:
    print("不是回文数")

# 5.打印出100-999中所有的"水仙花数"，所谓"水仙花数"是指一
#   个三位数，其各位数字立方和等于该数本身。例如：
#   153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方
# 6.输出9*9口诀
# 7.输出100之内的素数总个数，所谓"素数"是指除了1和它本身以外，不能被任何整数整除的数，例如17
# 8.算法：python的冒泡排序

# 循环嵌套，Python 语言允许在一个循环体里面嵌入另一个循环体。
# 举例：对列表[50,20,30,10]进行冒泡排序,按照升序排列
# 冒泡排序：从前往后将相邻的两个数进行比较，将较小的数放在前面，较大的数放在后面
# 第一轮
# 20 50 30 10
# 20 30 50 10
# 20 30 10 50
# 第二轮
# 20 30 10 50
# 20 10 30 50
# 第三轮
# 10 20 30 50
# 冒泡排序原理: 每一轮只能将一个数归位, 如果有n个数进行排序,只需将n-1个数归位,
# 也就是说要进行n-1轮操作(已经归位的数不用再比较)
aList = [50, 20, 30, 10, 5]

for i in range(1, len(aList)):  # 比较几轮,第一轮：1，第二轮：2，第三轮：3
    for j in range(0, len(aList) - i):  # 定义比较的索引,第一轮，0-1,1-2,2-3，第二轮：0-1,1-2，第三轮：0-1
        if aList[j] > aList[j + 1]:
            aList[j], aList[j + 1] = aList[j + 1], aList[j]
        print(aList)


        # 作业：
        # 		1.某市的出租车计费标准为：3公里以内10元，3公里以后每0.5公里加收1元；每等待2.
        # 		  5分钟加收1元；超过15公里的加收原价的50%为空驶费。
        # 		  要求编写程序，对于任意给定的里程数（单位：公里）和等待时间（单位：秒）计算出应付车费
        # 		2.一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程找出1000以内的所有完数
        # 	   *3.用python实现选择排序
        # 			算法如下：[49, 38, 27, 45, 13]
        # 			第一趟[13, 49, 38, 27, 45]
        # 			第二趟[13, 27, 49, 38, 45]
        # 			第三趟[13, 27, 38, 49, 45]
        # 			第四趟[13, 27, 38, 45, 49]
