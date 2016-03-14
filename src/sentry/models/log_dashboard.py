# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""
from __future__ import unicode_literals
from sentry.models.user import User
from django.db import models


class LogDashboard(models.Model):
    name = models.CharField(max_length=512, null=True)
    desc = models.CharField(max_length=512, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    is_fav = models.BooleanField(default=False)
    layout = models.CharField(max_length=512 * 1024)
    config = models.CharField(max_length=512, null=True)
    user = models.ForeignKey(User)

    class Meta:
        app_label = 'sentry'
        db_table = 'sentry_log_dashboard'

    def __unicode__(self):
        return self.title
