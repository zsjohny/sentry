from __future__ import absolute_import

import itertools

from django.http import HttpResponse


class HealthCheck(object):
    def process_request(self, request):
        # Our health check can't be a done as a view, because we need
        # to bypass the ALLOWED_HOSTS check. We need to do this
        # since not all load balancers can send the expected Host header
        # which would cause a 400 BAD REQUEST, marking the node dead.
        # Instead, we just intercept the request at this point, and return
        # our success/failure immediately.
        if request.path != '/_health/':
            return

        if 'full' not in request.GET:
            return HttpResponse('ok', content_type='text/plain')

        from sentry.status_checks import check_all
        from sentry.utils import json

        results = check_all()
        problems = list(itertools.chain.from_iterable(results.values()))
        return HttpResponse(json.dumps({
            'problems': map(
                lambda problem: {
                    'message': problem.message,
                    'severity': problem.severity,
                },
                problems,
            ),
            'healthy': {type(check).__name__: not problems for check, problems in results.items()},
        }), content_type='application/json', status=(500 if problems else 200))
