# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from sentry.testutils.cases import APITestCase
from django.core.urlresolvers import reverse
from uuid import uuid4
import random

class ProjectRuleListTest(APITestCase):
    """
    项目设置 project settings
    事件设置 event settings
    """
    def test_simple(self):
        # org = self.create_organization(owner=self.user)
        # self.login_as(user=self.user)
        # response = self.client.get('{}?member=1'.format(self.path))
        # assert response.status_code == 200
        # assert len(response.data) == 1
        # assert response.data[0]['id'] == str(org.id)

        # self.login_as(user=self.user)
        #
        # #project settings
        # project = self.create_project()
        # team = self.create_team()
        # url = reverse('sentry-api-0-project-settings', kwargs={
        #     'id': project.id,
        #     'organization_slug': project.organization.slug,
        #     'project_slug': project.slug,
        #     'team_id': team.id,
        #     'origins' : uuid4().hex,
        #     'token': uuid4().hex,
        #     'resolve_age': random.randint(0, 100),
        #     'scrub_data': uuid4().hex,
        #     'scrub_defaults': uuid4().hex,
        #     'sensitive_fields': uuid4().hex,
        #     'scrub_ip_address': '120.1.1.1',
        #     'scrape_javascript': uuid4().hex,
        #     'blacklisted_ips': uuid4().hex,
        # })
        # response = self.client.get(url, format='json')
        # assert response.status_code == 200, response.content
        pass



