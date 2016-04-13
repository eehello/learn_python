#!/usr/bin/env python
# coding=utf-8
print '欢迎访问系统！请在下面输入您的账号密码以进入系统！'
count = 0
name_file = open('name.txt', 'r')

while count < 3:
    count += 1
    name = raw_input('请输入你的用户名：')
    password = raw_input('请输入你的密码:')
    lock_file = open('lock.txt', 'r')
    for lock_name in lock_file:
        if name == lock_name.strip():
            print 'You name is locked!'
            count = 5
            break
    for name_zq in name_file:
        n_p =  name_zq.strip('\n').split(':')
        if name == n_p[0] and password == n_p[1]:
#                print 'password is true'
                print 'You are right!'
                count = 5
        break

    else:
                print '输入错误'
    if count ==5 :
        break
        
#if count !=5 :
else:
    lock_file.close()
    print 'You are wrong fuck! You lock!'
    lock_file = open('lock.txt', 'a')
#    locked = name+'\n'
    lock_file.write(name+'\n')

name_file.close()
lock_file.close()
