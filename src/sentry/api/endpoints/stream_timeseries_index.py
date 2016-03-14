# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""


from __future__ import absolute_import
from rest_framework.response import Response
from sentry.api.bases.stream import StreamEndpoint
import requests
from django.conf import settings


class StreamTimeSeriesIndexEndpoint(StreamEndpoint):

    def get(self, request):
        """
        List an stream's timeseries count
        ````````````````````````````

        Return a list of hosts bound to a organization.
        :pparam string host_key:
        :pparam string stream_key : the host id  for Host instance
        :pparam string count: default 20
        :pparam string offset: default 0
        :auth: required
        : resp.body = {
            "start_time": //起始时间
            "timeseries": [count, count, count]
        }
        """
        result = request.GET
        print request.GET
        host_key = result['host_key']
        stream_key = result['stream_key']
        offset = result['offset']
        count = result['count']
        print 'storage_server=', settings.STORAGE_SERVER
        uri = "/api/v1/u/%s/nodes/%s/streams/%s/statistic?offset=%s&len=%s" % ('sdf', host_key, stream_key, offset, count)
        r = requests.get(settings.STORAGE_SERVER + uri)
        print r
        return Response(r.json())
