# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from django.db import models
from sentry.models.user import User
import datetime


class Search(models.Model):
    name = models.CharField(max_length=1024, null=True)
    create_timestamp = models.DateTimeField(default=datetime.datetime.now(), null=True)
    last_timestamp = models.DateTimeField(default=datetime.datetime.now(), null=True)
    query = models.CharField(max_length=1024 * 1024, null=True)
    time_range = models.CharField(max_length=512, null=True)
    config = models.CharField(max_length=512, null=True)
    desc = models.CharField(max_length=512, null=True)
    user = models.ForeignKey(User)

    class Meta:
        app_label = 'sentry'
        db_table = 'sentry_search'

    def __unicode__(self):
        return self.name
