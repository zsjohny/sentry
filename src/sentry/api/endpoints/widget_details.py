# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from sentry.api.base import Endpoint
from sentry.models.log_widget import LogWidget
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response


class WidgetDetailsEndpoint(Endpoint):
    permission_classes = []

    def convert_args(self, request, widget_id, *args, **kwargs):
        kwargs['widget_id'] = widget_id
        return (args, kwargs)

    def get(self, request, widget_id, *args, **kwargs):
        try:
            widget = LogWidget.objects.get(id=widget_id, user=request.user)
        except ObjectDoesNotExist:
            return Response(status=400, data={'msg': 'widget does not exist!'})
        if widget:
            return Response({'title': widget.title,
                             'search_id': widget.search_id,
                             'x_axis': widget.x_axis,
                             'y_axis': widget.y_axis,
                             'chart_type': widget.chart_type}, status=200)
        else:
            return Response(status=400, data={'msg': 'failed'})

    def put(self, request, widget_id, *args, **kwargs):
        data = request.DATA
        if len(data) == 0:
            return Response(status=400)
        try:
            # widget = LogWidget.objects.get(id=widget_id, user=request.user)
            # widget.update(title=data.get('title', ''),
            #               search=data.get('search_id', None),
            #               x_axis=data.get('x_axis', None),
            #               y_axis=data.get('y_axis', None),
            #               chart_type=data.get('chart_type', None))
            # w = LogWidget.objects.get(id=widget_id, user=request.user)
            # print 'data == ', data
            # widget = LogWidget(id=widget_id, user=request.user, **data)
            # widget.save(force_update=True)
            LogWidget.objects.filter(pk=widget_id, user_id=request.user.id).update(**data)
            widget = LogWidget.objects.get(id=widget_id)
            resp_data = {
                'id': widget.id,
                'title': widget.title,
                'search_id': widget.search_id,
                'x_axis': widget.x_axis,
                'y_axis': widget.y_axis,
                'chart_type': widget.chart_type
            }
            return Response(data=resp_data, status=200)
        except ObjectDoesNotExist:
            return Response(status=400, data={'msg': 'widget does not exist!'})
        return Response(status=400, data={'msg': 'failed'})

    def delete(self, request, widget_id, *args, **kwargs):
        widget = LogWidget.objects.get(id=widget_id, user=request.user)
        if widget:
            widget.delete()
            return Response(status=200, data={'msg': 'ok'})
        return Response(status=400, data={'msg': 'failed'})
