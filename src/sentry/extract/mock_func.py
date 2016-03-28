# -*- coding: utf-8 -*-
"""
author : xiaoge
company: LogInsight
email_ : duchao@loginsight.cn
file: mock_func.py
time   : 16/3/28 下午5:40  
"""
from sentry.extract import sourcetype, core
from django.conf import settings

filename = settings.MOCK_LOG_FILE.join("access_log")

stype=sourcetype.try_to_detect_file_sourcetype(filename,filename)

stype= 'access_common'
big_map={}
def mock_data(filename):
    with open(filename) as f:
        for line in f:

            temp = {'sourcetype':stype,'_raw':line}
            final_event = core.extract_event(temp)

            for field in final_event:
                if big_map.has_key(field):
                    big_map[field]['count']+=1
                    if big_map[field]['values'].has_key(final_event[field]):
                        big_map[field]['values'][final_event[field]]+=1
                    else:
                        big_map[field]['values'][final_event[field]]=1

                else:
                    new_map={'key':field,'count':1,'values':{}}
                    if new_map['values'].has_key(final_event[field]):
                        new_map['values'][final_event[field]]+=1
                    else:
                        new_map['values'][final_event[field]]=1

                    big_map[field]=new_map
    return big_map
if __name__=='__main__':
    print 'hh'