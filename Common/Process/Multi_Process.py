from time import sleep,ctime
import multiprocessing

def talk(content,loop):
     for i in range(loop):
         print("Start talk:%s %s" %(content,ctime()))
         sleep(2)

def write(content, loop):
    for i in range(loop):
        print("Start write:%s %s" % (content, ctime()))
        sleep(3)
process=[]
t1=multiprocessing.Process(target=talk,args=('Hello 51zxw!',2))
process.append(t1)
t2=multiprocessing.Process(target=write,args=('Life is short,You need Python!',2))
process.append(t2)
if __name__=='__main__':
    for t in process:
        t.start()
    for t in process:
        t.join()
    print("All thread end! %s" %ctime())