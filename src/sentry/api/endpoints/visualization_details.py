
# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from sentry.api.base import Endpoint
from sentry.models.visualization import Visaulization
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
import ast
import datetime


class VisualizationDetailsEndpoint(Endpoint):
    permission_classes = []

    def convert_args(self, request, visualization_id, *args, **kwargs):
        kwargs['visualization_id'] = visualization_id
        return (args, kwargs)

    def get(self, request, visualization_id, *args, **kwargs):
        try:
            visualization = Visaulization.objects.get(id=visualization_id, user=request.user)
        except ObjectDoesNotExist:
            return Response(status=400, data={'msg': 'visualization does not exist!'})
        if visualization:
            layout = None
            if visualization.layout is None:
                layout = None
            else:
                layout = ast.literal_eval(visualization.layout)
            return Response({'name': visualization.name,
                             'desc': visualization.desc,
                             'is_fav': visualization.is_fav,
                             'created_at': visualization.created_at,
                             'updated_at': visualization.updated_at,
                             'layout': layout}, status=200)
        else:
            return Response(status=400, data={'msg': 'failed'})

    def put(self, request, visualization_id, *args, **kwargs):
        data = request.DATA
        if len(data) == 0:
            return Response(status=400, data={'msg': 'no request parameters'})
        try:
            visualization = Visaulization(id=visualization_id, user_id=request.user.id, **data)
            visualization.save()
            resp_data = {
                'id': visualization.id,
                'name': visualization.name,
                'layout': visualization.layout,
                'is_fav': visualization.is_fav,
                'updated_at': visualization.updated_at,
                'created_at': visualization.created_at
            }
            return Response(status=200, data=resp_data)
        except ObjectDoesNotExist:
            return Response(status=400, data={'msg': 'visualization objects does not exist!'})
        return Response(status=400, data={'msg': 'failed'})

    def delete(self, request, visualization_id, *args, **kwargs):
        visualization = Visaulization.objects.get(id=visualization_id, user=request.user)
        if visualization:
            visualization.delete()
            return Response(status=200, data={'msg': 'ok'})
        return Response(status=400, data={'msg': 'failed to delete visualization'})
