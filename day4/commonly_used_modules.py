# os - -对目录或文件操作
# 变量类
# os.environ - -以字典形式返回系统环境变量
#
# 函数类
# os.system(command) - -执行命令行（运行外部程序），不能存储结果
# os.startfile(path) - -windows特有，模拟双击打开文件
# mac / linux - - subprocess.Popen(path)
# popen(command) - -执行命令行，并返回一个文件对象
# os.getpid() - -返回当前进程ID
#
# 操作路径：
# os.getcwd() - -得到当前工作的目录
# os.listdir() - -指定目录下所有的文件和目录名
# os.mkdir() - -创建目录, 已存在报错
# os.makedirs() - -创建多级目录
# os.rmdir() - -删除指定目录, 只能是空目录(不能有文件或子目录)
# os.removdirs() - -删除多级目录, 只能是空目录
# os.chdir() - -改变目录到指定目录
# os.path.isfile() - -判断指定对象是否为文件。是返回True, 否则False
# os.path.isdir() - -判断指定对象是否为目录。是True, 否则False
# os.path.exists() - -检验指定的对象(文件)
# 是否存在
# os.path.split() - -返回路径的目录和文件名
# os.path.join(path, name) - -连接目录和文件名
# os.path.dirname(path) - -返回path中的文件夹部
# os.path.basename(path) - -返回文件名
# os.path.abspath(path) - -获得绝对路径
#
# 练习：
# report文件夹中，是所有自动化测试报告的存放路径。
# 编写new_report函数，传入路径。返回最新一份报告的文件名(完整路径 + 文件名)
# 1.
# 报告以时间戳命名
# *2.
# 报告不以时间戳命名
#
# 操作文件：
# os.path.getmtime(path) - -文件或文件夹的最后修改时间，从新纪元到访问时的秒数
# os.path.getctime(path) - -输出文件最近访问时间
# os.path.getsize(path) - -文件或文件夹的大小，若是文件夹返回0
# os.remove(path) - -移除文件
# os.rename(old, new) - -重命名文件或目录
# os.chown(path, uid, gid) - -改变文件或目录所有者
# os.chmod(path, mode) - -改变文件访问权限
# os.chmod('/home/user/c/a.tar.gz', 0777)
#
# shutil - -高级的
# 文件、文件夹、压缩包
# 处理模块
# shutil.copyfile(src, dst) - -拷贝文件, 如果当前的dst已存在的话就会被覆盖掉
# shutil.copy(src, dst) - -拷贝文件和权限
# shutil.copytree(src, dst, symlinks=False, ignore=None) - -递归的去拷贝文件
# shutil.rmtree(src) - -递归删除一个目录以及目录内的所有内容
import shutil
shutil.copy(r"d:\test\test.txt",r"d:\test\test_copy.txt")
shutil.copy(r"d:\test\ivy\test03.py",r"d:\test\copy")

# time - -提供了各种操作时间值
# time.time()
# 获取当前时间时间戳 - -秒
# time.ctime(seconds)
# 根据秒数取时间戳 - -美式时间格式
# time.asctime([tuple])
# 根据时间元祖，获取时间戳 - -美式时间格式
# time.localtime(seconds)
# 将秒数转换成一个时间值元祖
# time.mktime(tuple)
# 将一个时间值元祖转换成秒数
# time.sleep(seconds)
# 延迟执行给定的秒数
# *time.strftime(format[, tuple_time])
# 根据传入的格式化字符串，将tuple时间格式化为指定的格式
# tuple_time可以不传，不传返回当前时间格式化后的结果
#  python中时间日期格式化符号:
# %y     两位数的年份表示（00-99）
# %Y     四位数的年份表示（000-9999）
# %m     月份（01-12）
# %d     月内中的一天（0-31）
# %H     24小时制小时数（0-23）
# %I     12小时制小时数（01-12）
# %M     分钟数（00=59）
# %S     秒（00-59）
# time.strptime(string, format)
# 传入的时间为字符串
# 按照传入的format解析字符串时间为tuple格式的时间

# random - -生成随机数
# random.uniform(a, b)
# 返回a和b范围内的随机实数[a, b)
# andom.randint(a, b)
# 返回整数a和b范围内数字[a, b]
# random.random()
# 返回随机数，它在0和1范围内(不包括1)
# random.randrange(start, stop[, step])    返回整数范围的随机数
# random.sample(array, x)
# 从集合或元祖中返回随机x个元素 - -集合形式
# random.shuffle(array)
# 给指定的序列进行随机移位
#
# 练习：
#     0.编写一个方法，输出当前时间三天前的时间点，格式：2017-05-01_13:59:06
#     1.编写一个方法，根据传入的美式时间字符串(13:28:06_12/21/2018)，生成标准时间字符串(2018-12-21_13:28:06)
#
# 作业：
#     1.编写一个方法，接受参数为一个列表：[2017, 01, 15] (不考虑1970.1.1之前的时间点)
#       随机输出2017.1.15日 00:00:00 之前的一个时间点，格式为：2017-01-01_13:59:06
#     2.用python脚本，写一个斗地主的发牌程序
#       3个人每人17张，三张底牌归地主所有
#       要求：函数返回一个字典，{地主：[], 农民1:[], 农民2:[]}
