# -*- coding: utf-8 -*-
"""
author : xiaoge
company: LogInsight
email_ : duchao@loginsight.cn
file: test_project_notifications.py.py
time   : 16/3/15 下午8:30  
"""
from __future__ import absolute_import

from django.core.urlresolvers import reverse

from sentry.testutils import APITestCase


class ProjectNotificationsTest(APITestCase):
    def test_simple(self):

        self.login_as(user=self.user)
        organization = self.create_organization()
        project = self.create_project()

        url = reverse('sentry-api-0-project-notifications', kwargs={
            'organization_slug': organization.slug,
            'project_slug': project.slug,
        })

        response = self.client.get(url)
        assert response.status_code == 200, response.content

