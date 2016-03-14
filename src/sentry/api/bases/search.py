# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""
from sentry.api.base import Endpoint


class SearchEndpoint(Endpoint):
    def convert_args(self, request, *args, **kwargs):
        print args, kwargs.keys()
        return (args, kwargs)
