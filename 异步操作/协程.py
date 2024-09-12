# python编写程序的协议
# 所有异步程序的开始都需要await
# 书写异步操作需要 1先定义函数,形成协程对象 2创造操作列表 3await和wait列表 4在主函数中run函数
# import asyncio
# import time

# async def fun():
#     print("你好，任思羽")

# if __name__=="__main__":
#     g=fun()    #此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
#     asyncio.run(g)    #协程对象运行需要的asyncio模板

# async def func1():
#     print("你好，我叫任思羽")
#     await asyncio.sleep(4)
#     print("哈哈哈哈")

# async def func2():
#     print("你好，我叫小任思羽")
#     await asyncio.sleep(2)
#     print("一哈哈哈哈")

# async def func3():
#     print("你好，我叫大任思羽")
#     await asyncio.sleep(3)
#     print("啊哈哈哈哈")

# async def main():
#     #第一种写法
#     # f1=func1()
#     # await f1
#     # f2=func2()
#     # await f2
#     # f3=func3()
#     # await f3
#     # 第二种写法
#     tasks=[
#         asyncio.create_task(func1()),
#         asyncio.create_task(func2()),
#         asyncio.create_task(func3())
# ]
#     await asyncio.wait(tasks)
  
# if __name__=="__main__":
#     asyncio.run(main())

# 在爬虫中的应用
# async def download(url):#下载程序
#     print("准备开始下载")
#     await asyncio.sleep(2)
#     print("下载完成")

# async def main():
#     urls=[
#         "http://www.baidu.com",
#         "http://www.bilibili.com",
#         "http://www.163.com"
#     ]
#     tasks=[]
#     for url in urls:
#         d=asyncio.create_task(download(url))
#         tasks.append(d)
#     await asyncio.wait(tasks)


# if __name__=="__main__":
#     asyncio.run(main())