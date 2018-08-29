# ----------------元组------------------------------------------------
# 元组tuple也是python内置的一种数据类型，可以认为它是一种特殊的数组
# 元组是不可变类型，并且跟数组一样可以进行切片操作，以()来包裹
aTuple = ('ivy', 20, 'male', 170)
print(aTuple[0])
print(aTuple[0:3])
print(aTuple[:2])
print(aTuple[0:])

# 试图改变tuple中的值，会报错
# aTuple[2]=21

# T.index(value, [start, [stop]]) 判断是否是元组中的元素,如果查询不存在元素会报错
print(aTuple.index('ivy'))

# 使用成员运算符判断是否存在于元组中
print(20 in aTuple)

# 统计元组中的元素出现次数
print("20在元组中出现的次数：", aTuple.count(20))