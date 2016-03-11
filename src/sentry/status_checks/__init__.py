from __future__ import absolute_import

__all__ = (
    'Problem',
    'SEVERITY_CRITICAL',
    'SEVERITY_WARNING',
    'StatusCheck',
    'check_all',
    'severity_threshold',
)

from .base import Problem, StatusCheck, SEVERITY_CRITICAL, SEVERITY_WARNING, severity_threshold  # NOQA
from .celery_alive import CeleryAliveCheck
from .celery_app_version import CeleryAppVersionCheck


checks = [
    CeleryAliveCheck(),
    CeleryAppVersionCheck(),
]


def check_all():
    return {check: check.check() for check in checks}
