#!/usr/bin/env python3
#coding:utf-8

'''
Make the string type to float type.

Mainly practicing map() and reduce() usage.
'''

from functools import reduce

def str2float(s):
    def func(x,y):
        return x*10+y
    def cd(a):
        return {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0,'.':'d'}[a]

    L=list(map(cd,s))
    i=L.index('d')
    L.pop(i)
    return float(reduce(func,L)/pow(10,i))#pow(x,y) mean x^y 

print('str2float(\'123.456\')=',str2float('123.456'))
