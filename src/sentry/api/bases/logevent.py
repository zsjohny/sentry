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


class LogeventPermission(ScopedPermission):
    scope_map = {
        'GET': ['logevent:read', 'logevent:write', 'logevent:delete'],
        'POST': ['logevent:write', 'logevent:delete'],
        'PUT': ['logevent:write', 'logevent:delete'],
        'DELETE': ['logevent:delete'],
    }

    def has_object_permission(self, request, view, logevent):
        if request.auth:
            if self.is_project_key(request):
                return False
            return request.auth.logevent_id == logevent.id

        request.access = access.from_request(request, logevent)
        allowed_scopes = set(self.scope_map.get(request.method, []))
        return any(request.access.has_scope(s) for s in allowed_scopes)


class LogEventEndpoint(Endpoint):
    permission_classes = (LogeventPermission,)

    def convert_args(self, request, *args, **kwargs):
        return (args, kwargs)
