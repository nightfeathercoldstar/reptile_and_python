import requests
import re
import csv
url="https://movie.douban.com/top250"
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}
resp=requests.get(url,headers=headers)
print(resp.text)
page_content=resp.text

#解析数据
obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>',re.S)
result=obj.finditer(page_content)
f=open("data.csv",mode="w",encoding="utf-8")
csvwriter=csv.writer(f)
for i in result:
    print(i.group("name"))
    dict=i.groupdict()
# dict['year']=dict['year'].strip()
    csvwriter.writerow(dict.values())
f.close()
print('over!')