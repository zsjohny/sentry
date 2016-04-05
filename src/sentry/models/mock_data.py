# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: mock_data.py
time   : 16/4/5 上午10:54  
"""

from django.db import models
from sentry.db.models import sane_repr


class MockData(models.Model):
    remote_addr = models.CharField(max_length=128, null=True)
    remote_user = models.CharField(max_length=128, null=True)
    _timestamp = models.CharField(max_length=128, null=True)
    method = models.CharField(max_length=128, null=True)
    url = models.CharField(max_length=512, null=True)
    protocol = models.CharField(max_length=512, null=True)
    status = models.CharField(max_length=512, null=True)
    body_bytes_sent = models.CharField(max_length=512, null=True)
    http_referer = models.CharField(max_length=512, null=True)
    http_user_agent = models.CharField(max_length=512, null=True)
    http_x_forwarded_for = models.CharField(max_length=512, null=True)
    _raw = models.CharField(max_length=512, null=True)

    class Meta:
        app_label = 'sentry'
        db_table = 'sentry_mock_data'

    __repr__ = sane_repr('remote_addr', 'remote_user', '_timestamp', 'method', 'url', 'protocol',
                         'status', 'body_bytes_sent', 'http_referer', '_raw',)
