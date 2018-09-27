# 文件对象模型（Document Object Model，简称DOM），是W3C组织推荐的处理可扩展置标语言的标准编程接口。
# 一个 DOM 的解析器在解析一个 XML 文档时，一次性读取整个文档，把文档中所有元素保存在内存中的一个树结构里，之后你可以利用DOM 提供的不同的函数来读取或修改文档的内容和结构，也可以把修改过的内容写入xml文件。
# python中用xml.dom.minidom来解析xml文件

from xml.dom.minidom import parse
import xml.dom.minidom

# 解析xml文件生成Dom树对象
DomTree = parse(r"movies.xml")

# 获取所有电影
collection = DomTree.documentElement

# 遍历所有movie对象，打印详细movie信息
if collection.hasAttribute("shelf"):
    print("Root Element : %s" % collection.getAttribute("shelf"))

movies = collection.getElementsByTagName("movie")
for movie in movies:
    print("***** movie *****")
    if movie.hasAttribute("title"):
        print("title: %s" % movie.getAttribute("title"))

    movie_type = movie.getElementsByTagName("type")[0]
    print("type: %s" % movie_type.childNodes[0].data)
    movie_format = movie.getElementsByTagName("format")[0]
    print("type: %s" % movie_format.childNodes[0].data)

    try:
        # year标签可能不存在，放在try语句中
        movie_year = movie.getElementsByTagName("year")[0]
    except IndexError:
        pass
    else:
        print("year: %s" % movie_year.childNodes[0].data)
    movie_rating = movie.getElementsByTagName("rating")[0]
    print("rating: %s" % movie_rating.childNodes[0].data)
    movie_stars = movie.getElementsByTagName("stars")[0]
    print("stars: %s" % movie_stars.childNodes[0].data)
    movie_description = movie.getElementsByTagName("description")[0]
    print("description: %s" % movie_description.childNodes[0].data)
