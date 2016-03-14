# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from __future__ import unicode_literals
from sentry.models.user import User
from django.db import models
import datetime


class Visaulization(models.Model):
    name = models.CharField(max_length=512)
    desc = models.CharField(max_length=512, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), null=True)
    is_fav = models.BooleanField(default=False)
    layout = models.CharField(max_length=512, null=True)
    user = models.ForeignKey(User)

    class Meta:
        app_label = 'sentry'
        db_table = 'sentry_visualization'

    def __unicode__(self):
        return self.name
