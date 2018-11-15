#coding=utf-8
import time
import calendar
import datetime
def get_time():
    dt = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
    return dt



def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


if __name__ == '__main__':
    print(get_time())
    print(getYesterday())
    # cal = calendar.month(2016, 1)
    # print ("以下输出2016年1月份的日历:")
    # print (cal)
    # import datetime
    # i = datetime.datetime.now()
    # print ("当前的日期和时间是 %s" % i)
    # print ("ISO格式的日期和时间是 %s" % i.isoformat() )
    # print ("当前的年份是 %s" %i.year)
    # print ("当前的月份是 %s" %i.month)
    # print ("当前的日期是  %s" %i.day)
    # print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
    # print ("当前小时是 %s" %i.hour)
    # print ("当前分钟是 %s" %i.minute)
    # print ("当前秒是  %s" %i.second)