import rsa

# 生成密钥
(pubkey, privkey) = rsa.newkeys(1024)

# 保存密钥

x=pubkey.save_pkcs1().decode()

y=privkey.save_pkcs1().decode()


print(x)
print(y)
# 导入密钥
pubkey = rsa.PublicKey.load_pkcs1(x.encode())


privkey = rsa.PrivateKey.load_pkcs1(y.encode())

# 明文
message = 'hello'

# 公钥加密
crypto = rsa.encrypt(message.encode(), pubkey)

# 私钥解密
message = rsa.decrypt(crypto, privkey).decode()
print(message)

print(crypto)


# 私钥签名
signature = rsa.sign(message.encode(), privkey, 'SHA-1')

# 公钥验证
rsa.verify(message.encode(), signature, pubkey)

print(signature)
