# tag
from bs4 import BeautifulSoup
# BeautifulSoup represents the whole file

# Tag
#
# Comment is a special Navigatable,content does not include comments
# 文档的遍历 .contents 获取所有节点 不是很重要

# 文档的搜索 比较重要
# (1).find_all:字符串过滤：会查找和字符串完全匹配的内容
#
# 2 正则表达式方法: t_list = bs.find_all(re.compile("a"),limit=3)
# 传入一个函数 根据函数的要求搜索:
# 3 def name_exist(tag):
#     return tag.hass_attr("name")
# t_list = bs.find_all(name_exists)
# for i in t_list:
#     print(i)
# 4 kwargs  参数:
# t_list = bs.find_all(id = "head")
# t_list = bs.find_all(class_=TRUE)\
# 5 text 参数
# t_list = bs.find_all(text =["aaa"])

# css选择器:
# t_list= bs.select("title") 通过标签
# t_list= bs.select(".mnav") 通过类名
# t_list= bs.select("#aa") 通过id
# t_list= bs.select("a[class='bri']") 通过属性  a标签下class=“bri”
# t_list= bs.select("head>title")通过子标签
# t_list= bs.select(".mnav ~ .bri") 通过兄弟标签·




import re
import urllib.request,urllib.error



def name_exists(tag):
    return tag.has_attr("name")

def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
    res = urllib.request.Request(url = url,headers = head)
    try:
        response = urllib.request.urlopen(res)

        bs = BeautifulSoup(response, "html.parser")
        t_list = bs.select(".star>.rating45-t")
        print(t_list[0].get_text)
        # for i in t_list:
        #     print(i)
    except urllib.error.URLError as e:

        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

if __name__ == "__main__":
    askURL("https://movie.douban.com/top250")
