# -*- coding: utf-8 -*-
__author__ = 'wanghe'
__company__ = 'LogInsight'
__email__ = 'wangh@loginsight.cn'

from sentry.models.organizationmember import OrganizationMember
from sentry.models.organization import Organization
from sentry.api.base import Endpoint
from sentry.utils import load_demo
from rest_framework.response import Response


class DemoExceptionEndpoint(Endpoint):
    """
      POST /demo_exception
    """

    permission_classes = ()
    PROCESS_PERCENT = 0

    def get(self, request):
        return Response({'msg': ''})

    def post(self, request):
        try:
            org_member = OrganizationMember.objects.get(user_id=request.user.id)
            org = Organization.objects.get(id=org_member.organization_id)
            print 'org.slug == ', org.slug
            load_demo.create_demo_sample(num_events=1, org_slug=org.slug, user_name=request.user.username, request=request)
        except Exception:
            return Response({'msg': 'failed'})
        return Response({'msg': 'ok'})
