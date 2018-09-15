def add(a, b):
    return a + b


class Student(object):
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

if __name__ == '__main__':
    print("demo01模块执行")