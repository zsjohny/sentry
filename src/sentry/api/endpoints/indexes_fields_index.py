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

"""
    URI /api/0/indexes/<index_id>/fields/

"""


class IndexesFieldsIndexEndpoint(Endpoint):
    permission_classes = []

    def convert_args(self, request, index_id, *args, **kwargs):
        kwargs['index_id'] = index_id
        return (args, kwargs)

    def get(self, request, index_id, *args, **kwargs):
        if index_id is not None:
            try:
                index = Indexes.objects.get(id=index_id)
            except ObjectDoesNotExist:
                return Response(status=400, data={'msg': 'Object does not exist!'})
            url = "%s/%s/%s/" % (settings.STORAGE_SERVER, request.user.id, index_id)
            response = requests.get(url)
            return Response(response.json(), status=response.status_code)
