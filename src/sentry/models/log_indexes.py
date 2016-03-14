# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from __future__ import unicode_literals
from django.db import models
from sentry.models.user import User
import datetime


class Indexes(models.Model):
    name = models.CharField(max_length=512)
    type = models.CharField(max_length=512, null=True)
    dsn = models.CharField(max_length=512, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), null=True)
    desc = models.CharField(max_length=512, null=True)
    user = models.ForeignKey(User)

    class Meta:
        app_label = 'sentry'
        db_table = 'sentry_indexes'

    def __unicode__(self):
        return self.name
