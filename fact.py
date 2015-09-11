#! /usr/bin/env python3
# -*- coding:utf-8 -*-
def fact(n):
    if n==1:
        return 1
    return n* fact(n-1)
n=int(input("请输入想阶乘的数值"))
print(fact(n))
