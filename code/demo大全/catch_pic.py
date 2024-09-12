import requests
from bs4 import BeautifulSoup
url="https://www.umeituku.com/bizhitupian/weimeibizhi/"
resp=requests.get(url)
resp.encoding="utf-8"
result1=BeautifulSoup(resp.text,"html.parser")
alist=result1.find("div",class_="TypeList").find_all("a")
# print(alist)
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

