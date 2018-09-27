import xml.sax


# SAX是一种基于事件驱动的API。
#
# 利用SAX解析XML文档牵涉到两个部分:解析器和事件处理器。
#
# 解析器负责读取XML文档,并向事件处理器发送事件,如元素开始跟元素结束事件;
#
# 而事件处理器则负责对事件作出相应,对传递的XML数据进行处理。
#
# 1、对大型文件进行处理；
# 2、只需要文件的部分内容，或者只需从文件中得到特定信息。
# 3、想建立自己的对象模型的时候。
# 在python中使用sax方式处理xml要先引入xml.sax中的parse函数，还有xml.sax.handler中的ContentHandler。

class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.contentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # 元素开始事件处理
    def startElement(self, tag, attrs):
        self.contentData = tag
        if tag == "movie":
            print("***** movie *****")
            title = attrs["title"]
            print("Title: %s" % title)

    # 元素内容事件处理
    def characters(self, content):
        if self.contentData == "type":
            self.type = content
        elif self.contentData == "format":
            self.format = content
        elif self.contentData == "year":
            self.year = content
        elif self.contentData == "rating":
            self.rating = content
        elif self.contentData == "stars":
            self.stars = content
        elif self.contentData == "description":
            self.description = content

    # 元素结束事件处理
    def endElement(self, tag):
        if tag == "type":
            print("type: %s" % self.type)
        elif tag == "format":
            print("format: %s" % self.format)
        elif tag == "year":
            print("year: %s" % self.year)
        elif tag == "rating":
            print("rating: %s" % self.rating)
        elif tag == "stars":
            print("stars: %s" % self.stars)
        elif tag == "description":
            print("description: %s" % self.description)


if __name__ == '__main__':
    # 创建一个XMLReader
    parser = xml.sax.make_parser()
    # 关闭命名空间
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写ContentHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    # 解析xml文件
    parser.parse(r"movies.xml")
