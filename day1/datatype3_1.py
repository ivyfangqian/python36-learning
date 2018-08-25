# -*-coding:utf-8-*-

# 整型 num =1,可以是正数、负数、0,3.x版本将long合并到int中，int为布线长度整整型
# 浮点数 fl =1.2，8字节双精度浮点型
# 复数 1+2j complex(1,2)
# 字符串 str= ‘string’，有序不可变序列
# 布尔值 True, False
# 列表 list = [1,2,3] ，有序可变序列
# 元组 tuple=(‘a’,’b’,’c’)，有序不可变序列
# 字典 dict = {name:’Harry', age:12, height:150}，无序可变序列
# 集合 s= set([1,1,2,2,3]) ,无序可变不重复元素的序列
# 不可变集合 s= frozenset([1,1,2,2,3]) ,是一个无序可不变不重复元素的序列
# 空值 None

# 不可变数据类型
# 整型、浮点型、字符串、元组、不可变集合
# 可变数据类型：列表、字典、集合

# 有序数据集合：字符串、列表、元组
# 无序数据集合：字典、集合

# 整型 int
# python2.x,整型分为两种，一种为整型 int，一种为长整型 long，int类型最大长度为32位，long不限制长度，定义时可以用a = 1L
# python3.x,整型只有int，将long合并到int中
num = 1
print(type(num))

# 查看我们变量的内存地址
print('num:', id(num))
num1 = 1
print('num1:', id(num1))
num = 2
print('重新赋值后的num:', id(num))

# 浮点数float，8字节双精度浮点数
fl = 1.2
print(type(fl))

# 对于精度来说，float>int,int->float不会出现精度损失
print(float(num1))
# 但是如果float转为int，就会损失掉小数位
print(int(fl))

# 复数
x = 1 + 2j
y = complex(3, 4)
print(type(x), type(y), x, y)

# ------------------布尔值---------------------------------------------------------------------------
boolean = True
boo_res = True and False
print(boolean)
print(boo_res)
print(boolean and True)
print(1 > 2 or 2 < 3)

# if语句中，0,'',[],(),{}，None都被认为是False
if 0 or '' or [] or () or {} or None:
    print("哈哈哈")

# None -- Python中的Null对象
# python中一个特殊的类型，被称为Null对象或者NoneType，它不支持任何运算，也没有任何的方法
# None不是0，False，'',[]
aNone = None
print(aNone)
print(type(aNone))

print(None == "")
print(None == 0)
print(None == False)
print(None == [])
print(None == ())
print(None == {})
