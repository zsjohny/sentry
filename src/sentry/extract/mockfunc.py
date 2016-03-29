# -*- coding: utf-8 -*-
"""
author : xiaoge
company: LogInsight
email_ : duchao@loginsight.cn
file: mockfunc.py
time   : 16/3/28 下午5:40  
"""
from sentry.extract import sourcetype, core
from django.conf import settings

filename = settings.MOCK_CONF+r"/"+r"access.log"
#filename = r'/home/ubuntu/sentry/mock'+r"/"+r"access.log"

stype=sourcetype.try_to_detect_file_sourcetype(filename,filename)

stype= 'access_common'
big_map={}
def mock_data(filename,stype='access_common'):
    with open(filename) as f:
        for line in f:

            temp = {'sourcetype':stype,'_raw':line}
            final_event = core.extract_event(temp)

            for field in final_event:
                if final_event[field]!=None:
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
   s= mock_data(filename)
   print s.keys(),s['domain'],s['domain']['values']
