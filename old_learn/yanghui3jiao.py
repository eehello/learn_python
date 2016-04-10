#!/usr/bin/env python3.4
#-- coding: utf-8 --

n=int(input("请输入你想要的层数："))
if n>2 :
    pn=[([0]*(n+1)) for i in range(n+1)]
    pn[1][1]=1
    pn[2][1]=1
    pn[2][2]=1
    print(pn[1][1])
    print(pn[2][1]),
    print(pn[2][2])
    for x in range(3,(n+1)):
        pn[x][1]=1
        print(pn[x][1]),
        for y in range(2,x):
            pn[x][y]=pn[x-1][y-1]+pn[x-1][y]
            print(pn[x][y]),
        pn[x][x]=1
        print(pn[x][x])
else :
    print("请输入大于2层")
