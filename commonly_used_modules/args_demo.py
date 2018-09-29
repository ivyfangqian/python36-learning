import sys

# 使用sys模块接收命令行参数
# 接收到的参数存放在sys.argv中，sys.argv是一个列表
# 命令行执行python xx.py a b c ，那么sys.argv中有四个参数，第一个是文件名
# print("命令行参数个数：", len(sys.argv))
# print("命令行参数为：", sys.argv)

# getopt模块是专门处理命令行参数的模块，用于获取命令行选项和参数，也就是sys.argv。
# 命令行选项使得程序的参数更加灵活。支持短选项模式（-）和长选项模式（--）。
# 该模块提供了两个方法及一个异常处理来解析命令行参数。
# getopt可以接收带选项的参数

import getopt


# opts, args = getopt.getopt(sys.argv[1:], "i:o:v", ["input=", "output=", "version="])
# print(sys.argv[1:])
# print("opts:", opts)
# print("args:", args)

# 接收参数
def main(argv):
    input_file = ""
    output_file = ""
    try:
        # 设定传入的短选项和长选项参数
        # getopt(args, options[, long_options]) -> opts, args
        # 返回值中opts为列表，列表中元素为元组，元组中包含两个元素，第一个是传入的选项，第二个是传入的值
        # args也是一个列表，列表中每一项是传入的不带选项的参数
        opts, args = getopt.getopt(argv, "h:i:o:", ["input=", "output="])
    except getopt.GetoptError:
        print("args_demo.py -i <input_file> -o <output_file>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("args_demo.py -i <input_file> -o <output_file>")
            sys.exit()
        # 判断传出的参数是否是-i --input，进行接收
        elif opt in ["-i", "--input"]:
            input_file = arg
        # 判断传出的参数是否是-o --ouput，进行接收
        elif opt in ["-o", "--output"]:
            output_file = arg
    print(opts)
    print("输入文件：%s" % input_file)
    print("输出文件：%s" % output_file)


if __name__ == '__main__':
    main(sys.argv[1:])
