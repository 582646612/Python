import uuid
import socket
mac=uuid.UUID(int=uuid.getnode()).hex[-12:]#MAC地址
for e in range(0,11,2):
    print(":".join([mac[e:e+2]]))
myname=socket.getfqdn(socket.gethostname())#本机电脑名
myaddr=socket.gethostbyname(myname)#本机ID
print(myname)
print (myaddr)