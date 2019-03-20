#!/usr/bin/env python
# coding=utf-8


filename = 'test\pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())