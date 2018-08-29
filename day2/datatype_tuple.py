# ----------------元组------------------------------------------------
# 元组tuple也是python内置的一种数据类型，可以认为它是一种特殊的数组
# 元组是有序的不可变数据类型，并且跟数组一样可以进行切片操作，以()来包裹
# 创建元组
# 元组用圆括号表示，对象用逗号分隔
#   方式一：(1, 2, 3)
#   方式二: 1, 2, 3
user = (1, "小明", 20)
print(user)
user = 1, "小明", 20
print(user)

# 访问元组对象
# 通过索引、分片
aTuple = ('ivy', 20, 'male', 170)
print(aTuple[0])
print(aTuple[0:3])
print(aTuple[:2])
print(aTuple[0:])

# 使用成员运算符判断是否存在于元组中
print(20 in aTuple)

# T.index(value, [start, [stop]]) 判断是否是元组中的元素,如果查询不存在元素会报错
print(aTuple.index('ivy'))

# 统计元组中的元素出现次数
print("20在元组中出现的次数：", aTuple.count(20))

# 元组中的元素值是不允许修改的--因为tuple不可变，所以代码更安全
# 试图改变tuple中的值，会报错
# aTuple[2]=21

# 元祖运算符
# 	+ 连接: tup3 = tup1 + tup2;
# 	*N 复制并连接: 重复N次 tup3 = tup1 * 3
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)
print(tuple1 * 5)

# 内置函数作用于元祖
# 	len(tuple)：计算元组元素个数。
# 	max(tuple)：返回元组中元素最大值。
# 	min(tuple)：返回元组中元素最小值。

numbers = (10, 50, 30, 40, 20)
print(len(numbers))
print(max(numbers))
print(min(numbers))

# 	tuple(seq)：将序列转换为元组。
list_nums = [10, 50, 30, 40, 20]
print(tuple(list_nums))

# select id,name,salary from salary
#
# 练习：员工工资表，查询结果集如下：((1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000))
# 	  1.计算员工的平均工资
# 	 *2.输出工资最高的员工姓名


# 删除元组
# 	del语句来删除整个元组
# del user
