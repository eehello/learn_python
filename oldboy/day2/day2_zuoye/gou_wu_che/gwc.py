#!/usr/bin/env python
# coding=utf-8
# Copyright © 2016 ldf@eehello.com All Rights Reserved
# 本程序在python3.4下测试通过
shops = {'tv':3000,'iphone':5000,'tea':10,'move':35,'spring':1200,
         'fangte':200,'shopping':500}

gongzi = int(input('请输入你的工资：'))

buys = []
min_shop = gongzi

while gongzi >= min_shop:
    print('物品清单为：')
    shops_value = []
    for i in shops:
        print('物品:%s,价格为:%d元' % (i,shops[i]))
        shops_value.append(shops[i])
    print('----------------------------------------------------------')
    print('你的可用金额为：',gongzi)
    min_shop = min(shops_value)
    buy = str(input('请输入你想购买的物品名称(退出请按字母 q ):'))
    if buy == 'q':
        exit()
    gongzi = gongzi - shops[buy]
    buys.append(buy)

print('你购买了如下产品:')
for i in buys:
    print(i)
print('你的余额为:%d' % gongzi)
