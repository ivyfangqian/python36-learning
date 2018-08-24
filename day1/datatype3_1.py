# -*-coding:utf-8-*-

# 整型 num =1,可以是正数、负数、0
# 浮点数 fl =1.2
# 复数 1+2j complex(1,2)
# 字符串 str= ‘string’
# 布尔值 True, False
# 列表 list = [1,2,3]
# 元组 tuple=(‘a’,’b’,’c’)
# 字典 dict = {name:’Harry’,age:12,height:150}
# 集合 s= set([1,1,2,2,3])
# 其中，数字（包含整数、浮点数、复数）、字符串、元组是不可变类型，列表、字典是可变类型
# 空值 None

# 整型
num = 1
print(type(num))

# 查看我们变量的内存地址
print('num:', id(num))
num1 = 1
print('num1:', id(num1))
num = 2
print('重新复制后的num:', id(num))

# 浮点数
fl = 1.2
print(type(fl))

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

# None -- Python中的Null对象
# python中一个特殊的类型，被称为Null对象或者NoneType，它不支持任何运算，也没有任何的方法
aNone = None
print(aNone)

