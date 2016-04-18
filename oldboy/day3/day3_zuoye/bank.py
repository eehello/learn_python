#!/usr/bin/env python
# coding=utf-8
'''
# @Created on : 2016/04/17 11:37
# @Author     : ldf (ldf@eehello.com)
# @Link       : http://www.eehello.com
# @Version    : 
# 本程序在python2.7下测试通过
'''
import pickle
from backgroud import jiami
ka = []
with open('backgroud/kami.cfg', 'rb') as fa:
    ka = pickle.load(fa)

print('欢迎登录网上银行系统！')
print('-------------------------------------')

kahaomima = []
yanzheng = False
count = 0
while count < 3:
    ka1 = []
    kahao = input('请输入您的银行卡卡号：')
    mima = jiami.jiami_md5(raw_input('请输入您的银行卡密码：'))
    ka1.append(kahao)
    ka1.append(mima)

    with open('backgroud/lock.cfg', 'rb') as fl:
        for i in fl:
            if ka1[0] == int(i.strip()):
                print('您的卡号已被锁，请联系银行解锁！')
                exit()

    for i in ka:
        if ka1[0] == i[0] and ka1[1] == i[1]:
            yanzheng = jiami.jiami_md5('tongguo')
    if yanzheng == jiami.jiami_md5('tongguo'):
        kahaomima = ka1
        break
    count += 1
    if count < 3 and yanzheng == False:
        print('您的输入有误，请重新输入！')
    if count ==3 and yanzheng == False:
        with open('backgroud/lock.cfg', 'ab') as fl:
            fl.write(str(ka1[0])+'\n')
        print('您的输入错误次数太多，此卡号已被临时冻结！')



if yanzheng == jiami.jiami_md5('tongguo'):
    kahao = str(kahaomima[0])
    print(
        '''
        欢迎您登录网上银行系统！
        您的卡号为：%s
        1：取现
        2：查询
        3：还款
        4：转账
        5：退出
        '''
    % (kahao[0]+kahao[1]+'***'+kahao[-2]+kahao[-1])
    )

yewu = {1:'quxian',2:'chaxun',3:'huankuan',4:'zhuanzhang',5:'tuichu'}

shuru = int(input('请选择您要办理的业务：'))
for i in range(1,6):
    if i == shuru:
        model01 = __import__('backgroud.'+yewu[shuru])
        func1 = getattr(model01,yewu[shuru])
        func1.run()
