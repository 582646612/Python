#!/usr/bin/python3

import threading
import time

threadLock = threading.Lock()
threads = []
exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        threadLock.acquire()
        print_time(self.name, self.counter, 2)
        # 释放锁，开启下一个线程
        threadLock.release()

def get_time():
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return dt


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, get_time()))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread 1", 1)
thread2 = myThread(2, "Thread 2", 3)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")