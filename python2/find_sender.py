#!/usr/bin/python
#coding:utf-8

#find_sender.py
#usage:python find_sender.py message.eml

import fileinput,re

pat = re.compile('From:(.*)<.*?>$')
for line in fileinput.input():
	m = pat.match(line)
	if m: print m.group(1)
