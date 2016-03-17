# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: test_react.py
time   : 16/3/15 下午4:19  
"""


from sentry.testutils.cases import APITestCase
from django.core.urlresolvers import reverse


class ReactTest(APITestCase):
    def test_simple(self):
        self.login_as(self.user)
        url = reverse('sentry-api-0-react')
        resp = self.client.get(url)
        assert 200 == resp.status_code, resp.content