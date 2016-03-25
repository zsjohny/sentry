# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from __future__ import absolute_import
from sentry.api.base import Endpoint
from sentry.models.LogInsightDashboard import LogInsightDashboard
from rest_framework.response import Response
import datetime
import ast


class DashboardIndexEndpoint(Endpoint):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        queryset = LogInsightDashboard.objects.filter(user=request.user)
        dashboard_list = []
        for q in queryset:
            o = {}
            o['id'] = q.id
            o['name'] = q.name
            if q.layout is None:
                o['layout'] = None
            else:
                o['layout'] = ast.literal_eval(q.layout)
            o['desc'] = q.desc
            o['created_at'] = q.created_at
            o['updated_at'] = q.updated_at
            o['is_fav'] = q.is_fav
            dashboard_list.append(o)
        return Response(data=dashboard_list, status=200)

    def post(self, request, *args, **kwargs):
        data = request.DATA
        if len(data) == 0:
            return Response(status=400, data={'msg': 'no request parameters'})
        dashboard = LogInsightDashboard.objects.create(name=data['name'],
                                                       created_at=datetime.datetime.now(),
                                                       updated_at=datetime.datetime.now(),
                                                       desc=data.get('desc', ''),
                                                       layout=data.get('layout', None),
                                                       is_fav=data.get('is_fav', False),
                                                       user_id=request.user.id)

        if dashboard:
            layout = dashboard.layout
            if len(layout) == 0:
                layout = None
            else:
                layout = ast.literal_eval(dashboard.layout)
            resp_data = {
                'id': dashboard.id,
                'name': dashboard.name,
                'created_at': dashboard.created_at,
                'updated_at': dashboard.updated_at,
                'desc': dashboard.desc, 
                'layout': layout,
                'is_fav': dashboard.is_fav
            }
            return Response(data=resp_data, status=200)
        else:
            return Response(status=500)
