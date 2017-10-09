#!/usr/bin/env python
#coding:utf-8

import requests
from lxml import etree

def gethtml(url):
    content = requests.get(url).content
    html = etree.HTML(content)
    nodes = html.xpath('//ul[@class="list-recent-events menu"]/li')
    for node in nodes:

        # 会议时间
        time = node.xpath('p/time/text()')

        # 会议主题
        zt = node.xpath('h3[@class="event-title"]/a/text()')

        # 会议地点
        address = node.xpath('p/span[@class="event-location"]/text()')

        data = {
        '会议时间':time,
        '会议主题':zt,
        '会议地点':address
        }
        print(data)

if __name__ == '__main__':
    gethtml('https://www.python.org/events/python-events/')

