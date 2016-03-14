
# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""


from __future__ import absolute_import
from sentry.api.base import Endpoint
from sentry.models.visualization import Visaulization
from rest_framework.response import Response
import datetime
import ast


class VisualizationIndexEndpoint(Endpoint):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        queryset = Visaulization.objects.filter(user=request.user)
        dashboard_list = []
        for q in queryset:
            o = {}
            o['id'] = q.id
            o['name'] = q.name
            o['created_at'] = q.created_at
            o['updated_at'] = q.updated_at
            if q.layout is None:
                o['layout'] = None
            else:
                o['layout'] = ast.literal_eval(q.layout)
            o['is_fav'] = q.is_fav
            o['desc'] = q.desc
            dashboard_list.append(o)
        return Response(dashboard_list)

    def post(self, request, *args, **kwargs):
        data = request.DATA
        if len(data) == 0:
            return Response(status=400, data={'msg': 'no request parameters'})
        visualization = Visaulization.objects.create(name=data['name'],
                                                     created_at=datetime.datetime.now(),
                                                     updated_at=datetime.datetime.now(),
                                                     is_fav=data.get('is_fav', False),
                                                     layout=data.get('layout', None),
                                                     desc=data.get('desc', None),
                                                     user=request.user)
        if visualization:
            return Response(data, status=200)
        else:
            return Response(status=400, data={'msg': 'failed to add visualization'})
