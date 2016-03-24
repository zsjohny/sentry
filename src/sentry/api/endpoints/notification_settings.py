# -*- coding: utf-8 -*-
"""
author : xiaoge
company: LogInsight
email_ : duchao@loginsight.cn
file: notification_settings.py
time   : 16/3/24 下午1:01  
"""
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
import sentry.web.forms.accounts


'''
$.post("/api/0/account/settings/notifications/",{'project-2-alert': 'on',
'subscribe_notes': '0', 'subscribe_by_default': '0', 'project-2-email': '',
'alert_email': '1493578498@qq.com', '
csrfmiddlewaretoken': 's12DBcRHCLGgUXMT8TLswnzgaHccnQ6m',
'project-3-email': ''})

subscribe_notes: 0 or 1
subscribe_by_default: 0 or 1
'''
class NotificationSettingsEndpoint(Endpoint):
    permission_classes = []
    def get(self,request):
        settings_form = NotificationSettingsForm(request.user, request.POST or None)

        project_list = list(Project.objects.filter(
            team__organizationmemberteam__organizationmember__user=request.user,
            team__organizationmemberteam__is_active=True,
            status=ProjectStatus.VISIBLE,
        ).distinct())

        project_forms = [
            (project, ProjectEmailOptionsForm(
                project, request.user,
                request.POST or None,
                prefix='project-%s' % (project.id,)
            ))
            for project in sorted(project_list, key=lambda x: (
                x.team.name if x.team else None, x.name))
        ]

        ext_forms = []
        for plugin in plugins.all():
            for form in safe_execute(plugin.get_notification_forms) or ():
                form = safe_execute(form, plugin, request.user, request.POST or None, prefix=plugin.slug)
                if not form:
                    continue
                ext_forms.append(form)
            pass
        content={
            'alert_email':settings_form.fields['alert_email'].initial,
            'subscribe_by_default':settings_form.fields['subscribe_by_default'].initial,
            'subscribe_notes':settings_form.fields['subscribe_notes'].initial,

        }
        for x in project_forms:
            temp_dict={
                'project-%s-email' % (x[0].id):x[1].fields['email'].initial,
                'project-%s-alert' % (x[0].id):x[1].fields['alert'].initial,
            }
            content.update(temp_dict)
        return Response(data=content,status=200)

    def post(self,request):

        settings_form = NotificationSettingsForm(request.user, request.POST or None)
        project_list = list(Project.objects.filter(
                team__organizationmemberteam__organizationmember__user=request.user,
                team__organizationmemberteam__is_active=True,
                status=ProjectStatus.VISIBLE,
        ).distinct())

        ext_forms = []

        project_forms = [
        (project, ProjectEmailOptionsForm(
            project, request.user,
            request.POST or None,
            prefix='project-%s' % (project.id,)
        ))
        for project in sorted(project_list, key=lambda x: (
            x.team.name if x.team else None, x.name))
        ]

        for plugin in plugins.all():
            for form in safe_execute(plugin.get_notification_forms) or ():
                form = safe_execute(form, plugin, request.user, request.POST or None, prefix=plugin.slug)
                if not form:
                    continue
                ext_forms.append(form)
            all_forms = list(itertools.chain(
            [settings_form], ext_forms, (f for _, f in project_forms)
        ))
        if all(f.is_valid() for f in all_forms):

            for form in all_forms:
                form.save()
            return Response({"msg":"ok"},status=200)
        return Response({"msg":"err!"},status=400)
