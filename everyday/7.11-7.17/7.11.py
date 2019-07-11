#!/usr/bin/env python
# coding=utf-8
"""
# @Created on : 2019/07/11 20:41
# @Author     : ldf (ldf@eehello.com)
# @Link       : http://www.eehello.com
# @Version    : 
# 本程序在python3.7下测试通过
"""


print("这是一个处理坐标象限的小程序！")
pd_x = int(input("请输入X坐标："))
pd_y = int(input("请输入Y坐标："))

if pd_x > 0:
    if pd_y > 0:
        print("此坐标点位于第一象限")
    elif pd_y < 0:
        print("此坐标点位于第四象限")
    else:
        print("此坐标点位于X轴右部")
elif pd_x < 0:
    if pd_y > 0:
        print("此坐标点位于第二象限")
    elif pd_y < 0:
        print("此坐标点位于第三象限")
    else:
        print("此坐标点位于X轴左部")
else:
    if pd_y > 0:
        print("此坐标点位于Y轴上部")
    elif pd_y < 0:
        print("此坐标点位于Y轴下部")
    else:
        print("此坐标点位于原点")