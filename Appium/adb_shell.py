#coding:utf-8
# for i in range(1,10):
#
#         spath="//*[@class='android.widget.LinearLayout'][%d]"%i
#         print spath
#coding:utf-8
from Function import Scroll_up
import os
# 获取app信息
# aapt dump badging xxx.apk
# 获取appactivity
# monkey -p 包名 -v -v -v 1
#
# 查看app
# pm list package
# adb shell -> su->cd /data/data - > ls - l
#启动
# os.system("adb shell am start -n com.android.settings/.Settings")
# os.system("adb shell am start -n com.android.browser/.BrowserActivity")

# // 模拟Power键
os.system("adb shell input keyevent 26")
Scroll_up(driver)
# // 模拟Home键
# os.system(("adb shell input keyevent 3")