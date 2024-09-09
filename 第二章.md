

正则表达式
正则表达测试OSChina
字符串.*?字符串  惰性匹配
匹配从字符串到字符串的最短的组合
.*   贪婪匹配
匹配从字符串到字符串最长的组合
惰性或者贪婪匹配在最后面加上字母可以表示到哪里开始停下
 
re.S让点能匹配换行符，用于预加载compile后在匹配完成后增加规则
在匹配到的地方提取需要的点
在正则表达式前加上.?<组名>，后面将这个和正则表达式一块用括号
后面使用group的时候记得要在组名上加上双引号，其不是一个变量
import re
#findall:匹配字符串中所有符合正则表达式中的内容，拿到的数据全部储存在列表中

#list=re.findall(r"\d+","我的电话号码是10086，任思羽的电话号码是521")
#print(f"{list}")

#finditer：匹配字符串中所有的内容（返回的是迭代器）适合返回内容比较多的,从迭代器中拿到内容需要group()
#iter=re.finditer(r"\d+","我的电话号码是10086，任思羽的电话号码是521")
#for i in iter:
 print(i.group())
    
    
##search:返回的结果是match对象，拿数据需要.group()，但是拿到数据后就立刻返回，不会像iter迭代器一样全部拿完
#s=re.search(r"\d+","我的电话号码是10086，任思羽的电话号码是521")
#print(s.group())


#match：是从头开始匹配，匹配一个，也需要用group()拿数据,使得\d+的作用相当于^\d+
#m=re.match(r"\d+","10086，任思羽的电话号码是521")
#print(m.group())


#预加载正则表达式
obj=re.compile("\d+")
ret=obj.finditer("我的电话号码是10086，任思羽的电话号码是521")
for i in ret:
    print(i.group())

ret=obj.findall("我的电话号码是10086，任思羽的电话号码是521")
for i in ret:
    print(f"{i}")


手刃豆瓣排行榜加后续数据处理csv
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







import requests
import re
url="http://www.dytt89.com/"
resp=requests.get(url,verify=False)#verify=False 去掉安全检验
resp.encoding="gb2312" #charset处有网站的code类型，可以复制粘贴
此处表示requests的回应可以转换字符集，使用encoding
字符集：charset



在html中，a标签表示一个超链接
<a href="url>周杰伦</a>
这就是点击网页上的字可以跳转到其他网页的原因
