#!/usr/bin/env python3
#coding:utf-8

'''
Mainly practicing sorted() usage.

'''


L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

L1 = sorted(L,key=by_name)
L2 = sorted(L,key=by_score)
print('sort by name:',L1)
print('sort by score:',L2)
