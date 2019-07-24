import cv2 #pip install opencv-python
from PIL import Image
def cut_photo():
    img = cv2.imread(r'D:\Project\python\Working\qudao_system\photo\1.png')
    cropped = img[538:568,975:1065]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite(r'D:\Project\python\Working\qudao_system\photo\1.jpg', cropped)

def cut_picture():
    rangle = (975,538,975+90,538+30)  #计算验证码整体坐标
    photo = Image.open(r'D:\Project\python\Working\qudao_system\photo\1.png')
    frame4=photo.crop(rangle)   #截取验证码图片
    frame4.save(r'D:\Project\python\Working\qudao_system\photo\1.jpg')