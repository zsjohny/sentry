# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: mock_data.py
time   : 16/3/28 下午7:00  
"""

from datetime import datetime
import random
import time
import json
from django.conf import settings


def fetch_data(offset, count):
    raw_log_path = settings.MOCK_LOG_FILE
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
                    'events': len(lines),
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
        return result