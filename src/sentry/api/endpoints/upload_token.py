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
from django.conf import settings
from sentry.models.organization import Organization
from sentry.models.organizationmember import OrganizationMember
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import time


class UploadTokenEndpoint(Endpoint):
    permission_classes = []

    def get(self, request):

        print request.GET
        access_key = settings.ACCESS_KEY
        secret_key = settings.SECRET_KEY
        bucket_name = settings.QINIU_SPACE
        q = Auth(access_key, secret_key)

        om  = OrganizationMember.objects.get(user_id=request.user.id)
        org = om.organization
        if "name" in request.GET:
            if request.GET["name"] =="":
                return Response(data={"msg":'filename invalid'})
            else:
                str_ = str(int(time.time())) +"/" +str(org.name)+'/'+str(request.user)+'/'+request.GET["name"]
                try:
                    token = q.upload_token(bucket_name, str_, 3600)
                except:

                    return Response(data={"msg":"fetch qiniu token error"})
                return Response(data={"token":token,"key":str_},status=200)
        else:
            return Response(data={"msg":'filename invalid'})

