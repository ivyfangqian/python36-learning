# 对文件系统的访问主要通过os模块来进行，os模块主要用于访问操作系统命令
# import os

import os

# 对一个文件重命名
# os.rename('D:\\test\\test.txt','D:\\test\\test01.txt')

# 删除一个文件
# os.remove('D:\\test\\hello.txt')

# 创建一个目录
# os.mkdir('D:\\test\\ivy')

# 删除一个目录
# os.rmdir('D:\\test\\ivy')

# 同时创建多个目录
# os.makedirs('D:\\test\\ivy\\test')

# os.sep 可以取代操作系统特定的路径分割符
print(os.sep)

# os.getcwd() 相当于Linux下的pwd，获取当前目录
print(os.getcwd())

# os.chdir(os.getcwd()+os.sep+'test') 进到某个目录下
os.chdir('d:\\test\\ivy')
print(os.getcwd())

# os.listdir(os.getcwd()) 相当于Linux下的ls，显示当前目录下的文件
print(os.listdir(os.getcwd()))

# os.path.isfile("test.txt") 判断是否是文件
# print os.path.isfile('test03.py')

# os.path.isdir("test.txt") 判断是否是文件夹
print(os.path.isdir('test'))

# os.path.exists("test.txt") 判断文件是否存在
# print os.path.exists('test03.py')

# os.path.getsize("test.txt") 获取文件的大小
# print os.path.getsize('test03.py')

# os.path.abspath("test.txt") 返回文件的绝对路径
# print '文件的绝对路径：', os.path.abspath('test03.py')

# os.path.basename(os.path.abspath("test.txt")) 获取文件的文件名，注意参数需要传入绝对路径
# print os.path.basename('d:\\test\\ivy\\test03.py')

# os.path.dirname(os.path.abspath("test.txt")) 获取文件的所在目录，注意参数需要传入绝对路径
# print os.path.dirname('d:\\test\\ivy\\test03.py')

# 实现目录递归遍历，查找以.py结尾的文件，并将文件绝对路径存入log.txt文件。
res = []


def go_through(dir):
    # 遍历文件夹中的所有文件夹和文件
    for i in os.listdir(dir):
        # 判断是否是文件夹，如果是文件夹，就进行递归调用
        if os.path.isdir(dir + os.sep + i):
            go_through(dir + os.sep + i)
        else:
            # 如果是文件，判断最后是不是以.py结尾
            if i[-3:] == '.py':
                res.append(dir + os.sep + i)


go_through('D:\\test')
print(res)

file_log = open('D:\\test\\log.txt', 'w+')
for i in res:
    file_log.write(i + '\n')
file_log.close()
