""" 文件处理相关的工具模块 """
def print_file_info(file_name):
    f=None
    try:
        f=open(file_name,"r",encoding='UTF_8')
        content=f.read()
        print("文件的全部内容如下")
        print(content)
    except Exception as e:
        print(f"程序出现了异常，原因是{e}")
    finally:
        if f:
          f.close()
def append_to_file(file_name,data):
    f=open(file_name,"a",encoding="UTF_8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__=="__main__":
    append_to_file("D:/test_append.txt","任思羽做一个开心的吃货")