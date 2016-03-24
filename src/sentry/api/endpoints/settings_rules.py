# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from sentry.rules import rules
from sentry.models.rule import Rule
from sentry.models.log_search import Search
from rest_framework.response import Response
from sentry.models.project import Project
from sentry.models.organization import Organization
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from sentry.api.base import Endpoint
from sentry.utils.query_parse import *
import requests
import ast

def _generate_rule_label(project, rule, data):
    rule_cls = rules.get(data['id'])
    if rule_cls is None:
        return

    rule_inst = rule_cls(project, data=data, rule=rule)
    return rule_inst.render_label()


class SettingsRulesEndpoint(Endpoint):
    # required_scope = 'project:write'
    permission_classes = []

    def convert_args(self, request, organization_slug,  project_slug, *args, **kwargs):
        kwargs['organization_slug'] = organization_slug
        kwargs['project_slug'] = project_slug
        print 'prj ==== ', project_slug
        return (args, kwargs)

    def get(self,request, organization_slug, project_slug,*args, **kwargs):
        rule_list = []
        try:
            organization = Organization.objects.get(name=organization_slug)
            project = Project.objects.get(slug=project_slug)
            for rule in Rule.objects.filter(project=project):
                conditions = []
                for data in rule.data['conditions']:
                    conditions.append(_generate_rule_label(project, rule, data))
                conditions = filter(bool, conditions)
                actions = []
                for data in rule.data['actions']:
                    actions.append(_generate_rule_label(project, rule, data))
                actions = filter(bool, actions)
                rule_list.append({
                    'id': rule.id,
                    'label': rule.label,
                    'match': rule.data.get('action_match', 'all'),
                    'actions': actions,
                    'conditions': conditions,
                })
                context = {
                'page': 'rules',
                'rule_list': rule_list,
            }
            print type(context)
            for key in context:
                print key,context[key]
            return Response(data=context, status=200)
        except ObjectDoesNotExist:
            return Response(data={'error': 'can not find object for organization or project', 'code': '40001'},
                            status=400)


# def _generate_rule_label(project, rule, data):
#     rule_cls = rules.get(data['id'])
#     if rule_cls is None:
#         return
#
#     rule_inst = rule_cls(project, data=data, rule=rule)
#     return rule_inst.render_label()
#
#
# class ProjectRulesView(ProjectView):
#     required_scope = 'project:write'
#
#     def get(self, request, organization, team, project):
#         rule_list = []
#         for rule in Rule.objects.filter(project=project):
#             conditions = []
#             for data in rule.data['conditions']:
#                 conditions.append(_generate_rule_label(project, rule, data))
#             conditions = filter(bool, conditions)
#
#             actions = []
#             for data in rule.data['actions']:
#                 actions.append(_generate_rule_label(project, rule, data))
#             actions = filter(bool, actions)
#
            # rule_list.append({
            #     'id': rule.id,
            #     'label': rule.label,
            #     'match': rule.data.get('action_match', 'all'),
            #     'actions': actions,
            #     'conditions': conditions,
            # })
#
        # context = {
        #     'page': 'rules',
        #     'rule_list': rule_list,
        # }
#
#         return self.respond('sentry/projects/rules/list.html', context)


