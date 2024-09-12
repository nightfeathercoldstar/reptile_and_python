# 定位到2024必看电影
import requests
import re
url="http://www.dytt89.com/"
child_href_list=[]
resp=requests.get(url,verify=False)
resp.encoding="gb2312"
# print(resp.text)
obj1=re.compile(r"2024必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2=re.compile(r"<a href='(?P<href>.*?)'",re.S)
obj3=re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)
result1=obj1.finditer(resp.text)
for it in result1:
    tr=it.group("ul")
#拿到2024必看片中的信息
#提取子页面链接的方式
result2=obj2.finditer(tr)
for itt in result2:
    child_href=url+itt.group("href").strip("/")
    # +(str)(itt.group("href").split("/")[2])
    child_href_list.append(child_href)
    # print(itt.group("href").split("/i/")[1])


print(child_href_list)
for href in child_href_list:
    child_resp=requests.get(href,verify=False)
    child_resp.encoding="gb2312"
    result3=obj3.search(child_resp.text)
    print(result3.group("movie"))
    print(result3.group("download"))