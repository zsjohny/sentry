# -*- coding: utf-8 -*-
"""
author : xiaoge
company: LogInsight
email_ : duchao@loginsight.cn
file: configure.py
time   : 16/3/21 下午4:29  
"""

from django.utils.translation import ugettext_lazy as _
from rest_framework.response import Response
from sentry.models.user import User
from django.contrib.auth.models import Group
from sentry.api.bases import Endpoint
'''
when user configure the agent ,get the user info

'''


class LogAgentUserInfoEndpoint(Endpoint):
    required_scope = 'project:write'
    permission_classes = []

    def get(self,request):
        user = request.user
        resp = {'name': user.username,'key':None}
        return Response(resp,status=200)


from rest_framework import viewsets
from sentry.api.serializers.models.user import UserDemoSerializer, GroupDemoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserDemoSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupDemoSerializer
