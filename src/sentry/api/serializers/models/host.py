# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from __future__ import absolute_import

from sentry.api.serializers import Serializer, register
from rest_framework import serializers

from sentry.models import Host


@register(Host)
class HostSerializer(Serializer):
    host_name = serializers.CharField(max_length=200)
    host_key = serializers.CharField(max_length=200)
    host_type = serializers.CharField(max_length=200)
    system = serializers.CharField(max_length=200)
    distver = serializers.CharField(max_length=50)
    create_time = serializers.DateTimeField()
    last_time = serializers.DateTimeField()

    def serialize(self, obj, attrs, user):
        return {
            'id': str(obj.id),
            'host_name': obj.host_name,
            'host_key': obj.host_key,
            'host_type': obj.host_type,
            'system': obj.system,
            'create_time': obj.create_time,
            'last_time': obj.last_time,
        }
