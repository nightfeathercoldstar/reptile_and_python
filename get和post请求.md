import requests

url="http://movie.douban.com/"

headers={

   "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"

  

}

resp=requests.get(url,headers=headers)

print(resp.text)

resp.close()





import requests

url="https://fanyi.baidu.com/sug"

s=input("请输入你想要搜索的英文单词")

dat={

    "kw":s

}

resp=requests.post(url,data=dat)

print(resp.json())

resp.close()



import requests

url = "https://movie.douban.com/j/chart/top_list"

#重新封装参数

param={

    "type":"24",

    "interval_id":"100:90",

    "action":"",

    "start":0,

    "limit":20,

}

headers={

    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"

}

reps=requests.get(url,params=param,headers=headers)

print(reps.json())

reps.close()