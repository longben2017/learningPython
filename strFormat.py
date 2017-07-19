#!/usr/bin/python
#coding:utf-8

#使用给定的宽度打印格式化后的价格列表

width = input('Please enter width: ')

#物品和价格之间的宽度
price_width = 10
#物品前面的宽度
item_width = width -price_width

#'-'代表左对齐，只要输入的宽度大于32(最长的物品宽度为22+price_width宽度10)，表格就会对齐
#'*'代表星号运算符，可从转换元组中读取
header_format = '%-*s%*s'
format = '%-*s%*.2f'

print '=' * width

print header_format % (item_width,'Item',price_width,'Price')

print '-' * width

print format % (item_width,'Apples',price_width,0.4)
print format % (item_width,'Pears',price_width,0.5)
print format % (item_width,'Cantaloupes',price_width,1.92)
print format % (item_width,'Dried Apricots(16 oz.)',price_width,8)
print format % (item_width,'Prunes(4 lbs.)',price_width,12)

print '=' * width
