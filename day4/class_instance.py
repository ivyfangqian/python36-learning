# 面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
# OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

# 面向过程 -- 程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。
# 面向对象 -- 程序设计把计算机程序视为一组对象的集合，用对象的调用来完成程序。

# 面向过程与面向对象的区别
# 以盖房子举例：
# 面向过程：我去买砖瓦水泥，我来砌墙，我去买门，我去做窗户，我去给房间布线，我来对房子进行装修；
# 面向对象：我让购买材料的人员去买砖瓦水泥，让泥瓦匠来砌墙，
# 让家具城的人给我送门窗过来，让电工来进行布线，找装修公司来进行装修。

# 区别在哪里？
# 第一种所有的事情都是你去做，
# 第二种所有的事情都有专门的人去做，我们负责指挥（调用）。
# 所谓面向对象编程思想，就是说要是有什么事情去做的话，不要上来就自己去干，
# 所有事情都自己干，如果事情很复杂，那么过程将会很乱，没有条理。而应该怎么样呢？
# 应该分工明确，分解这件事情，各司其职，当然这是要由我们去分解，由我们去创建对象，赋予他们职能。
# 具体的活，再让他们去干（调用）。

# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。
# 自定义的对象数据类型就是面向对象中的类（Class）的概念。
# python中面向对象有两个重要的主题，类和类的实例(对象)

# 类是对某一类具有共同特点的事物的抽象，是对象的定义，像是玩具的模具
# 类的实例（对象）是类的产物，它存放了类中定义的对象的具体信息，
# 像是生产线上根据同一个模具生产的不同规格的玩具

# 类是对某一类具有共同特点的事物的抽象,是在概念上的一个定义
# 		比如：动物，人，学生。但是单独说这三个概念的时候，不代表任何一个具体的个体
#
# 类的具体实例叫做 【对象】 【类的实例】 【实例化一个类】
# 		学生是类，张三是一个具体的学生就是 学生类的实例(Instance)，也叫学生对象

# 类语法
# class 类名(继承的类的类名):
#     类体代码
# 注意：类名命名规则：名词，首字母大写，如果由多个单词组成，每个单词首字母都要大写
# 类包含成员变量和方法

# 构造函数（初始化函数） __init__(self)
# 	作用：python在创建类的实例的时候，会调用这个类的__init__()方法初始化数据
#
# 	self：创建的实例自身(存储当前对象的地址)
# 		所有的类方法第一个参数默认是self，但是调用的时候不需要传值
class Student(object):
    def __init__(self):
        pass


# 类的属性：变量
#     成员变量--属于实例的变量，例如学生姓名，身高
#         每次实例化就创建，实例结束就销毁
#             *一般是在__init__方法中通过self完成 定义
#             *类内部：通过self访问，类外部：通过实例名访问(一般需要封装getter)
#
#     类变量--属于类的，类的对象通用的，统一的变量，例如
#         属于类自己的变量（保存在内存），每次被构造的时候，拷贝一个副本给对象
#             *在类起始处统一定义
#             *通过类名或实例来访问
#                 通过对象的修改只对当前类生效，通过类名的修改才能改变值
class HuiCeStudent(object):
    """HuiCe Student class"""
    school = "慧测"

    # 私有变量：__变量名
    # python使用的是名字重整技术，改变了私有变量的值：_类名__变量名
    # 私有变量无法在外部直接通过 类.变量 方式获取
    # 但是在类内部可以随意使用
    # 一般外部想要获取私有变量值，可以在类中添加私有变量的get方法
    # 一般外部想要修改私有变量值，可以在类中添加私有变量的set方法
    __tuition = 8800

    # __init__()方法是一种特殊的方法。我们称之为初始化方法，
    # python在创建类的实例的时候，会调用这个类的__init__()方法
    # 类中的方法，参数中一定要传递self,self指的是对象自己
    # 我们根据图纸来建造房子，房子造好了，每个人都要回自己的家，self相当于门牌号
    def __init__(self, name):
        self.name = name  # 类中使用成员变量，用self.来访问

    def print_name(self):
        print("我叫%s" % self.name)

        # 实例化对象
        # zhangsan = HuiCeStudent() --报错，因为init需要传入name

    @classmethod
    def get_tuition(cls):
        return cls.__tuition

    @classmethod
    def set_tuition(cls, tuition):
        cls.__tuition = tuition

    @staticmethod
    def welcome():
        print("欢迎来到" + HuiCeStudent.school)

    def __str__(self):
        return HuiCeStudent.school + " : " + self.name


