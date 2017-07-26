#!/usr/bin/python
#coding:utf-8

#find_mails.py
#usage:python find_mails.py message.eml

import fileinput,re

pat = re.compile(r'[0-9a-z\-\.]+@[0-9a-z\-\.]+',re.IGNORECASE)
addresses = set()
for line in fileinput.input():
	for address in pat.findall(line):
		addresses.add(address)
for address in sorted(addresses):
	print address
