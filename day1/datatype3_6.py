# -----------------Set集合---------------
# 集合类型 - -无序不重复元素集
# 创建
# set(序列对象)---可变集合类型
# 不支持索引和分片
# 可以循环
aset = set(["zhang", "wang"])
for i in aset:
    print(i)

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
