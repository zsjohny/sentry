from __future__ import absolute_import

# Used for issues that may render the system inoperable or have effects on
# data integrity (e.g. issues in the processing pipeline.)
SEVERITY_CRITICAL = 'critical'

# Used for issues that may cause the system to operate in a degraded (but
# still operational) state, as well as configuration options that are set
# in unexpected ways or deprecated in future versions.
SEVERITY_WARNING = 'warning'

# Mapping of severity level to a priority score, where the greater the
# score, the more critical the issue. (The numeric values should only be
# used for comparison purposes, and are subject to change as levels are
# modified.)
SEVERITY_LEVELS = {
    SEVERITY_CRITICAL: 2,
    SEVERITY_WARNING: 1,
}


def severity_threshold(level):
    threshold = SEVERITY_LEVELS[level]

    def predicate(problem):
        return SEVERITY_LEVELS[problem.severity] >= threshold

    return predicate


class Problem(object):
    def __init__(self, message, severity=SEVERITY_CRITICAL):
        assert severity in SEVERITY_LEVELS
        self.message = unicode(message)
        self.severity = severity

    def __cmp__(self, other):
        if not isinstance(other, Problem):
            return NotImplemented

        return cmp(
            SEVERITY_LEVELS[self.severity],
            SEVERITY_LEVELS[other.severity],
        )

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
