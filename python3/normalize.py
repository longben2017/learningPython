#!/usr/bin/env python3
#coding:utf-8

'''
Make these wrong English Names correct.

Mainly practicing map() usage.
'''

def normalize(name):
    return name.capitalize()

L1 = ['adam','LISA','barT']
L2 = list(map(normalize,L1))
print(L2)
