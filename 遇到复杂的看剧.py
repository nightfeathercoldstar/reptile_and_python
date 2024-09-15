# 1拿到主页面的页面源代码，找到iframe
# 2从iframe中的页面源代码中拿到m3u8文件
# 3下载第一层m3u8文件->下载第二层m3u8文件
# 4下载视频
# 5下载秘钥
# 6合并所有的ts文件为一个长视频
#考虑到91看剧网无需查看iframe，因此直接开始查找m3u8
import requests
from bs4 import BeautifulSoup
import aiohttp
import aiofiles
from Crypto.Cipher import AES 
from lxml import etree
import re
import asyncio




headers={
    "user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
    "origin":"https://91mjww.com",
    "Connection":"close"

}




def get_first_m3u8(url):
    resp=requests.get(url,headers=headers)
    with open("无耻之徒第一季第一集1.m3u8",mode="wb") as f:
        f.write(resp.content)

    with open("无耻之徒第一季第一集1.m3u8",mode="r") as f:
        for line in f:
            line=line.strip()
            if line.startswith("#"):
                continue
            else:
                print("第一层m3u8下载完毕")
                return line
            



def get_second_m3u8(url):
    resp=requests.get(url,headers=headers)
    with open("无耻之徒第一季第一集2_m3u8.txt",mode="wb") as f:
        f.write(resp.content)
    print("第二层m3u8下载完毕")




def main(url):
    resp=requests.get(url,headers=headers)
    obj=re.compile(r'var vid="https%3A%2F%2F(?P<h1>.*?)%2F(?P<h2>.*?)%2F(?P<h3>.*?)%2F(?P<h4>.*?)";',re.S)
    all=obj.finditer(resp.text)
    s1="https://"
    for iter in all:
        dict=iter.groupdict()
    s1=s1+dict['h1']+"/"+dict['h2']+"/"+dict['h3']+"/"+dict['h4']
    print("开始请求第一层m3u8")
    return s1




async def down_load_ts(url,name,session):
    async with session.get(url,headers=headers) as resp:
        async with aiofiles.open(f"video/{name}",mode="wb") as f:
            # print(resp)
            await f.write(await resp.read())
    # print(f"ts{name}小视频下载完毕")




async def aio_download(up_url):
    tasks=[]
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open("无耻之徒第一季第一集2_m3u8.txt",mode="r",encoding="utf-8") as f:
            async for line in f:
                if line.startswith("#"):
                    continue
                line=line.strip()
                ts_url=up_url+line
                print(ts_url)
                line=line.split("/")[5]
                task=asyncio.create_task(down_load_ts(ts_url,line,session))
                tasks.append(task)


            await asyncio.wait(tasks)




async def aio_dec():
    tasks=[]
    async with aiofiles.open("无耻之徒第一季第一集2_m3u8.txt",mode="r",encoding="utf-8") as f:
        async for line in f:
            if line.startswith("#"):
                continue
            line=line.strip()
            line=line.split("/")[5]            
            task=asyncio.create_task(dec_ts(line))
            tasks.append(task)
        await asyncio.wait(tasks)



async def dec_ts(name):
    aes=AES.new(key=b"326d3e539daca8cd",IV=b"0000000000000000", mode=AES.MODE_CBC)
    async with aiofiles.open(f"video/{name}",mode="rb") as f1,aiofiles.open(f"video/temp_{name}",mode="wb") as f2:
        bs=await f1.read()
        await f2.write(aes.decrypt(bs))
    print(f"{name}加载完毕")



if __name__=="__main__":
    # url="https://91mjww.com/vplay/MjU4LTEtMA==.html"
    # first_m3u8_url=main(url)
    # second_m3u8_url=get_first_m3u8(first_m3u8_url)
    # second_m3u8_url="https://s1.fsvod1.com"+second_m3u8_url
    # get_second_m3u8(second_m3u8_url)
    # up_url="https://s1.fsvod1.com"
    # asyncio.run(aio_download(up_url))
    asyncio.run(aio_dec())
