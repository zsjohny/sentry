# -*- coding: utf-8 -*-
"""
author : xiaoge
company: LogInsight
email_ : duchao@loginsight.cn
file: project_lssue_tracking.py
time   : 16/3/18 下午12:13  
"""


from __future__ import absolute_import

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.safestring import mark_safe
from rest_framework.response import Response

from sentry import constants
from sentry.models.project import Project
from sentry.plugins import plugins, IssueTrackingPlugin
from sentry.signals import plugin_enabled
from sentry.web.frontend.base import ProjectView


class ProjectIssueTrackingEndpoint(ProjectView):
    required_scope = 'project:write'

    def _iter_plugins(self):
        for plugin in plugins.all(version=1):
            if not isinstance(plugin, IssueTrackingPlugin):
                continue
            yield plugin

    def _handle_enable_plugin(self, request, project):
        plugin = plugins.get(request.POST['plugin'])
        plugin.enable(project)

        plugin_enabled.send(plugin=plugin, project=project, user=request.user, sender=self)

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

    def handle(self, request, organization, team, project):
        if request.method == 'POST':
            op = request.POST.get('op')
            if op == 'enable':
                self._handle_enable_plugin(request, project)
                return HttpResponseRedirect(request.path)
            elif op == 'disable':
                self._handle_disable_plugin(request, project)
                return HttpResponseRedirect(request.path)

        enabled_plugins = []
        other_plugins = []
        for plugin in self._iter_plugins():
            if plugin.is_enabled(project):
                content = plugin.get_issue_doc_html()

                form = plugin.project_conf_form
                if form is not None:
                    view = plugin.configure(request, project=project)
                    if isinstance(view, HttpResponse):
                        return view
                elif content:
                    enabled_plugins.append((plugin, mark_safe(content)))
                enabled_plugins.append((plugin, mark_safe(content + view)))
            elif plugin.can_configure_for_project(project):
                other_plugins.append(plugin)

        context = {
            'page': 'issue-tracking',
            'enabled_plugins': enabled_plugins,
            'other_plugins': other_plugins,
        }

        return self.respond('sentry/project-issue-tracking.html', context)

    def convert_args(self, request, organization_slug, project_slug, *args, **kwargs):
        kwargs['organization_slug'] = organization_slug
        kwargs['project_slug'] = project_slug
        return (args, kwargs)

    def get(self,request, organization_slug, project_slug):
        #will be done
        project=Project.objects.get(slug=project_slug)

        enabled_plugins = []
        other_plugins = []
        for plugin in self._iter_plugins():
            if plugin.is_enabled(project):
                content = plugin.get_issue_doc_html()

                form = plugin.project_conf_form
                if form is not None:
                    view = plugin.configure(request, project=project)
                    if isinstance(view, HttpResponse):
                        return view
                elif content:
                    enabled_plugins.append((plugin, mark_safe(content)))
                enabled_plugins.append((plugin, mark_safe(content + view)))
            elif plugin.can_configure_for_project(project):
                other_plugins.append(plugin)

        context = {
            'page': 'issue-tracking',
            'enabled_plugins': enabled_plugins,
            'other_plugins': other_plugins,
        }
        return Response({"msg":"ok"},status=200)

    def post(self,request, organization_slug, project_slug):

        project=Project.objects.get(slug=project_slug)
        op = request.POST.get('op')
        if op == 'enable':
            self._handle_enable_plugin(request, project)
            # return HttpResponseRedirect(request.path)
            return Response({"msg":"ok"},status=200)
        elif op == 'disable':
            self._handle_disable_plugin(request, project)
            # return HttpResponseRedirect(request.path)
            return Response({"msg":"ok"},status=200)
