#-*-coding:utf-8-*-
import  os
import pytesseract
from PIL import Image, ImageDraw
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
def localos():
    curpath = os.path.dirname(__file__)
    return curpath
#调用识别验证码
def get_yzm():
    localadd = localos() + '/photo/'
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

if __name__ == '__main__':
    yzm=get_yzm()
    while len(yzm)!=4:
        yzm=get_yzm()
    print(yzm)