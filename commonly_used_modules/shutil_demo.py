import shutil

# shutil 是高级的文件，文件夹，压缩包处理模块。
# 你想要复制或移动文件和目录，但是又不想调用shell命令。
# shutil 模块有很多便捷的函数可以复制文件和目录。使用起来非常简单，比如：

# Copy src to dst. (cp src dst)
src = r"d:\test\test.txt"
dst = r"d:\test\test_shutil_copy.txt"
shutil.copy(src, dst)

# Copy files, but preserve metadata (cp -p src dst)
src = r"d:\test\test.txt"
dst = r"d:\test\test_shutil_copy"
shutil.copy2(src, dst)

# Copy directory tree (cp -R src dst)
# 目标目录已存在会报错
# src = r"d:\test\ivy"
# dst = r"d:\test\test_shutil_copy1"
# shutil.copytree(src, dst)

# 可以设置拷贝忽略条件，被忽略的文件，将不被拷贝
# def igonre_file(dirname, filenames):
#     return [name for name in filenames if name.endswith('.py')]
#
#
# shutil.copytree(src, dst, ignore=igonre_file)

# copytree时,可以设置忽略


# Move src to dst (mv src dst)
# src = r"d:\test\test_shutil_copy2"
# dst = r"d:\test\test_shutil_copy3\test"
# shutil.move(src, dst)


# 拷贝文件内容到另一个文件
# copyfileobj(fsrc, fdst[, length=16*1024]):
# src = r"d:\test\test.txt"
# dst = r"d:\test\test_shutil_copy.txt"
# shutil.copyfileobj(open(src, "r", encoding="utf-8"), open(dst, "w", encoding="utf-8"))

# 删除文件夹,文件夹不存在会报FileNotFoundError错
# try:
#     shutil.rmtree(r"d:\test\test_shutil_copy1")
# except FileNotFoundError as fe:
#     print("文件夹不存在", fe)

# 压缩文件
# make_archive(base_name, format, root_dir=None, base_dir=None, verbose=0,
#                  dry_run=0, owner=None, group=None, logger=None)
# 将当前py文件所在目录下，所有文件进行压缩，压缩得到d:\test\test_shutil_copy1.zip
shutil.make_archive(r"d:\test\test_shutil_copy1", "zip")
# 将root_dir=r"d:\test\test_shutil_copy1"所对应的目录，进行压缩，压缩得到d:\test\test_shutil_copy1
shutil.make_archive(r"d:\test\test_shutil_copy1", "zip", root_dir=r"d:\test\test_shutil_copy1")