zhangsan = HuiCeStudent("zhangsan")
zhangsan.print_name()
print(zhangsan.school)

lisi = HuiCeStudent("lisi")
lisi.print_name()
print(zhangsan.school)
# lisi.school = "HuiCeAuto"
# print(lisi.school)

HuiCeStudent.school = "慧测自动化班"
print(zhangsan.school)
print(lisi.school)

HuiCeStudent.set_tuition(10800)
print(zhangsan.get_tuition())

# 专属变量:__xx__
# 用 类名.__doc__ 来查阅类的文档说明
print(HuiCeStudent.__doc__)
# __name__：类名
print(HuiCeStudent.__name__)
# 类的所有父类组成的元组
print(HuiCeStudent.__bases__)

# 类的操作：方法
# 成员（实例）方法
# 定义：必须带有参数self
# 内部：可以访问成员变量、类变量(self或类名)、成员方法(self)、类方法(self或类名)
# 外部：通过类实例调用
# HuiCeStudent中print_name(self)就是一个成员方法
lisi.print_name()

# 类方法
# 定义：必须带有 @ classmethod、和cls参数
# 内部：可以访问类变量、类方法
# 外部：通过类实例或类名调用
print(HuiCeStudent.get_tuition())
print(lisi.get_tuition())

# 静态方法
# 定义：必须带有 @ staticmethod
# 内部：如果静态方法调用类方法或属性时，只能直接类名.属性名或类名.方法名
# 外部：通过类实例或类名调用
HuiCeStudent.welcome()

# 私有方法:
# __xx()
#
# 特殊方法：
# __xx__()
# 代表一定的协议，相当于Java中的接口方法
#
# __str__()
# 与__repr__()
# __str__() - -让class作用于print()
print(lisi)


# 函数
# __repr__() - -返回程序开发者看到的字符串
#
# __len__() - -让class作用于len()
# 函数
#
# __iter__() - -让class具有可迭代的属性, 返回值必须是对象自己
# next(): 每一次for循环都调用该方法
#
# __getitem__() - -让class作用于索引方式
#
# __getattr__()
# 当调用不存在的属性时，会试图调用此方法，来尝试获得属性

# 封装
# 1.设计一个汽车类Auto（显示给出一个参数的构造函数--传入品牌名称），
#   有速度属性speed，启动start(显示xx汽车开始运行)、加速speedup(1次速度+10)和停止stop(1次速度-30)方法；

class Auto(object):
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0

    def start(self):
        print("%s汽车开始运行" % self.brand)

    def speedup(self):
        self.speed += 10
        return self.speed

    def stop(self):
        if self.speed >= 30:
            self.speed -= 30
        else:
            self.speed = 0
        return self.speed


tesla = Auto("Tesla")
# Auto("Tesla").start()
tesla.start()
print(tesla.speedup())
print(tesla.speedup())
print(tesla.speedup())
print(tesla.speedup())
print(tesla.stop())


# 2.利用列表实现数据结构--栈
# 	理解setter和getter的作用
# 		0.不能直接访问栈
# 		1.初始化函数，传入栈的容量大小
# 		2.提供一个弾栈和一个压栈的方法
# 		3.提供一个获取栈容量大小的方法
#       4.提供一个获取栈元素个数的方法
# 		5.其他方法私有--判断栈是否到达容量，栈是否为空
class Stack(object):
    def __init__(self, capacity=10):
        self.__capacity = capacity
        self.__data = []
        self.__size = 0

    def get_capacity(self):
        return self.__capacity

    def get_size(self):
        return self.__size

    def push(self, e):
        if self.__size < self.__capacity:
            self.__data.append(e)
            self.__size += 1
        else:
            print("栈已满")

    # def pop(self):
    #     if self.__size > 0:
    #         return self.__data.pop()
    #     else:
    #         return "栈为空"

    def pop(self):
        if not self.__is_empty():
            self.__size -= 1
            return self.__data.pop()
        else:
            return "栈为空"

    def __is_empty(self):
        return len(self.__data) == 0

    def __str__(self):
        res = "{"
        for i, j in enumerate(self.__data):
            if i != self.__size - 1:
                res += str(j) + ","
            else:
                res += str(j)
        res += "}"
        return res


