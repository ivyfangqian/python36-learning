# -----------------------------------------------------列表--------------------------------------
# 列表List,Python内置的一种数据类型,
# list是一种有序的集合，可以随时添加和删除其中的元素,是可变类型
aList = [1, 2, 3]
print(aList)
print(type(aList))
print(len(aList))

# 切片取值,Python提供了切片（Slice）操作符，能大大简化这种操作,
# [0:3]==>[0,3),从索引为0开始取值，取到索引为3的值，但不包含3
print(aList[0:3])
print(aList[1:3])
print(aList[0:])
print(aList[:3])
print(aList[0:-1])

# 常见的list内置函数'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort','del'
print(dir(aList))

persons = ['zhangsan', 'lisi', 'wangwu', 'zhaliu']
persons.append('zhangsan')
print(persons)

# insert(index, obj)		将对象插入到列表指定项
persons.insert(1, 'haha')
print(persons)

# extend()在列表末尾一次性追加另一个序列中的多个值
persons.extend(aList)
print(persons)
persons.extend(aList[0:2])
print(persons)

# 两个列表也可以用+来拼接
print([1, 2, 3] + [4, 5, 6])

# 列表是可变类型，对列表的部分内容进行修改
print(id(persons))
persons[2] = 'zhaoliu'
print(persons)
print(id(persons))

# 数组中是否含有某个元素
print(persons.__contains__('zhangsan'))
print("zhangsan" in persons)

# L.index(value, [start, [stop]])  用于从列表中找出某个值第一个匹配项的索引位置
print(persons.index('zhangsan'))

# count计数
print(persons.count('zhangsan'))

# pop     该方法从列表中弹出一个元素，默认是最后一个。并且返回弹出的元素
print(persons.pop())
print(persons)
print(persons.pop(-2))
print(persons)

# remove  从列表中移除某个值的第一个匹配项。与pop不同的是，该方法并不返回移除的元素
persons.remove(1)
print(persons)

# del从列表中按照索引删除某个元素
del (persons[-1])
print(persons)

# sort对列表进行排序,排序是按照ASCII码的顺序来排列，Z比a的顺序还要靠前
numbers = [10, 50, 20, 80, 30]
numbers.sort()
print(numbers)

# reverse对列表中的元素存放方向进行反转
numbers.reverse()
print(numbers)
