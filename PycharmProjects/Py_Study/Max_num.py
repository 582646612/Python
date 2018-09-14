#!/usr/bin/env python3
# -*- coding: utf-8 -*-
num1 = input()
num2 = input()
def Max_num(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a
result = Max_num(num1,num2)
print (result)