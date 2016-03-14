# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from sentry.api.base import Endpoint
from rest_framework.response import Response
from sentry.models.organizationmember import OrganizationMember
from sentry.models.organization import Organization
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from sentry.utils.sourcetype import *

import os


class UploadIndexEndpoint(Endpoint):
    permission_classes = []
    LOG_SAMPLE = ""

    def handle_upload_file(self, request, org, file):
        if file is None:
            return None
        # 读取默认配置的目录
        LOG_ROOT = settings.LOG_ROOT
        # 检查目录是否存在
        if not os.path.exists(LOG_ROOT):
            os.makedirs(LOG_ROOT)

        dest_path = os.path.join(LOG_ROOT, org, request.user.username)
        # 创建组织/用户子目录

        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        dest_path = os.path.join(dest_path, file.name)
        destination = open(dest_path, 'wb+')
        ret = None
        chunks = []
        i = 0
        for chunk in file.chunks():
            destination.write(chunk)
            i = i + 1
            if i != 20:
                chunks.append(chunks)
        destination.close()
        with open(dest_path, "r") as fd:
            lines = fd.readlines(20)
            a = try_to_detect_file_sourcetype(lines, "")
            return a

    def get(self, request):
        pass

    def post(self, request):
        file = request.FILES.get('file', None)
        try:
            org_mem = OrganizationMember.objects.get(user_id=request.user.id)
            org = Organization.objects.get(id=org_mem.organization_id)
        except ObjectDoesNotExist:
            return Response(status=200, data={'msg': 'Invalid user for organization'})
        ret = self.handle_upload_file(request, org.name, file)
        print 'ret === ', ret
        return Response(status=200, data={'msg': 'ok', 'source_type': ret})