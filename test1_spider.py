#-*- codeing = utf-8 -*-
import sqlite3

from bs4 import BeautifulSoup
import xlwt
import re
import urllib.request,urllib.error
from bs4 import BeautifulSoup

def main():
    baseurl = "https://movie.douban.com/top250"
    #savepath = r"C:\Users\HP\PycharmProjects\pachong\movielist.xls"

    datalist = getData(baseurl)
    #saveData(datalist,savepath)
    dbpath = "movie.db"

    print("complete")
#爬取网页

def findTitle(item,):

    other = re.compile(r'<span class="other">(.*)</span>')
    findtitle = re.compile(r'<span class="title">(.*)</span>')
    res = re.findall(findtitle,item)
    res.append(re.findall(other,item))


    for i in res:
        i = str(i)

        pos = i.find(r'\xa0/\xa0')

        if pos != -1:
            print(i[0:pos]+i[pos+9:len(i)])
        else:
            print(i)

















findT = re.compile(r'<span class="title">(.*)</span>')
findLink = re.compile(r'<a href="(.*?)">')
findImage = re.compile(r'<img.*src="(.*?)"/>',re.S)   #re.S 让换行符包含在字符中
findRaing = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findPpl = re.compile(r'<span>(.*)人评价')
findChara = re.compile(r'<p class="">(.*?)</p>',re.S)
findInq = re.compile(r'<span class="inq">(.*)</span>')
findt = re.compile(r'<span class="title">(.*)</span>')
findother = re.compile(r'<span class="other">(.*)</span>')

def getData(baseurl):
    datalist = []
    for i in range(0,250):



        url = baseurl + "?start=" + str(i*25)
        html = askURL(url)
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"):
            data = []
            item = str(item)

            titles = re.findall(findT, item)
            # titles.append(re.findall(findother,item))
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(" ")


            #从这里往后开始找符合条件的行
            link = re.findall(findLink,item)[0]
            data.append(link)

            bd = re.findall(findChara, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)

            data.append(bd.strip())     # eliminate the space

            image = re.findall(findImage,item)[0]
            data.append(image)

            rating = re.findall(findRaing,item)
            data.append(rating)

            ppl = re.findall(findPpl,item)[0]
            data.append(ppl)

            inq = re.findall(findInq,item)
            if len(inq) != 0:

                data.append(inq)
            else:
                data.append("NONE")




            datalist.append(data)

    #print(datalist)
    return datalist

            #print(image)
            #inq = re.findall(findInq,item)
            #print(titles)
            #print(inq)



#得到指定一个url的内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    res = urllib.request.Request(url = url,headers = head)

    try:
        response = urllib.request.urlopen(res)

        html = response.read().decode("utf-8")
        # print(html)
        return html
    except urllib.error.URLError as e:

        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):

            print(e.reason)

# def saveData(baseurl):
#     dataList = []
def saveData(datalist,savepath):
    workbook = xlwt.Workbook(encoding="utf-8")  # initiate a workbook subject
    worksheet = workbook.add_sheet('豆瓣电影250')
    col = ("影片中文名","影片外文名","电影详情链接","电影详细信息","图片","评分","评价人数","评论")
    for i in range(0,8):
        worksheet.write(0,i,col[i])
    for i in range(0,250):
        data = datalist[i]
        print("第%d条" %(i+1))

        for j in range(0,8):
            worksheet.write(i+1,j,data[j])

    workbook.save(savepath)




def init_db(dbpath):
    conn  = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        cname text,
        enname text,
        info_link text,
        info text,
        pic_link text,
        score numeric, 
        ppl numeric,
        comment text
        )
        
        
    '''
    

    cursor.execute(sql)
    conn.commit()
    conn.close()

    print("create database successfully")





def saveData2DB(datalist,dbpath):
    init_db()
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            data[index] = '"'+data[index]+'"'
            sql = '''
                insert into movie250 (
                
                
                
                
                )
            
            '''









                    

                






if __name__ == "__main__":
    # main()
    init_db("movietest.db")

    print("ok")
