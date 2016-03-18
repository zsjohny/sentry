# -*- coding: utf-8 -*-
"""
author : xiaoge
company: LogInsight
email_ : duchao@loginsight.cn
file: project_quotas.py
time   : 16/3/18 上午8:27  
"""
from __future__ import absolute_import

from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from rest_framework.response import Response

from sentry import app, features
from sentry.api.bases import ProjectEndpoint
from sentry.models.organization import Organization
from sentry.models.project import Project
from sentry.models.projectoption import ProjectOption
from sentry.quotas.base import Quota
from sentry.web.forms.projects import ProjectQuotasForm
from sentry.web.frontend.base import ProjectView

ERR_NO_SSO = _('The quotas feature is not enabled for this project.')


class ProjectQuotasEndpoint(ProjectEndpoint):
    required_scope = 'project:write'

    def convert_args(self, request, organization_slug, project_slug, *args, **kwargs):
        kwargs['organization_slug'] = organization_slug
        kwargs['project_slug'] = project_slug
        return (args, kwargs)

    def handle(self, request, organization, team, project):
        if not features.has('projects:quotas', project, actor=request.user):
            messages.add_message(
                request, messages.ERROR,
                ERR_NO_SSO,
            )
            redirect = reverse('sentry-manage-project',
                               args=[organization.slug, project.slug])
            return self.redirect(redirect)

        form = ProjectQuotasForm(project, request.POST or None)

        if form and form.is_valid():
            form.save()

            messages.add_message(
                request, messages.SUCCESS,
                _('Your settings were saved successfully.'))

            return self.redirect(reverse('sentry-manage-project-quotas', args=[project.organization.slug, project.slug]))

        context = {
            'organization': organization,
            'team': project.team,
            'page': 'quotas',
            # TODO(dcramer): has_quotas is an awful hack
            'has_quotas': type(app.quotas) != Quota,
            'organization_quota': int(app.quotas.get_organization_quota(project.organization)),
            'project': project,
            'form': form,
        }
        return self.respond('sentry/projects/quotas.html', context)
    def get(self,request, organization_slug, project_slug):
        try:
            project =Project.objects.get(slug=project_slug)
            per_minute = ProjectOption.objects.get_value(
                project, 'quotas:per_minute', None
            )
            if per_minute is None:
                per_minute = settings.SENTRY_DEFAULT_MAX_EVENTS_PER_MINUTE

            print(per_minute)
            content={"per_minute":per_minute}
            return Response(content,status=200)
        except:
            return Response({"msg":"read project from models error"},status=400)
    def post(self,request,organization_slug, project_slug):

        project=Project.objects.get(slug=project_slug)
        organization=Organization.objects.get(slug=organization_slug)
        if not features.has('projects:quotas', project, actor=request.user):
            messages.add_message(
                request, messages.ERROR,
                ERR_NO_SSO,
            )
            redirect = reverse('sentry-manage-project',
                               args=[organization.slug, project.slug])
            return Response("error")

        form = ProjectQuotasForm(project, request.POST or None)

        if form and form.is_valid():
            form.save()

            messages.add_message(
                request, messages.SUCCESS,
                _('Your settings were saved successfully.'))
            return Response({"msg":"ok"},status=200)

        return Response({"msg":"maybe the input number"},status=400)

#