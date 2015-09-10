#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import math
def quadratic(a,b,c):
    b1=float(b*b - 4*a*c)
    b2=float(math.sqrt(b1))
    x1=(-b + b2)/(2*a)
    x2=(-b - b2)/(2*a)
    return x1, x2
w1=int(input("请输入a的值:"))
w2=int(input("请输入b的值:"))
w3=int(input("请输入c的值:"))
f_ac=(w2*w2-4*w1*w3)
if  f_ac > 0:
    x, y = quadratic(w1,w2,w3)
    print("一元二次方程的一个解为：%f ,另一个解为：%f 。" % (x,y))
else :
    print("b*b-4*a*c不大于0")
