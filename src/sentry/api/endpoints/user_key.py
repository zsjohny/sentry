# -*- coding: utf-8 -*-
"""
__author__ = 'wanghe'
__company__ = 'LogInsight'
__email__ = 'wangh@loginsight.cn'
"""
from __future__ import absolute_import
from rest_framework.response import Response
from sentry.api.base import Endpoint
from sentry.models.user import User
from rest_framework import mixins
from rest_framework import generics
import hashlib
import datetime


def generate_user_key(user):
    data = user.username + user.email + user.password + str(datetime.datetime.now())
    hash_md5 = hashlib.md5(data)
    return hash_md5.hexdigest()


class UserkeyEndpoint(Endpoint,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    """
     GET /api/0/user_key
     授权方式 : basic auth (username/password)
     描述:  获取USER_KEY

     POST /api/0/user
    授权方式: basic auth (username/password)
    描述: 更新USER_KEY
    """
    # authentication_classes = [QuietBasicAuthentication]
    permission_classes = ()

    # XXX: it's not quite clear if this should be documented or not at
    # this time.
    # doc_section = DocSection.ACCOUNTS
    queryset = User.objects.all()

    def get(self, request):
        user = User.objects.get(username=request.user.username)
        resp = {'user_key': user.userkey}
        return Response(resp)

    def post(self, request):
        # user = User.objects.get(username=request.user.username)
        # user_key = generate_user_key(user)
        # if User.objects.filter(username=request.user.username).update(userkey=user_key):
        #     return Response({'msg': 'ok'})
        # return Response({'msg': 'failed'})
        print 'request.data ', request.DATA
        result = request.DATA
        print 'username = ', result['username']
        print 'password= ', result['password']
        user = User.objects.get(username=result['username'])
        resp = {'user_key': user.userkey}
        print 'resp=', resp
        return Response(resp)
