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



import itertools

from django.contrib import messages
from django.contrib.auth import login as login_user, authenticate
from django.core.context_processors import csrf
from django.db import transaction
from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
from sudo.decorators import sudo_required
from django.conf import settings
from sentry.models import (
    LostPasswordHash, Project, ProjectStatus, UserOption
)
from sentry.plugins import plugins
from sentry.web.decorators import login_required
from sentry.web.forms.accounts import (
    AccountSettingsForm, NotificationSettingsForm, AppearanceSettingsForm,
    RecoverPasswordForm, ChangePasswordRecoverForm,
    ProjectEmailOptionsForm)
from sentry.web.helpers import render_to_response
from sentry.utils.auth import get_auth_providers, get_login_redirect
from sentry.utils.safe import safe_execute




'''
$.post("/api/0/account/settings/appearance/",{'timezone': 'UTC',
'csrfmiddlewaretoken': 's12DBcRHCLGgUXMT8TLswnzgaHccnQ6m',
'language': 'en', 'stacktrace_order': '-1','clock_24_hours': 'on'})
'''

class AppearanceSettingsEndpoint(Endpoint):
    permission_classes = []
    # def convert_args(self, request, organization_slug, project_slug, *args, **kwargs):
    #     kwargs['organization_slug'] = organization_slug
    #     kwargs['project_slug'] = project_slug
    #     return (args, kwargs)

    # @csrf_protect
    # @never_cache
    # @login_required
    # @sudo_required
    # @transaction.atomic
    def get(self,request):

        options = UserOption.objects.get_all_values(user=request.user, project=None)

        initial={
            'language': options.get('language') or request.LANGUAGE_CODE,
            'stacktrace_order': int(options.get('stacktrace_order', -1) or -1),
            'timezone': options.get('timezone') or settings.SENTRY_DEFAULT_TIME_ZONE,
            'clock_24_hours': options.get('clock_24_hours') or False,
        }
        return Response(data=initial,status=200)


    def post(self,request):

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
            return Response({'msg':'some parameter error'},status=400)
        return Response("ok",status=200)