#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

def triangles(max):
    n=0
    N = [1]
    while n < max:
        yield N
        N.append(0)
        N = [N[i - 1] + N[i] for i in range(len(N))]
        # l = [1] + [l[i] + l[i + 1] for i in range(len(l) - 1)] + [1]
        n = n + 1
f = triangles(10)
print('fib(10):', f)
for x in f:
    print(x)