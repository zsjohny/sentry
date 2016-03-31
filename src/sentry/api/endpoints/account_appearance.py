# -*- coding: utf-8 -*-
"""
author : xiaoge
company: LogInsight
email_ : duchao@loginsight.cn
file: account_appearance.py
time   : 16/3/24 上午11:42  
"""
from __future__ import absolute_import

from rest_framework.response import Response
from sentry.api.base import Endpoint

from django.conf import settings
from sentry.models import (
    LostPasswordHash, Project, ProjectStatus, UserOption
)
from sentry.web.forms.accounts import AppearanceSettingsForm
'''
$.post("/api/0/account/settings/appearance/",{'timezone': 'UTC',
'csrfmiddlewaretoken': 's12DBcRHCLGgUXMT8TLswnzgaHccnQ6m',
'language': 'en', 'stacktrace_order': '-1','clock_24_hours': 'on'})
'''


class AppearanceSettingsEndpoint(Endpoint):
    permission_classes = []

    def get(self, request):

        options = UserOption.objects.get_all_values(user=request.user, project=None)

        initial = {
            'language': options.get('language') or request.LANGUAGE_CODE,
            'stacktrace_order': int(options.get('stacktrace_order', -1) or -1),
            'timezone': options.get('timezone') or settings.SENTRY_DEFAULT_TIME_ZONE,
            'clock_24_hours': options.get('clock_24_hours') or False,
        }
        return Response(data=initial, status=200)

    def post(self, request):
        options = UserOption.objects.get_all_values(user=request.user, project=None)
        form = AppearanceSettingsForm(request.user, request.POST or None, initial={
            'language': options.get('language') or request.LANGUAGE_CODE,
            'stacktrace_order': int(options.get('stacktrace_order', -1) or -1),
            'timezone': options.get('timezone') or settings.SENTRY_DEFAULT_TIME_ZONE,
            'clock_24_hours': options.get('clock_24_hours') or False,
         })
        if form.is_valid():
            form.save()
        else:
            return Response({'msg': 'some parameter error'}, status=400)
        return Response(data={'msg': 'ok'}, status=200)