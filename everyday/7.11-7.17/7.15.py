#!/usr/bin/env python3
# coding=utf-8
"""
# @Created on : 2019/07/15 14:44
# @Author     : ldf (ldf@eehello.com)
# @Link       : http://www.eehello.com
# @Version    : 
# 本程序在python3.4下测试通过
"""


def sum(a=1,b=2):
    return a+b

def sum_max(aaa):
    sumxx = 0
    for i in aaa:
        sumxx = sumxx + i
    return sumxx

def sum_xx(*bbb):
    sumyy = 0
    for i in bbb:
        sumyy += i
    return sumyy

a1 = input("请输入第一个数字：")
a2 = input("请输入第二个数字：")

print("函数默认计算的和为：",sum())
print("两数和为：",sum(int(a1),int(a2)))

print("计算任意个数字和：")

abc = []
while 1:
    aa = input("请输入任意一个数字(退出请按q)：")
    if aa == 'q':
        break
    abc.append(int(aa))


print("计算的和为：",sum_max(abc))


print(sum_xx(2,2,2))