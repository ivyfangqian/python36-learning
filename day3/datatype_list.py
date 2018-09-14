# -------------------------------------列表--------------------------------------
# 列表List,Python内置的一种数据类型,
# list是一种有序的集合，可以随时添加和删除其中的元素,是可变类型
# 可以保存任何数据类型--数据项不需要具有相同的类型
aList = [1, 2, 3]
print(aList)
print(type(aList))
print(len(aList))

# 访问数据项：索引和切片
# 使用索引访问指定元素，但是索引不能超出索引范围
print(aList[0])

# 切片取值,Python提供了切片（Slice）操作符，能大大简化这种操作,
# [0:3]==>[0,3),从索引为0开始取值，取到索引为3的值，但不包含3
print(aList[0:3])
print(aList[1:3])
print(aList[0:])
print(aList[:3])
print(aList[0:-1])

# 向列表中插入元素
# append  用于在列表末尾追加新的元素
alist = [1, 2, 3, 4]
alist.append(5)
print(alist)
# extend  在列表末尾一次性追加另一个序列中的多个值
# 两个列表也可以用+来拼接
new_list = [6, 7, 8]
alist.extend(new_list)
print(alist)
# insert(index, obj)		将对象插入到列表指定项
alist.insert(1, 90)
print(alist)
# 批量插入
# list[x:x] = list2 --第x项后插入一个列表，但是要注意区分和索引赋值的区别
user = [1, "张三", 20, 170]
info = [70, "1999-09-10"]
user[2:2] = info
print(user)

# 更新数据项
# 索引赋值
# 	不能超过索引范围
user = [1, "张三", 20, 170]
user[-1] = 175
print(user)

# 分片赋值
# 	可以同时改变一个范围内的数据项
# 	list1[x:y] = list2
user = [1, "张三", 20, 170]
info = [70, "1999-09-10"]
user[2:-1] = info
print(user)

persons = ['张三', '李四', '王五', '赵六']
# 数组中是否含有某个元素
# 使用成员运算符判断
print("张三" in persons)

# L.index(value, [start, [stop]])  用于从列表中找出某个值第一个匹配项的索引位置
print(persons.index('张三'))

# 使用L.__contains__(item)函数
print(persons.__contains__('张三'))

# count计数
print(persons.count('张三'))

# 删除列表元素
# pop     该方法从列表中弹出一个元素，默认是最后一个。并且返回弹出的元素值
# 如果传入索引，则弹出制定索引位置的元素，并且返回弹出元素值
print(persons.pop())
print(persons)
print(persons.pop(-2))
print(persons)

# remove  从列表中移除某个值的第一个匹配项。与pop不同的是，该方法并不返回移除的元素
persons.remove("张三")
# persons.remove(1)
print(persons)

# del从列表中按照索引删除某个元素
del (persons[-1])
print(persons)

# 批量删除
persons = ['张三', '李四', '王五', '赵六']
del persons[1:3]
print(persons)

# 清空列表
persons.clear()
print(persons)

# sort对列表进行排序,排序是按照ASCII码的顺序来排列，Z比a的顺序还要靠前
# L.sort(key=None, reverse=False) -> None
numbers = [10, 50, 20, 80, 30]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# stus中存放了四个学生的学号，姓名及成绩，请按照成绩倒序输出
stus = [[1, "zhangsan", 60], [2, "lisi", 80], [3, "wangwu", 75], [4, "zhaoliu", 90]]
stus.sort(key=lambda item: item[-1], reverse=True)
print(stus)

# 使用L.reverse()对列表进行存储顺序进行反转
persons = ['张三', '李四', '王五', '赵六']
persons.reverse()
print(persons)

# 列表可以使用+和*进行计算
# 两个列表也可以用+来拼接
print([1, 2, 3] + [4, 5, 6])
# 使用*对列表中元素进行乘法
print([1, 2, 3] * 5)

# 对列表进行遍历
user = [1, "小明", 20]
# 列表元素项
for i in user:
    print(user)
# 列表索引
for i in range(len(user)):
    print(i, user[i])
# 列表索引和值
for i, j in enumerate(user):
    print(i, j)

# 列表嵌套：
# 多维列表: [ [1, 2, 3], [4, 5, 6] ]
# zip函数
# 	它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。
# 	若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同
# 练习：用zip函数组合出
# 	((1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000))
ids = [1, 2, 3, 4]
names = ["zhangsan", "lisi", "wangwu"]
salary = [3000, 2500, 20000]
print("---------------------")
print(zip(ids, names, salary))
print(tuple(zip(ids, names, salary)))

# map函数
# 与zip函数类似，但是不同之处在于如果各个列表元素个数不一致，也会进行并行遍历 ，没有对应的元素补空
print()


def fun(x, y, z):
    return (x, y, z)


users = map(fun, ids, names, salary)
print(users)
print(list(user))

# 练习：
# 1.利用列表实现数据结构--栈
# 2.接收用户输入的数字，输入负数时结束输入。存入一个列表
#   然后找出用户所输入的所有数字中最大的数，最小的数，再将所有数字从小到大排序输出
numbers = []

while True:
    number = input("请输入一个大于等于0的整数：")
    if number.isdigit():
        numbers.append(int(number))
    elif number.startswith("-") and number[1:].isdigit():
        break
    else:
        print("输入不合法")
print(numbers)

# 最大的数
# numbers.sort(reverse=True)[0]

print("最大值为：", max(numbers))
print("最小值为：", min(numbers))
print("所有数的和为：", sum(numbers))
numbers.sort()
print("从小到大排序：", numbers)

# 3.调用慧测会议管理接口，需要填写一个参数sign-数字签名
#    sign的算法如下：
#    	用户输入的参数用，去除username参数，将其余的参数按参数名的ASCII码降序排列，
#    	在得到的参数字符串之前拼接上user=username值
#    	组合成一个新的字符串,加密后作为sign
#    要求：用户入参如下：
#    		address=beijing&limit=200&title=Huice_Test&time=2018-01-30&username=tianlaoshi
#    	    结果:user=tianlaoshititle=Huice_Test&time=2018-01-30&limit=200&address=beijing
data = "address=beijing&limit=200&title=Huice_Test&time=2018-01-30&username=tianlaoshi"
data_list = data.split("&")
user = ""
for item in data_list:
    if item.startswith("username="):
        data_list.remove(item)
        user = item.split("=")[-1]
data_list.sort(reverse=True)
print("user=%s&%s" % (user, "&".join(data_list)))
