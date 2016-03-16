# -*- coding: utf-8 -*-
"""
author : xiaoge
company: LogInsight
email_ : duchao@loginsight.cn
file: project_notifications.py
time   : 16/3/15 下午8:16  
"""
from __future__ import absolute_import
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.response import Response
from django.contrib import messages
from sentry.api.bases.project import ProjectEndpoint
from sentry.models.organization import Organization
from sentry.models.project import Project
from sentry import constants
from sentry.app import digests
from sentry.web.forms.projects import (
    DigestSettingsForm,
    NotificationSettingsForm,
)
from sentry.digests import get_option_key as get_digest_option_key
from sentry.plugins import plugins, NotificationPlugin
from django.utils.safestring import mark_safe
from sentry.testutils import APITestCase


OK_SETTINGS_SAVED = ('Your settings were saved successfully.')


class ProjectNotificationsEndpoint(ProjectEndpoint):
    # required_scope = 'project:write'
    # permission_classes = []

    def convert_args(self, request, organization_slug, project_slug, *args, **kwargs):
        kwargs['organization_slug'] = organization_slug
        kwargs['project_slug'] = project_slug
        return (args, kwargs)

    def _iter_plugins(self):
        for plugin in plugins.all(version=1):
            if not isinstance(plugin, NotificationPlugin):
                continue
            yield plugin

    def _handle_enable_plugin(self, request, project):
        plugin = plugins.get(request.POST['plugin'])
        plugin.enable(project)

        messages.add_message(
                request, messages.SUCCESS,
                constants.OK_PLUGIN_ENABLED.format(name=plugin.get_title()),
        )

    def _handle_disable_plugin(self, request, project):
        plugin = plugins.get(request.POST['plugin'])
        plugin.disable(project)
        messages.add_message(
                request, messages.SUCCESS,
                constants.OK_PLUGIN_DISABLED.format(name=plugin.get_title()),
        )

    def get(self, request, organization_slug, project_slug):

        organization = Organization.objects.get(slug=organization_slug)
        project_slug = Project.objects.get(slug=project_slug)
        print type(project_slug),project_slug
        if digests.enabled(project_slug):
            enabled_plugins = []
            other_plugins = []
            for plugin in self._iter_plugins():
                if plugin.is_enabled(project_slug):
                    content = plugin.get_notification_doc_html()

                    form = plugin.project_conf_form
                    if form is not None:
                        view = plugin.configure(request, project=project_slug)
                        if isinstance(view, HttpResponse):
                            return view
                        enabled_plugins.append((plugin, mark_safe(content + view)))
                    elif content:
                        enabled_plugins.append((plugin, mark_safe(content)))
                elif plugin.can_configure_for_project(project_slug):
                    other_plugins.append(plugin)

            context={
                'minimum_delay': project_slug.get_option(
                        get_digest_option_key('mail', 'minimum_delay'),
                        digests.minimum_delay,
                )/ 60,
                'maximum_delay': project_slug.get_option(
                        get_digest_option_key('mail', 'maximum_delay'),
                        digests.maximum_delay,
                )/ 60,
                'prefix': 'digests',
                'subject_prefix': project_slug.get_option(
                            'mail:subject_prefix', settings.EMAIL_SUBJECT_PREFIX),
                'enabled_plugins': str(enabled_plugins),
                'other_plugins': str(other_plugins)
                }
            return Response(data=context, status=200)

        else:
            return Response(data={'error': 'error', 'code': 40000}, status=400)


    def post(self, request, organization_slug, project_slug):

        organization = Organization.objects.get(slug=organization_slug)
        project_slug = Project.objects.get(slug=project_slug)
        op = request.POST.get('op')
        if op == 'enable':
            self._handle_enable_plugin(request, project_slug)
            return Response(request.path)
            # return HttpResponseRedirect(request.path)
        elif op == 'disable':
            self._handle_disable_plugin(request, project_slug)
            return Response(request.path)
            # return HttpResponseRedirect(request.path)

        if op == 'save-settings':
            if digests.enabled(project_slug):
                print "mmmmmm"
                project_slug.update_option('mail:subject_prefix',request.POST['general-subject_prefix'])
                #     if digests_form is not None:
                max_value=int(request.POST['digests-maximum_delay'])*60
                min_value=int(request.POST['digests-minimum_delay'])*60
                if max_value>=min_value:
                    project_slug.update_option(get_digest_option_key('mail', 'minimum_delay'),int(request.POST['digests-minimum_delay'])*60,
                        )
                    project_slug.update_option(get_digest_option_key('mail', 'maximum_delay'),int(request.POST['digests-maximum_delay'])*60,
                        )
                    return Response(data={"succeed"},status=200)
                # return HttpResponseRedirect(request.path)
                return Response(data={"error":"Maximum delivery frequency must be equal to or greater than the minimum delivery frequency"})