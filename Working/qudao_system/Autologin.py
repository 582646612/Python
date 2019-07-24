import cv2  #pip install opencv-python
import yaml
import time
import  os
import pytesseract
import warnings
from time import sleep
from selenium import webdriver
from PIL import Image, ImageDraw
warnings.filterwarnings("ignore", category=Warning)#警告不显示
#读取yaml用户名密码文件
def get_namepwd():
    f = open("namepwd.yaml", 'r',encoding='utf8')
    np = f.read()
    d = yaml.load(np)
    return d
#cookies写入文件
def write_cooks(conten):
    with open("cooks.txt", "w") as fout:
        fout.write(conten)
        print(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()), end=' ')
        print("Cookies写入成功")
        fout.close()
#不同地名返回对应用户名，密码
def trans_city(city):
    if city=='怒江':
        return 'CIS.NJ_USER','CIS.NJ_PASSWORD'
    elif city=='保山':
        return 'CIS.BS_USER', 'CIS.BS_PASSWORD'
    elif city=='昆明':
        return 'CIS.KM_USER', 'CIS.KM_PASSWORD'
    elif city=='临沧':
        return 'CIS.LC_USER', 'CIS.LC_PASSWORD'
    elif city=='丽江':
        return 'CIS.LJ_USER', 'CIS.LJ_PASSWORD'
    elif city=='曲靖':
        return 'CIS.QJ_USER', 'CIS.QJ_PASSWORD'
    elif city=='昭通':
        return 'CIS.ZT_USER', 'CIS.ZT_PASSWORD'
    elif city=='玉溪':
        return 'CIS.YX_USER', 'CIS.YX_PASSWORD'
    elif city=='普洱':
        return 'CIS.PE_USER', 'CIS.PE_PASSWORD'
    elif city=='楚雄':
        return 'CIS.CX_USER', 'CIS.CX_PASSWORD'
    elif city=='版纳':
        return 'CIS.BN_USER', 'CIS.BN_PASSWORD'
    elif city=='德宏':
        return 'CIS.DH_USER', 'CIS.DH_PASSWORD'
    elif city=='大理':
        return 'CIS.DL_USER', 'CIS.DL_PASSWORD'
    elif city=='红河':
        return 'CIS.HH_USER', 'CIS.HH_PASSWORD'
    elif city=='文山':
        return 'CIS.WS_USER', 'CIS.WS_PASSWORD'
    elif city=='迪庆':
        return 'CIS.DQ_USER', 'CIS.DQ_PASSWORD'
#不同用户返回不同菜单
def menu_city(city):
    if city=='怒江' or city=='保山' or city=='丽江' or city=='昭通' or city=='玉溪' or city=='德宏' or city=='文山' or city=='迪庆':
        return '5'
    elif city=='曲靖' or city=='普洱' or city=='楚雄' or city=='红河':
        return '4'
    elif city=='临沧' or city=='版纳' or city=='大理':
        return '3'
#图片预处理
def test(path):
    img=Image.open(path)
    w,h=img.size
    for x in range(w):
        for y in range(h):
            r,g,b=img.getpixel((x,y))
            if 190<=r<=255 and 170<=g<=255 and 0<=b<=140:
                img.putpixel((x,y),(0,0,0))
            if 0<=r<=90 and 210<=g<=255 and 0<=b<=90:
                img.putpixel((x,y),(0,0,0))
    img=img.convert('L').point([0]*150+[1]*(256-150),'1')
    return img
# 图片二值化
t2val = {}
def twoValue(image, G):

    for y in range(0, image.size[1]):
        for x in range(0, image.size[0]):
            g = image.getpixel((x, y))
            if g > G:
                t2val[(x, y)] = 1
            else:
                t2val[(x, y)] = 0
#降噪处理
def clearNoise(image, N, Z):
    for i in range(0, Z):
        t2val[(0, 0)] = 1
        t2val[(image.size[0] - 1, image.size[1] - 1)] = 1

        for x in range(1, image.size[0] - 1):
            for y in range(1, image.size[1] - 1):
                nearDots = 0
                L = t2val[(x, y)]
                if L == t2val[(x - 1, y - 1)]:
                    nearDots += 1
                if L == t2val[(x - 1, y)]:
                    nearDots += 1
                if L == t2val[(x - 1, y + 1)]:
                    nearDots += 1
                if L == t2val[(x, y - 1)]:
                    nearDots += 1
                if L == t2val[(x, y + 1)]:
                    nearDots += 1
                if L == t2val[(x + 1, y - 1)]:
                    nearDots += 1
                if L == t2val[(x + 1, y)]:
                    nearDots += 1
                if L == t2val[(x + 1, y + 1)]:
                    nearDots += 1

                if nearDots < N:
                    t2val[(x, y)] = 1
