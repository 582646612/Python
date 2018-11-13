#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1

L = range(100)

print(list(filter(is_odd, L)))

def not_empty(s):
    return s and s.strip()
# s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))