#-*- coding: utf-8 -*
'''
Author:         wanghe 
Email:          wangh@loginsight.cn
Author website: 
 
File: a.py
Create Date: 2016-03-15 22:42:00
''' 

from raven import Client

client = Client('http://b08759ac646040a5a80fbb9d7a528443:77f909bcccd04878b78fe414573441ed@localhost:9000/6')

try:
        1 / 0
except ZeroDivisionError:
        client.captureException()


