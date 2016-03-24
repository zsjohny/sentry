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
from django.core.exceptions import ObjectDoesNotExist
import datetime
import requests


class IndexesIndexEndpoint(Endpoint):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        url = "%s/tenant/%s/list" % (settings.SEARCH_SERVER_API,  request.user.username)
        resp = requests.get(url)
        if resp.status_code == 200:
            index_list = resp.json().get('index_info', None)
            idx_list = []
            print resp.status_code
            for k in index_list.keys():
                o = {}
                o['name'] = k
                idx_list.append(o)
            return Response(idx_list)
        return Response(status=resp.status_code, data={'msg': 'search server error'})

    def post(self, request, *args, **kwargs):
        data = request.DATA
        if len(data) == 0:
            return Response(status=400, data={'msg': 'no request parameters'})
        try:
            index = Indexes.objects.get(user_id=request.user.id, name=data['name'])
        except ObjectDoesNotExist:
            url = "%s/tenant/%s/%s/create?schema=key_format=r, value_format=QSQ," \
                  " columns=(_id, user_id, movie_id, rating)" % (settings.SEARCH_SERVER_API,
                                                                request.user.username,
                                                                 data['name'])
            resp = requests.get(url)
            if resp.status_code != 200:
                return Response(status=resp.status_code, data={'msg': 'failed'})
            if Indexes.objects.filter(user=request.user, name=data['name']):
                return Response(status=400, data={'msg': 'failed, Indexname has existed!'})
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
        return Response(status=400, data={'msg': 'index name has existed!'})
