#!/usr/bin/env python
# coding=utf-8
# Copyright © 2016 ldf@eehello.com All Rights Reserved
# 本程序在python3.4下测试通过
shops = {'tv':3000,'iphone':5000,'tea':10,'move':35,'spring':1200,
         'fangte':200,'shopping':500}

gongzi = int(input('请输入你的工资：'))

print('物品清单为：')
for i in shops:
    print('物品',i,',价格为：',shops[i],'元')
print('你的可用金额为：',gongzi)
