#!/usr/bin/env python
# coding=utf-8
# Copyright © 2016 ldf@eehello.com All Rights Reserved
# 本程序在python3.4下测试通过

ok = []
name_dict = {}

search_name = str(input('请输入你要查询的用户:'))

if search_name == 'q':
    exit()

f_name = open('name_list.cfg', 'r')

for name in f_name:
    #print(name)
    name = name.strip().split(':')
    name_dict[name[0]] = name[1]
    if search_name in name[0]:
        ok.append(name[0])

f_name.close()

print('符合查询条件有%d位\n 分别为:' % len(ok))

for i in ok:
    print('\033[31;1m%s\033[0m:%s' % (i, name_dict[i]))

