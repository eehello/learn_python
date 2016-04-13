#!/usr/bin/env python
# coding=utf-8
pass_file = open('password.txt', 'r')
for line in pass_file.readline():
    #    line = line.strip('\n')
    print line
    print 'test'
