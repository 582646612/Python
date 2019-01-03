from urllib import request
px=request.ProxyHandler({'http':'114.237.63.77:3681'})#这里就是代理ip和端口
opener=request.build_opener(px)
req=request.Request("https://www.zhihu.com")#这里是你要爬的链接
res=opener.open(req)
result=res.readlines()
print(result)
