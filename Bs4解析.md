Bs4就是通过对页面的标签和属性进行解析
# bs4应用方法
page=BeautifulSoup(page_text,"html.parser")#消除警报
result1=page.find("标签","属性"="属性值")
print(result.get(""标签名))

## bs4的小实例
import requests

from bs4 import BeautifulSoup

url="http://hksclz.com/groceries/index"

resp=requests.get(url)

#print(resp.text)

  
  

#把页面源代码交给bs4处理，生成bs对象

page=BeautifulSoup(resp.text,"html.parser") #直接制定html解析器

#从bs对象里面查找数据

#find(标签，属性=值)

#find_all(标签，属性=值)

table=page.find("div",class_="box_out_form box_out_form2")#class是pyhton关键字，bs为了避免这种情况可以在末尾加上下划线

table=page.find("div",attrs={"class":"box_out_form box_out_form2"})#和上一行是一个意思，此时可以避免class

#print(table)

trs=table.find_all("tr")[1:]

for tr in trs:

    tds=tr.find_all("td")

    name=tds[0]

    name1=tds[1]

    name2=tds[2]

    print(name,name1,name2)



### 抓取壁纸网站图片
import requests

from bs4 import BeautifulSoup

url="https://www.umeituku.com/bizhitupian/weimeibizhi/"

resp=requests.get(url)

resp.encoding="utf-8"

result1=BeautifulSoup(resp.text,"html.parser")

alist=result1.find("div",class_="TypeList").find_all("a")

#print(alist)

for i in alist:

    href=i.get("href")

    child_page_resp=requests.get(href)

    child_page_resp.encoding="utf-8"

    child_page_resp_text=child_page_resp.text

    child_page=BeautifulSoup(child_page_resp_text,"html.parser")

    img=child_page.find("p",align="center")

    img=img.find("img")

    print(img.get("src"))

    break




