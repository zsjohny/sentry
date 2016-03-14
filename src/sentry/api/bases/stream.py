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
from sentry.models import Stream


class StreamPermission(ScopedPermission):
    scope_map = {
        'GET': ['stream:read', 'stream:write', 'stream:delete'],
        'POST': ['stream:write', 'stream:delete'],
        'PUT': ['stream:write', 'stream:delete'],
        'DELETE': ['stream:delete'],
    }

    def has_object_permission(self, request, view, stream):
        if request.auth:
            if self.is_project_key(request):
                return False
            return request.auth.stream_id == Stream.id

        request.access = access.from_request(request, stream)
        allowed_scopes = set(self.scope_map.get(request.method, []))
        return any(request.access.has_scope(s) for s in allowed_scopes)


class StreamEndpoint(Endpoint):
    permission_classes = (StreamPermission,)

    def convert_args(self, request, *args, **kwargs):
        return (args, kwargs)
