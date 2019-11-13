# 导入AES模块
from Cryptodome.Cipher import DES #pycryptodome
import binascii
from Cryptodome.Cipher import AES
from Cryptodome import Random
from binascii import b2a_hex
class Aes():
    def __init__(self):
        # 密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.
        # 目前AES-128足够用
        self.key = b'this is a 16 key'
        self.iv = Random.new().read(AES.block_size)
    def jiami(self,text):
        # 生成长度等于AES块大小的不可重复的密钥向量

        # 使用key和iv初始化AES对象, 使用MODE_CFB模式
        mycipher = AES.new(self.key, AES.MODE_CFB, self.iv)
        # 加密的明文长度必须为16的倍数，如果长度不为16的倍数，则需要补足为16的倍数
        # 将iv（密钥向量）加到加密的密文开头，一起传输
        self.ciphertext = self.iv + mycipher.encrypt(text.encode())

        return b2a_hex(self.ciphertext)

    def jiemi(self,text):
        encrypto_text = binascii.a2b_hex(text)
        mydecrypt = AES.new(self.key, AES.MODE_CFB, encrypto_text[:16])
        decrypttext = mydecrypt.decrypt(encrypto_text[16:])
        return decrypttext.decode()

if __name__ == '__main__':

    a=Aes()
    b=a.jiami('123')
    print(b.decode())
    c=Aes().jiemi('aa73c17f70b62da34018a79952cbd67b7be04c35bac9')
    print(c)