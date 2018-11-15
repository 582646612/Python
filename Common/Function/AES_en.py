from Crypto.Cipher import AES
import base64
import json

class Crypt:
    def __init__(self):
        self.key = '0123456789123456'  # 只截取16位
        self.iv = '2015030120123456'  # 16位字符，用来填充缺失内容，可固定值也可随机字符串，具体选择看需求。
        self.mode = AES.MODE_CBC

    def __pad(self, text):
        """填充方式，加密内容必须为16字节的倍数，若不足则使用self.iv进行填充"""
        text_length = len(text)
        amount_to_pad = AES.block_size - (text_length % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        pad = chr(amount_to_pad)
        return text + pad * amount_to_pad

    def __unpad(self, text):
        pad = ord(text[-1])
        return text[:-pad]

    def encrypt(self, raw):
        """加密"""
        raw = self.__pad(raw)
        cipher = AES.new(str.encode(self.key), self.mode, str.encode(self.iv))
        #  msg=cipher.encrypt(str.encode(raw))
        return base64.b64encode(cipher.encrypt(str.encode(raw)))

    def decrypt(self, enc):
        """解密"""
        enc = base64.b64decode(enc)
        cipher = AES.new(str.encode(self.key), self.mode, str.encode(self.iv))
        return self.__unpad(cipher.decrypt(enc).decode("utf-8"))


if __name__ == '__main__':
    # aa = Crypt()
    # pp = aa.encrypt('aaa')
    #
    #  # byte转换string
    # print(pp.decode())
    #
    # jm = aa.decrypt(b'V0kstm7NjgzpNGzKbZZ2mg==')
    # print(jm)
    text="aaa"
    text_length = len(text)
    amount_to_pad = AES.block_size - (text_length % AES.block_size)
    if amount_to_pad == 0:
        amount_to_pad = AES.block_size
    pad = chr(amount_to_pad)
    print(pad)
    print(text)
    print(amount_to_pad)
    print(type(text + pad * amount_to_pad))
