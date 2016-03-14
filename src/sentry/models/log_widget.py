# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from django.db import models
from sentry.models.log_search import Search
from sentry.models.user import User
import datetime


class LogWidget(models.Model):
    title = models.CharField(max_length=512, null=True)
    x_axis = models.CharField(max_length=1024, null=True)
    y_axis = models.CharField(max_length=1024, null=True)
    chart_type = models.CharField(max_length=512, null=True)
    desc = models.CharField(max_length=512, null=True)
    search = models.ForeignKey(Search, null=True)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        app_label = 'sentry'
        db_table = 'sentry_widget'

    def __unicode__(self):
        return self.title
