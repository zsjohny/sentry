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
from qiniu import Auth
from django.conf import settings
from sentry.models.organization import Organization
from sentry.models.organizationmember import OrganizationMember


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
        # print type(org),org.name,
        # organization = Organization.objects.get(id=om.organization_id)
        # print username,org_id
        # token = q.upload_token(bucket_name, key, 3600)
        current_time = now()
        str_ = str(current_time) +"/" +str(org.name)+str(request.user)
        token = q.upload_token(bucket_name, str_, 3600)
        #
        # md5_ = hashlib.md5()
        # md5_.update(str_)
        # md5 = md5_.hexdigest()
        return Response(data={"token":token},status=200)


