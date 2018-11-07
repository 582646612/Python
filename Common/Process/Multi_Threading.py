from time import sleep,ctime
import threading

def talk(content,loop):
     for i in range(loop):
         print("Start talk:%s %s" %(content,ctime()))
         sleep(2)

def write(content, loop):
    for i in range(loop):
        print("Start write:%s %s" % (content, ctime()))
        sleep(3)
threads=[]
t1=threading.Thread(target=talk,args=('Hello 51zxw!',2))
threads.append(t1)
t2=threading.Thread(target=write,args=('Life is short,You need Python!',2))
threads.append(t2)
if __name__=='__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("All thread end! %s" %ctime())