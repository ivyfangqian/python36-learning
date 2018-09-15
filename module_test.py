# 在Python中，一个文件就称之为一个模块（Module）
# 	可以作为module的文件类型有: ".py"、".pyo"、".pyc"、".pyd"、".so"、".dll"
# 导入--完成代码的重复使用（属性，方法）
# 	import xxx
# 		导入xxx模块后，我们就有了变量xxx指向该模块，利用这个变量，就可以访问xxx模块的所有功能
# 	导入模块是用于定义的--定义变量、函数
# 		首次导入会运行代码，再次导入不会运行。除非使用reload(模块名)函数
# 		如果不想在导入的时候加载的代码（只在模块单独运行时执行）
# 			使用 if __name__ == '__main__'
import demo01

print(demo01.add(1, 2))

from demo01 import add

print(add(1, 2))

# 	解释器如何找到的模块？
# 		1.首先在当前目录查找 --将模块拷贝到当前路径?
# 		2.当前脚本指定的sys.path   --python搜索模块的路径集合
# 			可以在python 环境下使用sys.path.append(path)添加相关的路径，但在退出python环境后自己添加的路径就会自动消失
# 		3.环境变量 --PYTHONPATH
# 		4.安装设置相关的默认路径
# 			built-in --内建模块
# 			C:\Python27\Lib --所有python类库的总目录
# 				标准库模块
# 					email、json、csv、httplib、io....
# 				site-packages --第三方包（包括自定义）
# 		5.找到名字符合的就停止
import sys

print(sys.path)

# 		如果我们要引入自定义的模块：
# 			0.在project根目录中直接import名称
# 				如果是子目录
# 				如果是上级或同级目录
import day4.sub.demo02

print(day4.sub.demo02.multi(1, 2))

# 			1.添加自己的搜索目录，有三种方法：
# 				第一种是直接修改sys.path，添加要搜索的目录：
# 					import sys
# 					sys.path.append('/Users/my_py_scripts')
# 					但在退出python环境后自己添加的路径就会自动消失
# 				第二种方法是设置环境变量PYTHONPATH
# 				第三种方法是将包放到python安装目录的Lib下或sitepackage下（不推荐）

# 	包（Package）存放模块	--将多个.py文件组织起来，以便在外部统一调用
# 		完整的模块名 = 包名.子包名.模块名
# 		__init__.py
# 			每一个包，都有一个__init__.py 文件，否则就是普通目录
# 				__init__.py可以为空，也可以设置相应的内容
# 					导入包之前会优先执行__init__.py中的内容
# 	使用别名
# 		import xxx as X
# 			应用：统一变量名
# 			例：
# 					try:
#     					import json # python >= 2.6
# 					except ImportError:
#     					import simplejson as json # python <= 2.5
import day4.sub.demo02 as demo02

print(demo02.multi(2, 3))
# 	使用from
# 		从一个包中导入部分模块
# 			from selenium import webdriver
# 		从一个模块中导入部分内容
# 			from A import a, b, c --abc可以是类，也可以是方法
# 			from A import * --从A中导入 所有 __all__属性列表中定义的，允许导入的内容
from day4.sub.demo02 import multi

print(multi(3, 4))

# 	练习：新创建一个子包 sub
# 		sub中有一个模块：util.py 其中有一个工具类：Util，有一个类方法求两数之和；一个成员方法求两数之积
# 		如果单独运行该文件，显示说明文字
# 		在当前demo.py文件尝试调用该方法
from day4.sub.util import Util

print(Util().chengji(2, 3))
print(Util.jiafa(1, 2))
