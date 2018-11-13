#!/usr/bin/python
# -*- coding: UTF-8 -*-

# str = input("请输入：")
# print ("你输入的内容是: ", str)
'''input([prompt]) 函数和 raw_input([prompt]) 
函数基本类似，但是 input 可以接收一个Python表达式作为输入，
并将运算结果返回。'''
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))