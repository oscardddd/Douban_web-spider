from urllib.request import urlopen, Request
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
# response = Request("https://movie.douban.com/top250",headers=headers)
# aa = urlopen(response)
#
# print(aa.read().decode("utf-8"))
import urllib.parse
data = bytes(urllib.parse.urlencode({"Hello":"Tuanzi"}),encoding="utf-8")

# try:
#     response = urlopen("http://httpbin.org/post",data = data,timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("TIME OUT")

response = urlopen("https://www.baidu.com/?tn=44048691_1_oem_dg")
print(response.getheader("Server"))




