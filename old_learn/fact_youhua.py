#! /usr/bin/env python3
# -*- coding:utf-8 -*-
def fact(n): 
    return fact_youhua(n,1)

def fact_youhua(n,num):
    if n==1:
        return num
    return fact_youhua(n-1,num=num*n)    

n=int(input("请输入你想阶乘的值："))
print(fact(n))
