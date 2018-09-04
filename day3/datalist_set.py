# -----------------Set集合---------------
# 集合类型 - -无序不重复元素集
# 创建
# set(序列对象)---可变集合类型

aset = set(["zhang", "wang"])

# 不支持索引和分片
# print(aset[0])

# 可以循环
for i in aset:
    print(i)

# 可以帮助列表或者元组去重
user_list = ["小明", "小红", "小明", "小红"]
user_set = set(user_list)
print(user_set, type(user_set))

user_tuple = ["小明", "小红", "小明", "小红"]
user_set = set(user_tuple)
print(user_set, type(user_set))

# 操作
# 添加一项
# s.add('x')
aset.add("zhao")
print(aset)

# 删除一项
# s.remove('H')
# remove()
# 用于删除一个set中的元素，这个值在set中必须存在，如果不存在的话，会引发KeyError错误。
aset.remove("wang")
print(aset)

# discard()
# 用于删除一个set中的元素，这个值不必一定存在，不存在的情况下删除也不会触发错误。
aset.discard("zhao")

# 弹出末尾的元素
# s.pop()
print(aset.pop())
print(aset)

# 清空
# s.clear()
aset.clear()
print(aset)

# 因为也被当做序列对象，所以可以转元组或者转列表
print(tuple(aset))
print(list(aset))

# frozenset(序列集合)---不可变集合
users = ["tom", "alice", "tom"]
frozen_set = frozenset(users)
print("不可变集合：", frozen_set)

# 转为列表或者元组
print(list(frozen_set))
print(tuple(frozen_set))

# 列表去重
# 方法一：遍历列表
numbers = [1, 2, 3, 1, 2, 3, 4]
new = []
for i in numbers:
    if i not in new:
        new.append(i)
print(new)

# 方法二:
numbers = [1, 5, 7, 2, 3, 1, 2, 3, 4]
new = list(set(numbers))
print(new)

# 但是这样改变了原来列表的顺序，可以通过sort函数进行重新排序
new.sort(key=numbers.index)
print(new)

# 练习：列表合并(用你能想到所有方法实现)
#     [1, 2, 3, 5, 6]    [0, 2, 5, 7]
#     结果：[0, 1, 2, 3, 5, 6, 7]

list1 = [1, 2, 3, 5, 6]
list2 = [0, 2, 5, 7]

