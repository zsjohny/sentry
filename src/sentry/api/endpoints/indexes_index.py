# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""
from __future__ import absolute_import
from sentry.api.base import Endpoint
from sentry.models.log_indexes import Indexes
from rest_framework.response import Response
from django.conf import settings
import datetime
import requests


class IndexesIndexEndpoint(Endpoint):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        queryset = Indexes.objects.filter(user=request.user)
        indexes_list = []
        for q in queryset:
            o = {}
            o['id'] = q.id
            o['name'] = q.name
            o['type'] = q.type
            o['dsn'] = q.dsn
            o['desc'] = q.desc
            o['created_at'] = q.created_at
            o['updated_at'] = q.updated_at
            indexes_list.append(o)
        return Response(indexes_list)

    def post(self, request, *args, **kwargs):
        data = request.DATA
        if len(data) == 0:
            return Response(status=400, data={'msg': 'no request parameters'})
        url = "%s/tenant/test/%s/create?schema=key_format=r, value_format=QSQ," \
              " columns=(_id, user_id, movie_id, rating)" % (settings.SEARCH_SERVER_API, data['name'])
        resp = requests.get(url)
        if resp.status_code != 200:
            return Response(resp.status_code, data={'msg': 'failed'})

        indexes = Indexes.objects.create(name=data['name'],
                                         created_at=datetime.datetime.now(),
                                         updated_at=datetime.datetime.now(),
                                         type=data.get('type', None),
                                         dsn=data.get('dsn', None),
                                         desc=data.get('desc', None),
                                         user=request.user)

        if indexes:
            return Response(data, status=200)
        else:
            return Response(status=400, data={'msg': 'failed'})
