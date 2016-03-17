from __future__ import absolute_import

from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from sentry.plugins import plugins
from sentry.web.frontend.base import ProjectView
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
from sentry.plugins import plugins, NotificationPlugin, Annotation
from sentry.utils.safe import safe_execute

from django.utils.safestring import mark_safe


def get_plugins(project):
    results = []
    for plugin in plugins.for_project(project, version=None):
        if plugin.has_project_conf():
            results.append(plugin)
    return results


def get_plugins_with_status(project):
    return [
        (plugin, safe_execute(plugin.is_enabled, project))
        for plugin in plugins.configurable_for_project(project, version=None)
    ]



class ProjectPluginsEndpoint(ProjectEndpoint):
    # required_scope = 'project:write'

    def convert_args(self, request, organization_slug, project_slug, *args, **kwargs):
        kwargs['organization_slug'] = organization_slug
        kwargs['project_slug'] = project_slug
        return (args, kwargs)

    def post(self, request, organization_slug, project_slug):

        print request.POST.getlist('plugins')
        projects = Project.objects.get(slug=project_slug)
        enabled = set(request.POST.getlist('plugin'))

        for plugin in plugins.configurable_for_project(projects, version=None):
            if plugin.slug in enabled:
                plugin.enable(projects)
            else:
                plugin.disable(projects)
        pluginss = get_plugins_with_status(projects)

        return Response(data="ok",status=200)


    def get(self, request, organization_slug, project_slug, *args, **kwargs):

    # organization = Organization.objects.get(slug=organization_slug)

        project = Project.objects.get(slug=project_slug)
        plugins = get_plugins_with_status(project)
        context={}
        for plugin, is_enabled in plugins:
            context[plugin.get_title()]=is_enabled
            # print plugin.get_title(), is_enabled



        return Response (data=context,status=200)



# def handle(self, request, organization, team, project):
#     if request.POST:
#         enabled = set(request.POST.getlist('plugin'))
#         for plugin in plugins.configurable_for_project(project, version=None):
#             if plugin.slug in enabled:
#                 plugin.enable(project)
#             else:
#                 plugin.disable(project)
#
#         messages.add_message(
#             request, messages.SUCCESS,
#             _('Your settings were saved successfully.'))
#
#         return self.redirect(request.path)
#
#     context = {
#         'page': 'plugins',
#     }
#
#     return self.respond('sentry/projects/plugins/list.html', context)
