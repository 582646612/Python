str_1 = 'abccdef'
#将字符串转换为list列表
lst = list(str_1)
#对列表进行反转操作,reverse()返回为None
lst.reverse()
print(''.join(lst))
print(str_1[::-1])
for i in range(len(str_1)-1,-1,-1):
    print(str_1[i],end='')