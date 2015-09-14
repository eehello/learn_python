#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sum(n):
    if n==1:
        return 1
    return 2*sum(n-1)+1

n=int(input("请输入盘子数："))
print(sum(n))
