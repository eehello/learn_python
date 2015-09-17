#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(max):
    n=0
    a=0
    b=1
    while n<max:
        print(b)
        a, b=b,a+b
        n=n+1
    return 'done'
max=int(input("请输入斐波那契数列数:"))
f=fib(max)
print(f)
