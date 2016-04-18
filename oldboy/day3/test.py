#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#################################################
# @Created on : 2016.04.15
# @Author     : ldf (ldf@eehello.com)
# @Link       : http://www.eehello.com
# @Version    :
# 本程序在python2.7下测试通过
#################################################
'''
'''
print(__name__)
print(__file__)
print(__doc__)


def abc(name, where='pds', action='job'):
    print(name,where,action)

abc('ldf',action='it')

def show(**arg):
    for item in arg.items():
        print(item)

show(name='ldf',job='it')
def show1(*arg):
    for item in arg:
        print(item)

a = [222,333,555]
show1([123,4566])

show1(*a)

'''
# print(range(10))
# print(xrange(10))
'''
def foo():
    yield 1

re = foo()
print(re)

a = []
print(dir())
print(vars())

def a():
    yield 1

for x in a():
    print(x)


from day2 import test
from day2 import test
reload(test)



t1 = 123
t2 = 124
print id(t1)
print id(t2)

def foo(arg):
    if arg<22:
        return True
    else:
        return False

li = [11,22,33]

temp = filter(foo,li)
print temp
'''

'''
验证码生成函数：

import random

def random_yzm():
    a = []
    for i in range(4):
        if i == random.randint(0, 3):
            a.append(str(random.randint(0, 9)))
        else:
            a.append(chr(random.randint(65, 90)))

    return ''.join(a)


print(random_yzm())
'''
'''
md5加密函数：
def md5_jm(arg):
    import hashlib
    jm = hashlib.md5()
    jm.update(arg.encode('utf-8'))
    return jm.hexdigest()

a = md5_jm('admin')
print(a)
'''
with open('test003.cfg', 'wb') as f1:
    f1.write('test003')
