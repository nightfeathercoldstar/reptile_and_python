import requests
from bs4 import BeautifulSoup
url="http://hksclz.com/groceries/index"
resp=requests.get(url)
# print(resp.text)


#把页面源代码交给bs4处理，生成bs对象
page=BeautifulSoup(resp.text,"html.parser") #直接制定html解析器
# 从bs对象里面查找数据
# find(标签，属性=值)
#find_all(标签，属性=值)
table=page.find("div",class_="box_out_form box_out_form2")#class是pyhton关键字，bs为了避免这种情况可以在末尾加上下划线
table=page.find("div",attrs={"class":"box_out_form box_out_form2"})#和上一行是一个意思，此时可以避免class
# print(table)
trs=table.find_all("tr")[1:]
for tr in trs:
    tds=tr.find_all("td")
    name=tds[0]
    name1=tds[1]
    name2=tds[2]
    print(name,name1,name2)