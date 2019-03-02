#!/usr/bin/env python
# coding=utf-8
"""
# @Created on : 2019/03/02 17:54
# @Author     : ldf (ldf@eehello.com)
# @Link       : http://www.eehello.com
# @Version    : 
# 本程序在python2.7下测试通过
"""

def greet_user():
    """显示简单的问候语"""
    print("Hello!")

def greet_user001(username):
    print("Hello, "+ username.title() + "!")

greet_user001("df")
