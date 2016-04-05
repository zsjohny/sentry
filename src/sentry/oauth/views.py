# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: oauth/views.py
time   : 16/4/5 上午10:54
"""

from django.http import  HttpResponseRedirect
from django.views.generic import FormView
from sentry.models.user import User
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from sentry.utils.auth import get_login_redirect
from django.shortcuts import redirect
from sentry.models.organization import Organization
from sentry.models.organizationmember import OrganizationMember
from sentry import roles
import base64
import requests
from .forms import ConsumerExchangeForm
from django.conf import settings
from collections import namedtuple
import hashlib
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from xpinyin import Pinyin
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

ApiUrl = namedtuple('ApiUrl', 'name, url')


class ConsumerExchangeView(FormView):
    """
    The exchange view shows a form to manually perform the auth token swap
    """
    form_class = ConsumerExchangeForm
    template_name = 'example/consumer-exchange.html'

    def generate_user_key(self, username, email, password):
        data = username + email + password
        hash_md5 = hashlib.md5(data)
        return hash_md5.hexdigest()

    def get(self, request, *args, **kwargs):
        try:
            print request.GET
            self.initial = {
                'code': request.GET['code'],
                'state': request.GET['state'],
                'client_id': settings.DEFALUT_SENTRY_CLIENT_ID,
                'client_secret': settings.DEFALUT_SENTRY_CLIENT_SECRET,
                'token_url': settings.TOKEN_URL,
                'redirect_url': request.build_absolute_uri(reverse('oauth-consumer-exchange'))
            }
            headers = {"Authorization": "Basic " + base64.b64encode(settings.DEFALUT_SENTRY_CLIENT_ID + ":" + settings.DEFALUT_SENTRY_CLIENT_SECRET)}
            data = {'code': request.GET['code'],
                    'redirect_uri': request.build_absolute_uri(reverse('oauth-consumer-exchange')),
                    'grant_type': 'authorization_code'}
            resp = requests.post(settings.TOKEN_URL,
                                 data=data,
                                 headers=headers
                                 )
            data = resp.json()
            token = data['access_token']
            token_type = data['token_type']
            headers = {"Authorization": token_type + " " + token}

            resp = requests.post(settings.OAUTH_SERVER + "/api/user_info", data={'token': token}, headers=headers)
            data = resp.json()[0]['fields']
            user_key = self.generate_user_key(data['username'], data['email'], data['password'])
            user = User(username=data['username'], email=data['email'])
            user.password = data['password']
            user.userkey = user_key
            user.is_active = True
            user.is_managed = True
            user.is_staff = True
            try:
                u = User.objects.get(username=data['username'])
                uliste = User.objects.get(email=data['email'])
                print 'ulist = ', u
            except ObjectDoesNotExist:
                user.save()
            user = User.objects.get(username=data['username'])
            data = resp.json()[1]['fields']
            org_name = data['org_name'] + str(user.id)
            # create organization
            # m = hashlib.md5()
            # m.update(str(datetime.now()))
            # org_slug = m.hexdigest()
            print 'data == ', data
            print 'org_name=', org_name
            p = Pinyin()
            org_slug = p.get_pinyin(org_name).replace('-', '')
            if len(Organization.objects.filter(slug=org_slug)) == 0:
                org = Organization.objects.create(
                    name=org_name,
                    slug=org_slug,
                )

                OrganizationMember.objects.create(
                    organization=org,
                    user=user,
                    role=roles.get_top_dog().id,
                )

            if request.user.is_authenticated():
                # Do something for authenticated users.
                if request.user != data['name']:
                    logout(request)
                    user = authenticate(username=data['name'], password=data['password'])
                    login(request, user)
                uri = reverse('sentry-organization-home', args=[org_slug])
                return redirect(uri)
            else:
                # Do something for anonymous users.
                user = authenticate(username=data['name'], password=data['password'])
                login(request, user)
                if user is None:
                    return redirect('sentry-login')
                return HttpResponseRedirect(get_login_redirect(request))
        except KeyError:
            kwargs['noparams'] = True

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form, **kwargs))