sta = Stack(5)
sta.push(1)
sta.push(2)
sta.push(3)
print(sta)
sta.pop()
print(sta)

# 3.然后设计一个子类Bus表示公共汽车，Bus增加一个属性passenger表示乘客数量。
#   另外在添加两个方法gotOn和gotOff表示乘客的上车和下车；通过main方法完成对Auto和Bus的使用


# *if __name__ == '__main__' 该如何理解?
# 		脚本语言--逐行动态执行。不需要入口程序（main方法）--> 缺点
# 		__name__ 是内置变量，用于表示当前模块的名字
# 			如果一个模块被直接运行，其 __name__ 值为 __main__
if __name__ == '__main__':
    print("如果我这个py文件被直接运行，这行才会被打印")

# 面向对象的四个特点：封装，抽象，继承，多态
# 封装：对数据的封装--》列表，元组，字典
#       对脚本语句的封装--》函数
#       对数据，方法的封装--》类
#       对某一类数据操作封装==》模块
#       对某一些文件的封装==》包
# 好处：方便进行数据的存取、更多的复用、增强代码的可读性
# 抽象：对同一类事物的属性和方法进行抽取，抽象成类
# 继承：子类继承父类的属性和方法
# 多态：不同对象对同一方法响应不同的情况
list1 = [3, 2, 6, 7, 8]

list1.append(9)
print(list1)

list1.sort()
print(list1)


# 定义一个子类，继承list，类体中，什么都不做
class SubList(list):
    pass


print('*' * 30)

subList = [3, 2, 6, 7, 8]

subList.append(9)
print(subList)

subList.sort()
print(subList)

# 继承和多态
# 		继承 -- 复用
# 			方法覆盖(重写)
# 			多态--对扩展开放，对修改关闭
# 				1.当我们需要传入一个对象时，我们可以不传入具体的类型，而传入一个抽象的概念---父类对象
# 				2.这样，在程序实际运行时，可以动态绑定传入的类型
# 			    3.因为都有共同的父类，所以一定有共同的方法。使用时，内部使用时，调用共有的方法就可以
# 				  isinstance(instance, class)方法
# 			多重继承
#   				(class1, class2, class3)  --class1优先


class Animal(object):
    def run(self):
        print("animal run...")

    def eat(self):
        print("animal eat...")


class Cat(Animal):
    def run(self):
        print("cat run...")

    def eat(self):
        print("cat eat...")


class Dog(Animal):
    def run(self):
        print("dog run...")

    def eat(self):
        print("dog eat...")


class Person(object):
    def __init__(self, name):
        self.name = name

    def feed(self, animal):
        animal.eat()

# 作业：
#     设计一个部门类Department，属性为部门名称（name）
#     需求：
#         1.直接通过Department调用get_all方法，返回公司员工总数
#         2.通过部门实例，调用方法get_count方法，返回部门员工数
#         3.通过部门实例，调用方法get_employees()，显示该部门所有员工信息
#           格式为： 工号-xxx ，姓名-xxx ，手机号-xxx，工资-xxx
#         提示：有人入职，员工数就要增加，部门存入员工对象
#
#     设计一个员工类Employee，员工属性有姓名（name）、手机号(phone)、工资(salary)、所属部门。
#     需求：
#     1.新员工入职时，分配一个不重复的工号。从1开始排列，已离职员工工号作废。
#     2.员工本人可以调用get_salary方法查询自己的工资
#     3.员工本人可以调用get_info方法查询自己的全部信息--字典形式
#
#     测试：人力资源部（小红）、技术部（田老师、刘老师）
#           输出 每个部门的人员和公司总人数，输出两个部门的人员信息