# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""
from sentry.api.base import Endpoint
from sentry.models.log_widget import LogWidget
from rest_framework.response import Response
import ast


class WidgetIndexEndpoint(Endpoint):
    permission_classes = []

    def get(self, request, *args, **kwargs):
            widget_queryset = LogWidget.objects.filter(user=request.user)
            widget_list = []
            for e in widget_queryset:
                o = {}
                o['id'] = e.id
                o['title'] = e.title
                o['search_id'] = e.search_id
                if e.x_axis is not None:
                    o['x_axis'] = ast.literal_eval(e.x_axis)
                else:
                    o['x_axis'] = None
                if e.x_axis is not None:
                    o['y_axis'] = ast.literal_eval(e.y_axis)
                else:
                    o['y_axis'] = None
                o['chart_type'] = e.chart_type
                widget_list.append(o)
            return Response(widget_list, status=200)

    def post(self, request, *args, **kwargs):
        data = request.DATA
        if len(data) == 0:
            return Response(status=400)
        LogWidget.objects.create(title=data.get('title', None),
                                 search_id=data.get('search_id', None),
                                 x_axis=data.get('x_axis', None),
                                 y_axis=data.get('y_axis', None),
                                 chart_type=data.get('chart_type', None),
                                 desc=data.get('desc', None),
                                 user=request.user)
        return Response({'msg': 'ok'}, status=200)
