import xlwt
import re
import urllib.request,urllib.error
from bs4 import BeautifulSoup

def main():
    baseurl = "https://courses.rice.edu/courses/!SWKSCAT.cat?p_acyr_code=2021&p_action=CATASRCH&p_onebar=&p_mode=AND&p_subj_cd=COMP&p_subj=COMP&p_dept=COMP&p_school=EN&p_df=&p_submit="

    count(baseurl)

    print("complete")


def count(baseurl):
    cont = 0
    datalist= []
    html = askURL(baseurl)
    res = BeautifulSoup(html,"html.parser")
    for item in res.find_all("<tr>","<td data-label="):
        cont = cont+1

    print(res)
    print(cont)






#得到指定一个url的内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
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




if __name__ == "__main__":
    main()

