#!/usr/bin/python
#coding:utf-8

#util.py

#在文件的最后追加一个空行
def lines(file):
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
