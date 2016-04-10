#!/usr/bin/env python
# -*- coding: utf-8 -*-
sum=1
n=int(input("请输入需要阶乘的数："))
n=n+1
for x in range(n):
    if x==0:
        pass
    else:
        sum=sum*x
print(sum)
