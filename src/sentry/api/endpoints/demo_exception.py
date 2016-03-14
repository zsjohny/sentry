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
    # serializer_class = HostSerializer
    # queryset = Host.objects.all()

    permission_classes = ()
    PROCESS_PERCENT = 0

    def get(self, request):
        return Response({'msg': load_demo.PROCESS_PERCENT})

    def post(self, request):
        org_member = OrganizationMember.objects.get(user_id=request.user.id)
        org = Organization.objects.get(id=org_member.organization_id)
        load_demo.create_demo_sample(num_events=1, org_name=org.name, user_name=request.user.username, request=request)
        return Response({'msg': 'ok'})
