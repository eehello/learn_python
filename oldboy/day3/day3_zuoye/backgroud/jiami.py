#!/usr/bin/env python
# coding=utf-8
'''
# @Created on : 2016/04/17 14:51
# @Author     : ldf (ldf@eehello.com)
# @Link       : http://www.eehello.com
# @Version    : 
# 本程序在python2.7下测试通过
'''
#import pickle
# md5加密函数：

def jiami_md5(arg):
    import hashlib
    jm = hashlib.md5()
    jm.update(arg.encode('utf-8'))
    return jm.hexdigest()

'''
ka1 = jiami_md5('pds12345')
ka2 = jiami_md5('pds1234')
ka = [[110001,ka1],[110002,ka2]]
with open('kami.cfg','wb') as fb:
    pickle.dump(ka,fb)
'''
