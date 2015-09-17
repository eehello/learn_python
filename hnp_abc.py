#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def move(n,A,B,C):
    if n==1:
        print(A,'-->',C)
    else:
        move(n-1,A,C,B)
        move(1,A,B,C)
        move(n-1,B,A,C)
n=int(input("请输入汉诺塔的层数："))
move(n,'A','B','C')
