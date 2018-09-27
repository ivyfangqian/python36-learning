def add(a, b):
    return a + b


class Student(object):
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


# 对自己文件的单元测试用例内容
if __name__ == '__main__':
    print("demo01模块执行")
    print(123)
    print(456)

# if __name__ == '__main__':
#
# 当前执行模块名字 __main__
# print(__name__)