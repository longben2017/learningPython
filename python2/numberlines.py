#!/usr/bin/python                                           
#coding:utf-8                                               
                                                            
#numberlines.py                                                                 #usage:python numberlines.py numberlines.py                               
import  fileinput                                           
                                                            
for line in fileinput.input():                  
	line = line.rstrip()                                       
	num = fileinput.lineno()                                   
	print '%-60s # %2i' % (line,num)                           
