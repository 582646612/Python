#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

natuals = itertools.count(1)
print(natuals)
for n in natuals:
    print(n)
    if n >= 5:
        break

cs = itertools.cycle('ABC')
print(cs)
t = 5
for c in cs:
    print(c)
    t = t - 1
    if t == 0:
        break
