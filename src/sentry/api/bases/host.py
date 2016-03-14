# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""
from __future__ import absolute_import
from sentry.auth import access
from sentry.api.base import Endpoint
from sentry.api.permissions import ScopedPermission
from sentry.models import Host


class HostPermission(ScopedPermission):
    scope_map = {
        'GET': ['host:read', 'host:write', 'host:delete'],
        'POST': ['host:write', 'host:delete'],
        'PUT': ['host:write', 'host:delete'],
        'DELETE': ['host:delete'],
    }

    def has_object_permission(self, request, view, host):
        if request.auth:
            if self.is_project_key(request):
                return False
            return request.auth.host_id == Host.id

        request.access = access.from_request(request, host)
        allowed_scopes = set(self.scope_map.get(request.method, []))
        return any(request.access.has_scope(s) for s in allowed_scopes)


class HostEndpoint(Endpoint):
    permission_classes = (HostPermission,)

    def convert_args(self, request, *args, **kwargs):
        return (args, kwargs)
