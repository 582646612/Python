#coding:utf_8
list1 = ['chemistry', 1997, 1997,1997, 1997,2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

list1.append('Google')   ## 使用 append() 添加元素
del list1[2]#删除

print (len(list2))
print (max(list2))
print (min(list2))
print (list1.insert(1997,1))

'''list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素'''