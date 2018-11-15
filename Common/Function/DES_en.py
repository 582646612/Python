from Crypto.Cipher import DES
import base64
import binascii

class Crypt():
    def __init__(self):
        self.key= b'abcdefgh'
    def encypt(self, s):

        # 需要去生成一个DES对象
        des = DES.new(self.key, DES.MODE_ECB)
        # 需要加密的数据
        text =s
        text = text + (8 - (len(text) % 8)) * '='
        # 加密的过程
        encrypto_text = des.encrypt(text.encode())
        encrypto_text = binascii.b2a_hex(encrypto_text)
        return encrypto_text

    def descypt(self, s):
        # 解密
        cipherX = DES.new(self.key, DES.MODE_CBC)
        bytedt = base64.b64decode(s)
        y = cipherX.decrypt(bytedt)
        return str(y, 'UTF-8').strip('\0')

if __name__ == '__main__':

    obj = Crypt()
    a = obj.encypt("test")
    print(a)



