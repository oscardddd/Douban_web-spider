import re
# 创建模式对象

# pat = re.compile("AA")  #此处的aa是正则表达式 用来验证其他的字符串
# m= pat.search("ABCAA") #被校验的内容


# m = re.search("asd","asdaaa")
# print(m)
#前面加一个r 不用担心转译字符的问题

print(re.findall("ABB+","ABBCaaBC"))

print(re.sub("a","A","asadsfds")) #找到a用A替换

print(r"aab\'")
print("aab\'")


