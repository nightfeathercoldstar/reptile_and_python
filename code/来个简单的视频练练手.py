#view-source:https://91mjww.com/vplay/MjU4LTEtMA==.html
import requests
import re
import asyncio
import aiohttp
import aiofiles
from Crypto.Cipher import AES


headers={
    "user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
    "origin":"https://91mjww.com"

}


url="https://91mjww.com/vplay/MjU4LTEtMA==.html"

resp=requests.get(url,headers=headers)
# print(resp.text)
resp.close()

obj=re.compile(r'var vid="(?P<url>.*?)";',re.S)

m3u8_url=obj.search(resp.text).group("url")


#https://https%3A%2F%2Fs1.fsvod1.com%2F20220308%2F6shoCFzt%2Findex.m3u8
# https://s1.fsvod1.com/20220308/6shoCFzt/index.m3u8
obj1=re.compile(r'https%3A%2F%2F(?P<name>.*?)%2F(?P<id>.*?)%2F(?P<end>.*?)%',re.S)
resp2=obj1.finditer(m3u8_url)
for i in resp2:
    dic=i.groupdict()
    name=dic['name']
    id=dic['id']
    end=dic['end']
resp3=f"https://{name}/{id}/{end}/1200kb/hls/index.m3u8"
print(resp3)

resp4=requests.get(resp3,headers=headers)
resp4.close()

with open("无耻之徒.m3u8",mode="wb") as f:
    f.write(resp4.content)

resp4.close()
print("下载完毕")

#解析m3u8文件
# n=1
# with open("无耻之徒.m3u8",mode="r") as f:
#     for line in f:
#         line=line.strip()
#         if line.startswith("#"):
#             continue
        

# #下载视频的片段
#         resp5=requests.get('https://s1.fsvod1.com'+line,headers=headers)
#         # print(resp5)
#         f=open(f"video/{n}.ts",mode="wb")
#         f.write(resp5.content)
#         f.close()
#         resp5.close()
#         n+=1


#拿到秘钥
# key_url="https://s1.fsvod1.com/20220308/6shoCFzt/1200kb/hls/key.key"
# def get_key(url):
#     resp6=requests.get(url)
#     return resp6.content

# key=get_key(key_url)


#解密
aes=AES.new(key=b"326d3e539daca8cd",IV=b"0000000000000000", mode=AES.MODE_CBC)
n=1
while n<=10:
    with open(f"video/{n}.ts",mode="rb") as f1,open(f"video/temp_{n}.ts",mode="wb") as f2:
        bs = f1.read()
        f2.write(aes.decrypt(bs))
        n+=1