# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""


from __future__ import absolute_import
from rest_framework.response import Response
from sentry.api.bases.logevent import LogEventEndpoint
from django.conf import settings
import requests


class LogEventIndexEndpoint(LogEventEndpoint):

    def get(self, request):
        """
        List an event  's log file
        ````````````````````````````

        Return a list of hosts bound to a organization.
        :pparam string  file_id : the file id for Log file
        :pparam string  event_offset : the offset of log
        :pparam string : event_count : count of events num
        :auth: required
        """

        result = request.GET
        stream_id = result.get('stream_id', '0')
        host_id = result.get('host_id', '0')
        event_count = result.get('event_count', '0')
        event_offset = result.get('event_offset', '0')
        file_id = result.get('file_id', '0')
        url = "%s/u/%s/nodes/%s/streams/%s/files/%s/content/?fid=%s&offset=%s&len=%s" \
            % (settings.STORAGE_API_BASE_URL, request.user.id, host_id, stream_id, file_id, file_id, event_offset, event_count)
        r = requests.get(url)
        if r.status_code == 200:
            resp = r.json()
            print resp['content']
            event_list = []
            for ctx in resp['content']:
                payload_list = ctx[1].split('\n')
                i = int(event_offset)
                for payload in payload_list:
                    event_obj = {
                        'last_timestamp': '',
                        'file_id': '',
                        'create_timestamp': '',
                        'offset': '',
                        'payload': '',
                        'size': 0
                    }
                    i = i + 1
                    event_obj['file_id'] = file_id
                    event_obj['offset'] = i
                    event_obj['size'] = len(payload)
                    event_obj['payload'] = payload
                    event_list.append(event_obj)

        return Response(event_list)
