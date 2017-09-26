#!/usr/bin/env python3
#coding:utf-8

'''
To determine whether a number is palindrome.

Mainly practicing filter() usage.
'''

def is_palindrome(n):
    return str(n) == str(n)[::-1]#str(n)[::-1]意为把n转换为字符串，并反向取值，是python分片的用法

output = filter(is_palindrome,range(1,150))
print(list(output))
