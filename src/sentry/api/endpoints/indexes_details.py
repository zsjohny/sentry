# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""


from sentry.api.base import Endpoint
from sentry.models.log_indexes import Indexes
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
import datetime


class IndexesDetailsEndpoint(Endpoint):
    permission_classes = []

    def convert_args(self, request, index_id, *args, **kwargs):
        kwargs['index_id'] = index_id
        return (args, kwargs)

    def get(self, request, index_id, *args, **kwargs):
        try:
            index = Indexes.objects.get(id=index_id, user=request.user)
        except ObjectDoesNotExist:
            return Response(status=400, data={'msg': 'object does not exist!'})
        if index:
            return Response({'name': index.name,
                             'desc': index.desc,
                             'type': index.type,
                             'dsn': index.dsn,
                             'created_at': index.created_at,
                             'updated_at': index.updated_at}, status=200)
        else:
            return Response(status=400, data={'msg': 'Index does not exist'})

    def put(self, request, index_id, *args, **kwargs):
        data = request.DATA
        if len(data) == 0:
            return Response(status=400, data={'msg': 'no request parameters'})
        try:
            index = Indexes(id=index_id, user_id=request.user.id, **data)
            index.save()
            resp_data = {
                'id': index.id,
                'name': index.name,
                'desc': index.desc,
                'dsn': index.dsn,
                'created_at': index.created_at,
                'updated_at': index.updated_at
            }
            return Response(status=200, data=resp_data)
        except ObjectDoesNotExist:
            return Response(status=200, data={'msg': 'index object has not exist!'})
        return Response(status=400, data={'msg': 'failed'})

    def delete(self, request, index_id, *args, **kwargs):
        index = Indexes.objects.get(id=index_id, user=request.user)
        if index:
            index.delete()
            return Response(status=200, data={'msg': 'ok'})
        return Response(status=400, data={'msg': 'failed'})
