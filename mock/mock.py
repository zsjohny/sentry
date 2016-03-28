# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: mock.py
time   : 16/3/28 下午6:38  
"""

import os
import json
import time
import random
from datetime import datetime
# '$remote_addr - $remote_user [$time_local] "$request" '
#                       '$status $body_bytes_sent "$http_referer" '
#                       '"$http_user_agent" "$http_x_forwarded_for"'
# 127.0.0.1 - - [18/Dec/2015:20:08:22 +0800] "GET /sockjs-node/info?t=1450440502937 HTTP/1.1" 404 570 "http://localhost:8080/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"


def fetch_data(count, offset):
    raw_log_path = '/Users/wanghe/LogSample/nginx/access.log'
    result = {}
    hits = []
    with open(raw_log_path, "r") as fd:
        lines = fd.readlines()

        for line in lines[offset:offset+count]:
            ro = {}
            t_arr = line.split(' ')
            ro['remote_addr'] = t_arr[0]
            ro['remote_user'] = t_arr[2]
            ro['time_local'] = t_arr[3][1:] + t_arr[4][0:len(t_arr[4])-1]
            ro['method'] = t_arr[5]
            ro['url'] = t_arr[6]
            ro['protocol'] = t_arr[7]
            ro['status'] = t_arr[8]
            ro['body_bytes_sent'] = t_arr[9]
            ro['http_referer'] = t_arr[10]
            ro['http_user_agent'] = t_arr[11]
            ro['http_x_forwarded_for'] = str(t_arr[12:])
            ro['_raw'] = line
            hits.append(ro)
        meta = {}
        meta['search_id'] = 1
        meta['matches_total'] = len(lines)
        meta['match'] = len(hits)
        meta['count'] = count
        meta['offset'] = offset
        meta['time'] = time.clock()
        meta['search_time'] = time.clock()
        meta['process_time'] = time.clock()
        meta['shard_count'] = random.randint(0, 100)
        meta['warning'] = []
        meta['error'] = []
        meta['first_event'] = str(datetime.now())
        meta['last_event'] = str(datetime.now())
        fields = hits[0].keys()
        words = fields
        sources = [{'source_name': 'nginx',
                    'regex': '',
                    'events': random.randint(0, 10000),
                    'first_event': str(datetime.now()),
                    'last_event': str(datetime.now())}]

        result['meta'] = meta
        result['fields'] = fields
        result['words'] = words
        result['hits'] = hits
        result['sources'] = sources
        json_str = json.dumps(result)
        with open("mock.data", "w") as wd:
            wd.write(json_str)
