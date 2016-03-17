# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: tarantool_client.py
time   : 16/3/17 下午1:20
"""

"""
    需要 安装　tarantool 客户端，　也许需要最新版
    pip install git+https://github.com/tarantool/tarantool-python.git@master

    Usage:
    python mock/client.py -H <localhost> －k <token>　-s <stream_key> -rate <lps> log_file

    -H      要发送到的主机
    -s      日志文件的stream_key
    -rate   发送日志的条数(每秒)，　默认为　０　不限制
    logfile 要发送的日志文件

"""

import os
import tarantool
import argparse
import random
import time


class TarantoolClient(object):
    server = None

    def __init__(self, host='localhost', port=12801):
        self.server = tarantool.connect(host, port)

    def authenticate(self, host_key):
        username = "host%s" % host_key[:12]
        password = host_key[12:]
        self.server.authenticate(username, password)

    def sync_host_key(self, host_key):
        self.server.call('command_sync', host_key)


    """
    param: stream = {
            'stram_key': 'xxxx',
            'stream_type': 'xxxx',
            'file_status': {
                'filename': 'xxx',
                'file_dir': 'xxxx'
            },
            'file_tags': ['xxx', 'xxx', 'xxx']
        }
    """
    def stream_start(self, stream):
        print 'ssss'
        return self.server.call('command_stream_start', stream['stream_key'], stream['stream_type'],
                                      stream['file_status'], stream['file_tags'])

    def switch_stream(self, space_id=0, stream_id=0):
        self.server.insert(space_id, ['sem', stream_id])

    def insert(self, space_id, stream_id, data):
        self.server.insert(space_id, ['dat', 0, 0, data])


if __name__ == "__main__":
    host = '192.168.200.242'
    host_key = '7241C8810B8F9EE680C5A8384E576EC9'
    client = TarantoolClient(host=host, port=12801)
    client.authenticate(host_key) # host key is crc32
    client.sync_host_key(host_key)
    stream = {
            'stream_key': 1234556,
            'stream_type': 'xxxx',
            'file_status': {
                'filename': 'xxx',
                'file_dir': 'xxxx'
            },
            'file_tags': ['xxx', 'xxx', 'xxx']
        }
    stream_inst = client.stream_start(stream)
    stream_id = stream_inst[0][0]
    client.switch_stream(space_id=1000,  stream_id=stream_id)
    data = "demo log"
    client.insert(1000, stream_id, data)
