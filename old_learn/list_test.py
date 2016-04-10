#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list001=range(101)

a=0
n=int(input("请输入准备取前几个数："))
list002=[]
while a<n:
    list002.append(list001[a])
    a=a+1
print(list002)
