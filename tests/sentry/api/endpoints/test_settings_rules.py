from rest_framework.reverse import reverse
from django.core.urlresolvers import reverse
from sentry.testutils import APITestCase
import logging

class SettingsRulesTest(APITestCase):
    def test_simple(self):
        project = self.create_project()
        self.login_as(user=self.user)
        url = reverse('sentry-project-rules', kwargs={
            'organization_slug': project.organization.slug,
            'project_slug': project.slug,

        })
        response = self.client.get(url)
        # print 'self.content ====== ', response.content
        assert response.status_code == 200
