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
# stdout, stderr = CmdUtils.runCmd('adb shell dumpsys window policy', True)
# if 'mShowingLockscreen=true' in stdout:
#     if 'mScreenOnEarly=false' in stdout:
#         os.system('adb shell input keyevent 26')
#     os.system('adb shell input keyevent 82')

# os.system("adb shell input keyevent 26")
# os.system("adb shell input keyevent 26")
#
# os.system("adb shell input swipe 540 1280 541 480")
# os.system("adb shell input swipe 540 480 541 1280")
# os.system("adb shell input swipe 540 1280 541 480")
# os.system("adb shell input swipe 540 1280 541 480")
# // 模拟back键
# os.system("adb shell input keyevent 3")
# os.system("adb shell input swipe 360 960 960 961")
# os.system("adb shell input swipe 960 960 360 961")
# // 模拟Home键1
# os.system(("adb shell input keyevent 3")