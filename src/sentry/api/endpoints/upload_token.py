# -*- coding: utf-8 -*-
"""
author : xiaoge
company: LogInsight
email_ : duchao@loginsight.cn
file: upload_token.py
time   : 16/4/5 下午3:21  
"""
from sentry.api.base import Endpoint
from rest_framework.response import Response
import hashlib
from django.utils.timezone import now

class UploadTokenEndpoint(Endpoint):
    permission_classes = []

    def get(self, request):

        current_time = now()
        str_ = str(current_time) + str(request.user)
        md5_ = hashlib.md5()
        md5_.update(str_)
        md5 = md5_.hexdigest()
        return Response(data={"md5":md5},status=200)

    def post(self, request):
        pass
