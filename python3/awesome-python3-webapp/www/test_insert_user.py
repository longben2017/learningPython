#!/usr/bin/env python
# -*-coding:utf-8-*-

__author__ = 'longben2017'

import sys
import orm,asyncio
from models import User,Blog,Comment

@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(
        loop=loop,
        user='root',
        password='engine',
        db='awesome'
    )
    u = User(
        name='Test',
        email='test1@example.com',
        passwd='1234567890',
        image='about:blank'
    )
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()