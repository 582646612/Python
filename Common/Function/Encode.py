import hashlib,random
import base64
import binascii
from urllib import parse
import hmac
def hmacc(message):
    key = b'secret'
    h = hmac.new(key, message.encode('utf-8'), digestmod='MD5')
    # 如果消息很长，可以多次调用h.update(msg)
    return h.hexdigest()
def sha1(str):
    sha1 = hashlib.sha1()
    sha1.update(str.encode('utf-8'))
    print(sha1.hexdigest())
def md5(str):
    # hashlib.new('md5', b'123').hexdigest()
    # 创建md5对象
    hl = hashlib.md5()

    # 此处必须声明encode
    # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()
if __name__ == '__main__':
    password='123456'
    salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
    password = md5(password + salt)
    print(md5("这是一个测试"))
    print(sha1('这是一个测试'))
    print(hmacc("这是一个测试"))

    print('南北'.encode())
    print(b'\xe5\x8d\x97\xe5\x8c\x97'.decode())

    print(binascii.b2a_hex('南北'.encode()))
    print(binascii.a2b_hex(b'e58d97e58c97').decode())

    print(parse.quote('南北'))           #网址
    print(parse.unquote('%E5%8D%97%E5%8C%97'))

    print(base64.b64encode(b'hello world'))
    print(base64.b64decode(b'aGVsbG8gd29ybGQ='))
