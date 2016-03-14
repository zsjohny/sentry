# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""


from __future__ import absolute_import, print_function

from django import template
import os
register = template.Library()
import re


class EnvNode(template.Node):
    def __init__(self, key, var_name):
        self.key = key
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = os.environ.get(self.key)
        return ''


def test_env(parser, token):

    try:
        # tag_name, key = token.split_contents()
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        msg = '%r tag requires arguments' % token.contents.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    m = re.search(r'(.*?) as (\w+)', arg)
    print(arg)
    if m:
        key, var_name = m.groups()
        print(key, var_name)
    else:
        msg = '%r tag had invalid arguments' % tag_name
        raise template.TemplateSyntaxError(msg)
    if not (key[0] == key[-1] and key[0] in ('"', "'")):
        msg = "%r tag's argument should be in quotes" % tag_name
        raise template.TemplateSyntaxError(msg)
    return EnvNode(key[1:-1], var_name)

register.tag('env', test_env)
