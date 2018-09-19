# python打开文件
# 首先使用open()函数打开一个文件，创建一个file对象
# 语法
# file_object = open(name[, mode][, buffering])

file_test = open(r'D:\test\test.txt', 'r', encoding="utf-8")

# 读取文件内容
print(file_test.read())

file_test.close()

# 关闭后再次读取会报错
# file_test.read()

# readline()：从文本中读取一行文本，该函数返回一行的文本字符串，包括换行符“\n”。
file_test = open('d:\\test\\test.txt', "r", encoding="utf-8")
print(file_test.readline())
print(file_test.readline())

file_test.close()
# read()：返回文件中剩余的文本组成的多行字符串
# 若打开文件时调用则返回文件中的所有内容（即使用read()之前没有使用readline()）
file_test = open('d:\\test\\test.txt', "r", encoding="utf-8")
print(file_test.read())

file_test.close()

# readlines()：返回由文件中剩余的文本（行）组成的列表,  遍历返回的列表即可得到每一行的内容。
file_test = open('d:\\test\\test.txt', "r", encoding="utf-8")
file_list = file_test.readlines()
print(file_list)

file_test.close()

# 想知道怎么写入么，来看我-------------------------------------------------------------------------
# 如何向文件中写入内容
# file_test = open('D:\\test.txt')
# 需要以写入模式打开文件
file_test = open('D:\\test\\test1.txt', 'w')

# write()向文件中写入内容
file_test.write('hello \n python')

# 务必要调用f.close()来关闭文件。
# 当我们写文件时，操作系统往往不会立刻把数据写入磁盘，
# 而是放到内存缓存起来，空闲的时候再慢慢写入。
# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
# 忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。
file_test.close()

# writeline(sequence)写入一个包含字符串的序列类型
file_test = open('D:\\test\\test1.txt', 'w')

# 向文件中写入内容
file_test.writelines(['hello python \n', 'huicewang.com'])

file_test.close()

# 以读的方式打开一个不存在的文件会报错
# file_test = open('D:\\test\\new.txt')

# 以写的方式打开一个不存在的文件会？？？
file_new = open('D:\\test\\new.txt', 'w')
file_new.write('Hello python')
file_new.close()

# 以写的方式打开文件，文件会被清空
file_new = open('D:\\test\\new.txt', 'w')
file_new.close()

# 那如何在打开文件的时候不清空内容，往文件中追加内容呢
file_test = open('d:\\test\\test1.txt', 'a')

# a：以追加只写的方式打开，不清空文件，在文件末尾加入内容
file_test.write('我是追加的内容，追加a代表append')

file_test.close()

# Python文件打开方式，有w,r,a,w+,r+,a+：
# r ： 以只读方式打开文件，文件不存在则出错
# w：以只写方式打开文件，文件存在则清空，不存在则建立
# a：以追加只写的方式打开，不清空文件，在文件末尾加入内容
# r只有读的权限，w和a只有写的权限，w清空文件，a不清空文件。（read, write,append）
# w+读写权限打开文件，只要打开就会清空文件,文件不存在则创建文件
# r+读写权限打开文件，如果写入了数据则会清空文件,文件不存在出错
# a+读写权限打开文件，不清空文件,在文件末尾新增写入的内容，文件不存在创建文件

file_test = open('D:\\test\\test1.txt', 'a+')

# 用tell()函数获取游标在文件中的位置
print('当前游标位置', file_test.tell())
print(file_test.readline())

print('readline后游标位置', file_test.tell())

# 可以使用seek()来移动游标的位置
file_test.seek(0)
print('seek(0)后游标位置', file_test.tell())

# 游标移动到20
file_test.seek(20)
# print file_test.read()
# print file_test.tell()

file_test.write('read and write')
print(file_test.tell())

# flush(),一般的文件流操作都包含缓冲机制，write方法并不直接将数据写入文件，而是先写入内存中特定的缓冲区。
# flush方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区。
file_test.flush()

# 不要忘记关闭文件
file_test.close()
print(file_new.closed)

file_new = open('D:\\test\\new.txt')

print(file_new.name)
print(file_new.mode)
print(file_new.closed)

file_new.close()
print(file_new.closed)

# truncate([size])
