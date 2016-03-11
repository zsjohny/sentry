from __future__ import absolute_import


class Problem(object):
    # Used for issues that may render the system inoperable or have effects on
    # data integrity (e.g. issues in the processing pipeline.)
    SEVERITY_CRITICAL = 'critical'

    # Used for issues that may cause the system to operate in a degraded (but
    # still operational) state, as well as configuration options that are set
    # in unexpected ways or deprecated in future versions.
    SEVERITY_WARNING = 'warning'

    SEVERITY_LEVELS = frozenset((
        SEVERITY_CRITICAL,
        SEVERITY_WARNING,
    ))

    def __init__(self, message, severity=SEVERITY_CRITICAL):
        assert severity in self.SEVERITY_LEVELS
        self.message = unicode(message)
        self.severity = severity

    def __str__(self):
        return self.message.encode('utf-8')

    def __unicode__(self):
        return self.message


class StatusCheck(object):
    def check(self):
        """
        Perform required checks and return a list of ``Problem`` instances.
        """
        raise NotImplementedError
