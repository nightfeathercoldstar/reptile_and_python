#requests.get() 同步的代码->异步操作aiohttp

#pip install aiohttp

  

import aiohttp

import asyncio

  

urls=[

    "http://img.netbian.com/file/2023/0512/234031QECRj.jpg",

    "http://img.netbian.com/file/2023/0322/232520QuDUY.jpg",

    "http://img.netbian.com/file/2018/1109/18e76135e89d3aa1b5e1cf6b165fae23.jpg"

]

  

async def aiodownload(url):

    #发送请求，得到图片内容，写入文件

    #s=aiohttp.ClientSession()等同于requests里面的session

    name=url.rsplit("/",1)[1]

    async with aiohttp.ClientSession() as session:

        #session.get()

        #session.post()

        #with之后不需要再进行close操作

        async with session.get(url) as resp:

            #读取照片resp.content.read()

            #读取文本resp.text()

            with open(name,mode="wb") as f:

                f.write(await resp.content.read())

    print(name,"搞定")

  

async def main():

    tasks=[]

    for url in urls:

        tasks.append(asyncio.create_task(aiodownload(url)))

    await asyncio.wait(tasks)

  

if __name__=="__main__":

    asyncio.run(main())