# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from sentry.api.base import Endpoint
from sentry.models.LogInsightDashboard import LogInsightDashboard
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
import ast
import datetime
import os


class DashboardDetailsEndpoint(Endpoint):
    permission_classes = []

    def convert_args(self, request, dashboard_id, *args, **kwargs):
        kwargs['dashboard_id'] = dashboard_id
        return (args, kwargs)

    def get(self, request, dashboard_id, *args, **kwargs):
        try:
            dashboard = LogInsightDashboard.objects.get(id=dashboard_id, user=request.user)
        except ObjectDoesNotExist:
            return Response(status=400, data={'msg': 'object does not exist!'})
        if dashboard:
            layout = dashboard.layout
            if layout is not None:
                layout = ast.literal_eval(layout)
            return Response({'name': dashboard.name,
                             'desc': dashboard.desc,
                             'is_fav': dashboard.is_fav,
                             'created_at': dashboard.created_at,
                             'updated_at': dashboard.updated_at,
                             'layout': layout}, status=200)
        else:
            return Response(status=400, data={'msg': 'failed'})

    def put(self, request, dashboard_id, *args, **kwargs):
        data = request.DATA
        if len(data) == 0:
            return Response(status=400, data={'msg': 'no request parameters'})
        if dashboard_id:
            LogInsightDashboard.objects.filter(id=dashboard_id).update(**data)
            dashboard = LogInsightDashboard.objects.get(id=dashboard_id)
            layout = dashboard.layout
            resp_data = {
                'id': dashboard.id,
                'name': dashboard.name,
                'layout': layout,
                'desc': dashboard.desc,
                'updated_at': dashboard.updated_at,
                'created_at': dashboard.created_at,
                'is_fav': dashboard.is_fav,
            }
            return Response(resp_data, status=200)
        return Response(status=400, data=data)

    def delete(self, request, dashboard_id, *args, **kwargs):
        dashboard = LogInsightDashboard.objects.get(id=dashboard_id, user=request.user)
        if dashboard:
            dashboard.delete()
            return Response(status=200, data={'msg': 'ok'})
        return Response(status=400, data={'msg': 'dashboard does not exist'})
