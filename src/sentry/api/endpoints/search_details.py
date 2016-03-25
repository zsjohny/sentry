# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""
from sentry.api.base import Endpoint
from sentry.models.log_search import Search
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
import ast
import datetime


class SearchDetailsEndpoint(Endpoint):
    permission_classes = []

    def convert_args(self, request, search_id, *args, **kwargs):
        kwargs['search_id'] = search_id
        return (args, kwargs)

    def get(self, request, search_id, *args, **kwargs):
        try:
            search = Search.objects.get(id=search_id, user=request.user)
        except ObjectDoesNotExist:
            return Response(status=400, data={'msg': 'object does not exist!'})
        if search:
            if search.time_range is None:
                time_range = None
            else:
                time_range = ast.literal_eval(search.time_range)
            return Response({'id': search.id,
                             'name': search.name,
                             'create_timestamp': search.create_timestamp,
                             'last_timestamp': search.last_timestamp,
                             'query': search.query,
                             'time_range': time_range}, status=200)
        else:
            return Response(status=400, data={'msg': 'failed'})

    def put(self, request, search_id, *args, **kwargs):
        data = request.DATA
        if len(data) == 0:
            return Response(status=400)
        if search_id:
            try:
                search = Search.objects.filter(id=search_id, user=request.user)
            except ObjectDoesNotExist:
                return Response(status=400)

            search.update(name=data.get('name'),
                          last_timestamp=datetime.datetime.now(),
                          query=data.get('query', None),
                          time_range=data.get('time_range', None),
                          config=data.get('config', None))
            return Response(data, status=200)

    def delete(self, request, search_id, *args, **kwargs):
        search = Search.objects.get(id=search_id, user=request.user)
        if search:
            search.delete()
            return Response(status=200, data={'msg': 'ok'})
        return Response(status=400, data={'msg': 'do not exist search!'})
