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
from sentry.models.mock_data import MockData
from django.core.exceptions import ObjectDoesNotExist

def insert_db_mockdata(*args, **kwargs):
    mockdata = MockData(*args, **kwargs)
    mockdata.save()


def fetch_data(offset, count, key, sort, query):
    raw_log_path = settings.MOCK_LOG_FILE
    result = {}
    hits = []
    with open(raw_log_path, "r") as fd:
        lines = fd.readlines()

        for line in lines[offset:offset+count]:
            i = offset
            ro = {}
            t_arr = line.split(' ')
            ro['remote_addr'] = t_arr[0].replace("\"", "")
            ro['remote_user'] = t_arr[2].replace("\"", "")
            ro['_timestamp'] = (t_arr[3][1:] + t_arr[4][0:len(t_arr[4])-1]).replace("\"", "")
            ro['method'] = t_arr[5].replace("\"", "")
            ro['url'] = t_arr[6].replace("\"", "")
            ro['protocol'] = t_arr[7].replace("\"", "")
            ro['status'] = t_arr[8].replace("\"", "")
            ro['body_bytes_sent'] = t_arr[9].replace("\"", "")
            ro['http_referer'] = t_arr[10].replace("\"", "")
            ro['http_user_agent'] = t_arr[11].replace("\"", "")
            ro['http_x_forwarded_for'] = str(t_arr[12:]).replace("\"", "")
            ro['_raw'] = line.replace("\"", "")
            try :
                o = MockData.objects.get(id=i)
            except ObjectDoesNotExist as e:
                insert_db_mockdata(**ro)
            i = i+1

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
        if sort == 'desc':
            meta['sort'] = {'reverse': True, 'key': key},
        else:
            meta['sort'] = {'reverse': False, 'key': key},

        meta['query'] = query,

        fields = hits[0].keys()
        words = []
        i = 0
        for e in fields:
            o = {}
            o['name'] = e
            if i % 2 == 0:
                o['checked'] = True
            else:
                o['checked'] = False
            if e == 'status':
                o['type'] = 'Number'
            elif e == 'body_bytes_sent':
                o['type'] = 'Number'
            else:
                o['type'] = 'string'
            i = i + 1
            words.append(o)

        sources = [{'source_name': 'nginx',
                    'regex': '',
                    'events': len(lines),
                    'first_event': str(datetime.now()),
                    'last_event': str(datetime.now())}]

        result['meta'] = meta
        result['fields'] = words
        result['words'] = fields
        if sort == 'desc':
            result['hits'] = sorted(hits, reverse=True)
            i = offset
            for row in result['hits']:
                row['id'] = i
                i = i + 1
        else:
            i = offset
            result['hits'] = sorted(hits, reverse=True)
            for row in result['hits']:
                row['id'] = i
                i = i+1
            result['hits'] = sorted(hits, reverse=False)

        result['sources'] = sources
        json_str = json.dumps(result)
        with open("mock.data", "w") as wd:
            wd.write(json_str)
        if query.find('group') > 0:
            hits = []
            for i in range(0, offset+count):
                o = {}
                o['method_get_count'] = random.randint(10, 10000)
                o['method_post_count'] = random.randint(10, 10000)
                o['method_put_count'] = random.randint(10, 10000)
                o['method_delete_count'] = random.randint(10, 10000)
                o['status_200_count'] = random.randint(10, 10000)
                o['status_201_count'] = random.randint(10, 10000)
                o['status_202_count'] = random.randint(10, 10000)
                o['status_300_count'] = random.randint(10, 10000)
                o['status_301_count'] = random.randint(10, 10000)
                o['status_302_count'] = random.randint(10, 10000)
                o['status_400_count'] = random.randint(10, 10000)
                o['status_401_count'] = random.randint(10, 10000)
                o['status_403_count'] = random.randint(10, 10000)
                o['status_404_count'] = random.randint(10, 10000)
                o['status_500_count'] = random.randint(10, 10000)
                o['status_505_count'] = random.randint(10, 10000)
                o['status_502_count'] = random.randint(10, 10000)
                hits.append(o)
        result['hits'] = hits
        return result