#保存图片
def saveImage(filename, size):
    image = Image.new("1", size)
    draw = ImageDraw.Draw(image)
    for x in range(0, size[0]):
        for y in range(0, size[1]):
            draw.point((x, y), t2val[(x, y)])
    image.save(filename)
#识别图片验证码
def recognize_captcha(img_path):
    im = Image.open(img_path)
    num = pytesseract.image_to_string(im)
    # 去掉识别结果中的特殊字符
    exclude_char_list = ' .:\\|\'\"?![],()~@#$%^&*_+-={};<>/¥'
    num = ''.join([x for x in num if x not in exclude_char_list])
    return num
#剪切图片
def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)
#获取当前目录
def local_os():
    curpath = os.path.dirname(__file__)
    return curpath+'/photo/'
#调用函数识别验证码
def get_yzm():
    localadd = local_os()
    image_path = localadd + '1.jpg'
    file_out = localadd + '1.jpg'
    produceImage(image_path, 240, 80, file_out)
    im = test(image_path)
    path = image_path.replace('jpg', 'png')
    im.save(path)
    image = Image.open(path).convert("L")
    twoValue(image, 100)
    clearNoise(image, 3, 2)
    path1 = localadd + '1.jpeg'
    saveImage(path1, image.size)
    res = recognize_captcha(path1)
    return res
#判断是否在登录界面
def boollogin(driver):
    try:
        if driver.find_element_by_id('B1').size != '':
            return 1
    except:
        return 0
#登录
def get_cookie(name,pwd,menu):
    print(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()), end=' ')
    print("开始运行,正在打开浏览器……")
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://10.123.0.126:18010/CIS-SSF/login")
    login_bool = boollogin(driver)
    local_add= local_os()
    while login_bool == 1:
        driver.get("http://10.123.0.126:18010/CIS-SSF/login")
        driver.implicitly_wait(3)
        driver.find_element_by_id("username").send_keys(name)
        driver.find_element_by_id("password").send_keys(pwd)
        yzm = ''
        print(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()), end=' ')
        print("正在识别验证码……")
        while len(yzm) != 4:
            driver.find_element_by_xpath('/html/body/div/div[2]/form/table/tbody/tr[4]/td[2]/a/img').click()
            driver.save_screenshot(local_add+'login.png')
            img = cv2.imread(local_add+'login.png')
            cropped = img[538:568, 975:1065]  # 裁剪坐标为[y0:y1, x0:x1]
            cv2.imwrite(local_add+'1.jpg', cropped)
            yzm = get_yzm()
        driver.find_element_by_id("captchaResponse").send_keys(yzm)
        driver.find_element_by_id("B1").click()
        login_bool = boollogin(driver)
    try:
        driver.find_element_by_xpath("//*[@id='keepOnForm']/div[2]/div/div[2]/div[2]/ul/li[1]/a").click()
        print(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()), end=' ')
        print("登录成功1")
    except :
        print(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()), end=' ')
        print("登录成功2")
    sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li["+menu+"]").click()
    driver.find_element_by_xpath("/html/body/div[3]/div[3]/ul/li[3]").click()
    driver.find_element_by_xpath("/html/body/div[3]/div[3]/ul/li[3]").click()
    driver.switch_to.frame("_iFrameLeft")
    driver.find_element_by_id("smenuTreeSys1").click()
    sleep(1)
    driver.get('http://10.123.0.126:18210/CIS-CHAR')
    driver.implicitly_wait(3)
    result = driver.get_cookies()
    cook=result[0]['value']
    print(time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()), end=' ')
    print("cookies为：",cook)
    write_cooks(cook)
    driver.quit()
if __name__ == '__main__':
    tity='文山'       #更换不同地市
    info=get_namepwd()
    cities = trans_city(tity)
    menu=menu_city(tity)
    name,password=info[cities[0]],info[cities[1]]
    get_cookie(name,password,menu)