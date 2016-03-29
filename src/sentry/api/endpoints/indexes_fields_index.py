# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""


from sentry.api.base import Endpoint

from sentry.models.log_indexes import Indexes
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import requests
from sentry.extract import mock_func

"""
    URI /api/0/indexes/<index_id>/fields/

"""


class IndexesFieldsIndexEndpoint(Endpoint):
    permission_classes = []

    def convert_args(self, request, index_name, *args, **kwargs):
        kwargs['index_name'] = index_name
        return (args, kwargs)

    def get(self, request, index_name, *args, **kwargs):
        if index_name is not None:
            # try:
            #     index = Indexes.objects.get(user_id=request.user.id, name=index_name)
            # except ObjectDoesNotExist:
            #     return Response(status=400, data={'msg': 'Object does not exist!'})
            url = "%s/tenant/%s/%s/fields/" % (settings.SEARCH_SERVER_API, request.user.username, index_name)
            response = requests.get(url)
            print response.status_code
            return Response(data=response.json(), status=response.status_code)

'''
uee for mock data
'''
class IndexesFieldsCountIndexEndpoint(Endpoint):
    permission_classes = []
    def convert_args(self, request, index_name, *args, **kwargs):
        kwargs['index_name'] = index_name
        return (args, kwargs)

    def get(self, request, index_name, *args, **kwargs):

        data = mock_func()

        for key in data:
            if
        data ="hello"
        return Response(data, status=200)