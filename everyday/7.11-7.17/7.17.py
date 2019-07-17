#!/usr/bin/env python3
# coding=utf-8
"""
# @Created on : 2019/07/17 15:18
# @Author     : ldf (ldf@eehello.com)
# @Link       : http://www.eehello.com
# @Version    : 
# 本程序在python3.4下测试通过
"""



list01 = [1,2,3,4,5]
print("列表第三个元素为：",list01[2])
list01.append(6)
print(list01)
del list01[0]
print(list01)
print(list01[-1])
list02 = list01[0:3]
print(list02)
