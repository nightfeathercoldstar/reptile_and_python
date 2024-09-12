import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, counter):
        super().__init__()
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting", self.name)
        thread_lock.acquire()
        print_time(self.name, self.counter, 3)
        thread_lock.release()
        print("Exiting", self.name)

def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1

thread_lock = threading.Lock()
threads = []

# 创建新线程
thread1 = MyThread("Thread-1", 1)
thread2 = MyThread("Thread-2", 2)

# 启动新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()

print("Exiting Main Thread")
