"""
sentry
~~~~~~

:copyright: (c) 2010-2014 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
from __future__ import absolute_import

import os
import os.path

try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sentry').version
except Exception as e:
    VERSION = 'unknown'


def _get_git_revision(path):
    revision_file = os.path.join(path, 'refs', 'heads', 'master')
    print 'git revision file === ', revision_file
    if not os.path.exists(revision_file):
        print 'None ===='
        return None
    fh = open(revision_file, 'r')
    try:
        return fh.read().strip()
    finally:
        fh.close()


def get_revision():
    """
    :returns: Revision number of this branch/checkout, if available. None if
        no revision number can be determined.
    """
    if 'SENTRY_BUILD' in os.environ:
        return os.environ['SENTRY_BUILD']
    package_dir = os.path.dirname(__file__)
    print 'package_dir === ', package_dir
    checkout_dir = os.path.normpath(os.path.join(package_dir, os.pardir, os.pardir))
    print 'checkout_dir ===', checkout_dir
    path = os.path.join(checkout_dir, '.git')
    print 'path===', path
    if os.path.exists(path):
        return _get_git_revision(path)
    return None


def get_version():
    if __build__:
        return '%s.%s' % (__version__, __build__)
    return __version__

__version__ = VERSION
__build__ = get_revision()
__docformat__ = 'restructuredtext en'
