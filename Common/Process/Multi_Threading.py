from time import sleep,ctime
import threading

def talk(content,loop):
     for i in range(loop):
         print("Start talk:%s %s" %(content,ctime()))
         sleep(2)

def writ(content, loop):
    for i in range(loop):
        print("Start writ:%s %s" % (content, ctime()))
        sleep(3)
threads=[]
t1=threading.Thread(target=talk,args=('Life is long!',2))
threads.append(t1)
t2=threading.Thread(target=writ,args=('Life is short',2))
threads.append(t2)
if __name__=='__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("All thread end! %s" %ctime())