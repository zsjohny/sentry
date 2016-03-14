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


class LogFilePermission(ScopedPermission):
    scope_map = {
        'GET': ['logfile:read', 'logfile:write', 'logfile:delete'],
        'POST': ['logfile:write', 'logfile:delete'],
        'PUT': ['logfile:write', 'logfile:delete'],
        'DELETE': ['logfile:delete'],
    }

    def has_object_permission(self, request, view, logfile):
        if request.auth:
            if self.is_project_key(request):
                return False
            return request.auth.logfile_id == logfile.id

        request.access = access.from_request(request, logfile)
        allowed_scopes = set(self.scope_map.get(request.method, []))
        return any(request.access.has_scope(s) for s in allowed_scopes)


class LogFileEndpoint(Endpoint):
    permission_classes = (LogFilePermission,)

    def convert_args(self, request, *args, **kwargs):
        return (args, kwargs)
