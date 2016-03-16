# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from __future__ import absolute_import
from sentry.api.bases.project import ProjectEndpoint
from sentry.models.project import Project
from sentry.models.team import Team
from sentry.models.organization import Organization
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from uuid import uuid1


class ProjectSettingsEndpoint(ProjectEndpoint):
    def convert_args(self, request, organization_slug, project_slug, *args, **kwargs):
        kwargs['organization_slug'] = organization_slug,
        kwargs['project_slug'] = project_slug
        return (args, kwargs)

    def get(self, request, organization_slug, project_slug,  *args, **kwargs):
        try:
            organization = Organization.objects.get(slug=organization_slug)
            project = Project.objects.get(slug=project_slug)
            team_list = [
                t for t in Team.objects.get_for_user(
                    organization=organization,
                    user=request.user,
                )
                if request.access.has_team_scope(t, self.required_scope)
            ]

            # TODO(dcramer): this update should happen within a lock
            security_token = project.get_option('sentry:token', None)
            if security_token is None:
                security_token = uuid1().hex
                project.update_option('sentry:token', security_token)

                content = {
                    'origins': '\n'.join(project.get_option('sentry:origins', ['*'])),
                    'token': security_token,
                    'resolve_age': int(project.get_option('sentry:resolve_age', 0)),
                    'scrub_data': bool(project.get_option('sentry:scrub_data', True)),
                    'scrub_defaults': bool(project.get_option('sentry:scrub_defaults', True)),
                    'sensitive_fields': '\n'.join(project.get_option('sentry:sensitive_fields', None) or []),
                    'scrub_ip_address': bool(project.get_option('sentry:scrub_ip_address', False)),
                    'scrape_javascript': bool(project.get_option('sentry:scrape_javascript', True)),
                    'blacklisted_ips': '\n'.join(project.get_option('sentry:blacklisted_ips', [])),
                    'project_details': {
                        'name': project.name,
                        'slug': project.slug,
                        'team_list': team_list,
                    },
                },
                return Response(data=content, status=200)
        except ObjectDoesNotExist:
            return Response(data={'error': 'cannot find organization or project ', 'code': '4000'}, status=400)

    def post(self, request, *args, **kwargs):
         for opt in (
                    'origins',
                    'token',
                    'resolve_age',
                    'scrub_data',
                    'scrub_defaults',
                    'sensitive_fields',
                    'scrub_ip_address',
                    'scrape_javascript',
                    'blacklisted_ips'):
                # # Value can't be overridden if set on the org level
                # if opt in form.org_overrides and organization.get_option('sentry:%s' % (opt,), False):
                #     continue
                value = request.DATA.get(opt)
                # if value is None:
                #     project.delete_option('sentry:%s' % (opt,))
                # else:
                #     project.update_option('sentry:%s' % (opt,), value)
                #
            # project.update_option('sentry:reviewed-callsign', True)

    def put(self, request):
        pass
        
    def delete(self, request):
        pass
