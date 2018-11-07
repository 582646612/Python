__author__ = 'shikun'
import time
import datetime
def getStrTime(t_time):
    # time.strftime("%Y-%m-%d %I%p %M:%S 今天是当年第%j天  当年第%U周  星期%w",time.localtime())
    # time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

    return datetime.strftime(t_time)
