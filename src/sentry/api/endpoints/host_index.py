# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from __future__ import absolute_import

from rest_framework.response import Response

from sentry.api.base import DocSection
from sentry.api.bases.host import HostEndpoint
from sentry.api.serializers import serialize
from sentry.api.serializers.models.host import HostSerializer
from sentry.models.organizationmember import OrganizationMember
from sentry.models.organization import Organization
from sentry.models import (
    AuditLogEntryEvent, Host, User
)
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.viewsets import ViewSet
from sentry.api.base import Endpoint
from sentry.utils.apidocs import scenario, attach_scenarios
from django.conf import settings
import datetime
import requests
import hashlib


@scenario('CreateNewHost')
def create_new_host_scenario(runner):
    runner.request(method='POST',
                   path='/hosts/' % runner.org.slug,
                   data={'host_nme': 'demo_host', 'system': 'os', 'distver': 'v3.1'})


@scenario('ListHosts')
def list_hosts_scenario(runner):
    runner.request(method='GET', path='/hosts/')


def generate_host_key(result):
    m = hashlib.md5()
    m.update(str(result))
    host_key = m.hexdigest()
    return host_key


class HostIndexEndpoint(HostEndpoint):
    doc_section = DocSection.HOSTS

    @attach_scenarios([list_hosts_scenario])
    def get(self, request):
        """
        List an Organization's hosts
        ````````````````````````````

        Return a list of hosts bound to a organization.

        :pparam string organization_slug: the slug of the organization for
                                          which the teams should be listed.
        :auth: required
        """
        # TODO(dcramer): this should be system-wide default for organization
        # based endpoints
        host_list = list(Host.objects.filter(
            user=request.user
        ).order_by('host_name', 'system'))
        if settings.DEMO_MODAL:
            host = Host.objects.get(id=1)
            host_list.append(host)
        return Response(serialize(
            host_list, request.user, HostSerializer()))

    @attach_scenarios([create_new_host_scenario])
    def post(self, request):
        """
        Create a new host
        ``````````````````

        Create a new host bound to an organization.  Only the name of the
        team is needed to create it, the slug can be auto generated.

        :pparam string organization_slug: the slug of the organization the
                                          team should be created for.
        :param string host_name: the name of the host.
        :param string host_type:  the host type of the host
        :param string system:  the os of the host
        :param string distver:  the os version of the host

        :auth: required
        """
        if settings.DEMO_MODAL:
            result = request.DATA
            org_mem = OrganizationMember.objects.get(user=request.user)
            org = Organization.objects.get(id=org_mem.organization_id)
            hk = generate_host_key(result)
            if not Host.objects.filter(host_key=hk):
                host = Host.objects.create(
                    host_name=result['host_name'],
                    host_key=generate_host_key(result),
                    host_type=result['host_type'],
                    system=result['system'],
                    distver=result['distver'],
                    last_time=str(datetime.datetime.now()),
                    create_time=str(datetime.datetime.now()),
                    user_id=request.user.id,
                    organization=org,
                )
                self.create_audit_entry(
                    request=request,
                    organization=org,
                    target_object=host.id,
                    event=AuditLogEntryEvent.HOST_ADD,
                    data=host.get_audit_log_data(),
                )

                url = "%s/u/%s/nodes/%s/" % (settings.STORAGE_SERVER, request.user.id, host.id)
                host_obj = {"host_key": host.host_key, "user_id": request.user.id, "tenant_id": request.user.id}
                resp = requests.post(url, data=host_obj)
                if resp.status_code > 300:
                    return Response({'msg': 'failed to post stoarge server.'}, status=500)

                return Response({'msg': 'ok'}, status=201)
            return Response({'msg': 'fail'}, status=501)


class LogAgentHostIndexEndpoint(Endpoint):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        result = request.GET
        user = User.objects.get(id=result['user_id'])
        host_list = list(Host.objects.filter(user_id=user.id))
        print list(host_list)

        return Response(serialize(
            host_list, user, HostSerializer()))

    def post(self, request, *args, **kwargs):
        # validate access token
        user_id = self.validate_accesstoken(request.META['HTTP_AUTHORIZATION'], request)
        if user_id == self.INVALID_ACCESS_TOKEN:
            return Response({'msg': 'Invalid access token'}, status=400)

        result = request.DATA
        user = User.objects.get(id=user_id)
        org_mem = OrganizationMember.objects.get(user=user)
        org = Organization.objects.get(id=org_mem.organization_id)
        hk = generate_host_key(result)
        if not Host.objects.filter(host_key=hk):
            # http://192.168.200.245:8080/api/v1/u/1234/nodes/1
            # resp = requests.post(settings.STORAGE_SERVER)

            host = Host.objects.create(
                host_name=result['host_name'],
                host_key=generate_host_key(result),
                host_type=result['host_type'],
                system=result['system'],
                distver=result['distver'],
                last_time=str(datetime.datetime.now()),
                create_time=str(datetime.datetime.now()),
                mac_addr=result.get('mac_addr', ''),
                user_id=user.id,
                organization=org)
            url = "%s/u/%s/nodes/%s/" % (settings.STORAGE_API_BASE_URL, request.user.id, host.id)
            print 'url == ', url
            host_obj = {"host_key": hk, "user_id": user_id, "tenant_id": org.id}
            resp = requests.post(url, data=host_obj)
            print 'code === ', resp.status_code
            if resp.status_code > 200:
                host.delete()
                return Response({'msg': 'failed to post stoarge server.'}, status=400)
            return Response({'action': 'add host', 'host_key': hk, 'msg': 'ok'}, status=200)
        else:
            return Response({'action': 'add host', 'host_key': hk, 'msg': 'host exists!'}, status=200)


class AccessTokenView(Endpoint):
    authentication_classes = []
    permission_classes = []
    required_scopes = ['read']

    def get(self, request):
        # print reques
        authorization = request.META['HTTP_AUTHORIZATION']
        headers = {'Authorization': authorization}
        url = settings.OAUTH_SERVER + "/api/0/access_token"
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            return Response({'ret': 'false'})
        return Response({'ret': 'true'})


class HelloToken(Endpoint):
    permission_classes = []
    required_scopes = ['read']

    def get(self, request):
        return Response({'msg': "hello world"})
