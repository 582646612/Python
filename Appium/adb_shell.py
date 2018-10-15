# for i in range(1,10):
#
#         spath="//*[@class='android.widget.LinearLayout'][%d]"%i
#         print spath
#coding:utf-8
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
os.system("adb shell am start -n com.android.settings/.Settings")