# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""
from sentry.models.log_search import Search
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from sentry.api.base import Endpoint
from sentry.utils.query_parse import *
import requests
import ast


class SearchIndexEndpoint(Endpoint):
    permission_classes = []

    def get(self, request, *args, **kwargs):
            try:
                search_queryset = Search.objects.filter(user_id=request.user.id)
            except ObjectDoesNotExist:
                return Response(status=400)
            search_list = []
            for e in search_queryset:
                obj = {}
                obj['id'] = e.id
                obj['name'] = e.name
                obj['create_timestamp'] = e.create_timestamp
                obj['last_timestamp'] = e.last_timestamp
                obj['query'] = e.query
                if e.time_range is None:
                    obj['time_range'] = None
                else:
                    obj['time_range'] = ast.literal_eval(e.time_range)
                obj['config'] = e.config
                search_list.append(obj)
            return Response(search_list, status=200)

    def post(self, request):
        data = request.DATA
        if len(data) == 0:
            return Response(status=400)
        search_list = Search.objects.filter(name=data.get('name', ''))
        if search_list:
            return Response({'msg': 'existed!'}, status=404)
        search = Search.objects.create(name=data['name'],
                              query=data.get('query', None),
                              config=data.get('config', None),
                              time_range=data.get('time_range', None),
                              desc=data.get('desc', None),
                              user=request.user)
        resp_data = {
            'id': search.id,
            'name': search.name,
            'query': search.query,
            'config': search.config,
            'time_range': search.time_range,
            'desc': search.desc,
        }
        return Response(status=200, data=resp_data)

"""
获取查询结果的接口
PARAM: index_name
TEST:  /api/0/query/<index_name>/?q=search:Andorid
$.get("/api/0/query/idx/?q=search:Android?count=50&offset=0")
"""


class SearchResultEndpoint(Endpoint):
    permission_classes = []

    def convert_args(self, request, index_name, *args, **kwargs):
        kwargs['index_name'] = index_name
        return (args, kwargs)

    def get(self, request, index_name):
        if True:
            from sentry.api.endpoints.mock_data import *
            count = int(request.GET.get('count', 20))
            offset = int(request.GET.get('offset', 0))
            print 'count=', count, 'offset=', offset
            return Response(fetch_data(offset, count))
        else:
            q = request.GET.get('q', '')
            count = request.DATA.get('count', 50)
            offset = request.DATA.get('offset', 0)
            print 'q=', q
            query_json = parse_query(str(q))
            if len(query_json) == 0:
                return Response(status=200, data={"msg": "Invalid query statement"})
            query = str(query_json).replace("'", "\"")
            url = "%s/tenant/%s/%s/search?q=%s&offset=%s&count=%s" % (settings.SEARCH_SERVER_API,
                                                                      request.user.username,
                                                                      index_name,
                                                                      query,
                                                                      offset,
                                                                      count)
            resp = requests.get(str(url))
            return Response(status=resp.status_code, data=resp.json())
