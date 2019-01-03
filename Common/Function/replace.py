import re
s='所在区域五华\xa0顺城\xa0'
s.replace('\xa0','')
print(s)
x=re.sub('\xa0','',s)
print(x)