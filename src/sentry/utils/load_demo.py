#!/usr/bin/env python

from sentry.utils.runner import configure
configure()

import itertools

from datetime import datetime, timedelta
from django.conf import settings
from django.db import IntegrityError, transaction
from hashlib import md5
from pytz import utc
from random import randint

from sentry import roles
from sentry.app import tsdb, buffer
from sentry.models import (Activity, Broadcast, File, GroupMeta, Organization,
                           OrganizationAccessRequest, OrganizationMember, Project,
                           Release, ReleaseFile, Team, User, UserReport, OrganizationMemberTeam)
from sentry.utils.samples import create_sample_event
from sentry.models.host_stream import Host
import hashlib

PLATFORMS = itertools.cycle([
    'ruby',
    'php',
    'python',
    'java',
    'javascript',
])

LEVELS = itertools.cycle([
    'error',
    'error',
    'error',
    'fatal',
    'warning',
])


def create_system_time_series():
    now = datetime.utcnow().replace(tzinfo=utc)

    for _ in xrange(60):
        count = randint(1, 10)
        tsdb.incr_multi((
            (tsdb.models.internal, 'client-api.all-versions.responses.2xx'),
            (tsdb.models.internal, 'client-api.all-versions.requests'),
        ), now, int(count * 0.9))
        tsdb.incr_multi((
            (tsdb.models.internal, 'client-api.all-versions.responses.4xx'),
        ), now, int(count * 0.05))
        tsdb.incr_multi((
            (tsdb.models.internal, 'client-api.all-versions.responses.5xx'),
        ), now, int(count * 0.1))
        now = now - timedelta(seconds=1)

    for _ in xrange(24 * 30):
        count = randint(100, 1000)
        tsdb.incr_multi((
            (tsdb.models.internal, 'client-api.all-versions.responses.2xx'),
            (tsdb.models.internal, 'client-api.all-versions.requests'),
        ), now, int(count * 4.9))
        tsdb.incr_multi((
            (tsdb.models.internal, 'client-api.all-versions.responses.4xx'),
        ), now, int(count * 0.05))
        tsdb.incr_multi((
            (tsdb.models.internal, 'client-api.all-versions.responses.5xx'),
        ), now, int(count * 0.1))
        now = now - timedelta(hours=1)


def create_sample_time_series(event):
    group = event.group

    now = datetime.utcnow().replace(tzinfo=utc)

    for _ in xrange(60):
        count = randint(1, 10)
        tsdb.incr_multi((
            (tsdb.models.project, group.project.id),
            (tsdb.models.group, group.id),
        ), now, count)
        tsdb.incr_multi((
            (tsdb.models.organization_total_received, group.project.organization_id),
            (tsdb.models.project_total_received, group.project.id),
        ), now, int(count * 1.1))
        tsdb.incr_multi((
            (tsdb.models.organization_total_rejected, group.project.organization_id),
            (tsdb.models.project_total_rejected, group.project.id),
        ), now, int(count * 0.1))
        now = now - timedelta(seconds=1)

    for _ in xrange(24 * 30):
        count = randint(100, 1000)
        tsdb.incr_multi((
            (tsdb.models.project, group.project.id),
            (tsdb.models.group, group.id),
        ), now, count)
        tsdb.incr_multi((
            (tsdb.models.organization_total_received, group.project.organization_id),
            (tsdb.models.project_total_received, group.project.id),
        ), now, int(count * 1.1))
        tsdb.incr_multi((
            (tsdb.models.organization_total_rejected, group.project.organization_id),
            (tsdb.models.project_total_rejected, group.project.id),
        ), now, int(count * 0.1))
        now = now - timedelta(hours=1)


def generate_host_key(result):
    m = hashlib.md5('x')
    m.update(str(result))
    host_key = m.hexdigest()
    return host_key


def create_demo_sample(num_events=1, user_name="dummy@example.com", org_name='default', request=None):

    dummy_user, _ = User.objects.get_or_create(
        username=user_name,
        defaults={
            'email': user_name,
        }
    )
    # dummy_user.set_password('123')
    # dummy_user.save()

    mocks = (
        ('Massive Dynamic', ('Ludic Science',)),
        ('Captain Planet', ('Earth',)),
    )
    Broadcast.objects.create(
        title="Learn about Source Maps",
        message="Source maps are JSON files that contain information on how to map your transpiled source code back to their original source.",
        link="https://docs.getsentry.com/hosted/clients/javascript/sourcemaps/#uploading-source-maps-to-sentry",
    )
    if settings.SENTRY_SINGLE_ORGANIZATION:
        org = Organization.get_default()
    else:
        print('Mocking org {}'.format('Default'))
        org, _ = Organization.objects.get_or_create(
            name=org_name,
        )
    OrganizationMember.objects.get_or_create(
        user=dummy_user,
        organization=org,
        role=roles.get_top_dog().id,
    )

    dummy_member, _ = OrganizationMember.objects.get_or_create(
        user=dummy_user,
        organization=org,
        defaults={
            'role': roles.get_default().id,
        }
    )

    for team_name, project_names in mocks:
        print('> Mocking team {}'.format(team_name))
        team, _ = Team.objects.get_or_create(
            name=team_name,
            defaults={
                'organization': org,
            }
        )

        print('create organizationmemberteam ')
        OrganizationMemberTeam.objects.create(team=team,
                                              organizationmember=dummy_member,
                                              is_active=True)
        for project_name in project_names:
            print('  > Mocking project {}'.format(project_name))
            project, _ = Project.objects.get_or_create(team=team,
                                                       name=project_name,
                                                       defaults={'organization': org})
            release = Release.objects.get_or_create(version='4f38b65c62c4565aa94bba391ff8946922a8eed4',
                                                    project=project)[0]
            ReleaseFile.objects.get_or_create(
                project=project,
                release=release,
                name='an-example.js',
                file=File.objects.get_or_create(
                    name='an-example.js',
                    type='release.file',
                    checksum='abcde' * 8,
                    size=13043,
                )[0],
            )

            Activity.objects.create(
                type=Activity.RELEASE,
                project=project,
                ident=release.version,
                user=dummy_user,
                data={'version': release.version},
            )

            # Add a bunch of additional dummy events to support pagination
            for _ in range(45):
                platform = PLATFORMS.next()
                create_sample_event(
                    project=project,
                    platform=platform,
                    release=release.version,
                    level=LEVELS.next(),
                    message='This is a mostly useless example %s exception' % platform,
                    checksum=md5(platform + str(_)).hexdigest(),
                )

            for _ in range(num_events):
                event1 = create_sample_event(
                    project=project,
                    platform='python',
                    release=release.version,
                )

                event2 = create_sample_event(
                    project=project,
                    platform='javascript',
                    release=release.version,
                )

                event3 = create_sample_event(project, 'java')

                event4 = create_sample_event(
                    project=project,
                    platform='ruby',
                    release=release.version,
                )

                create_sample_event(
                    project=project,
                    platform='php',
                    release=release.version,
                    message='This is a an example PHP event with an extremely long and annoying title\nIt also happens to contain some newlines in it,\nthus making it even more annoying.',
                )

            with transaction.atomic():
                try:
                    GroupMeta.objects.create(
                        group=event1.group,
                        key='github:tid',
                        value='134',
                    )
                except IntegrityError:
                    pass

            UserReport.objects.create(
                project=project,
                event_id=event3.event_id,
                group=event3.group,
                name='Jane Doe',
                email='jane@example.com',
                comments='I have no idea how I got here.',
            )

            print('    > Loading time series data'.format(project_name))

            create_sample_time_series(event1)
            create_sample_time_series(event2)
            create_sample_time_series(event3)
            create_sample_time_series(event4)

            if hasattr(buffer, 'process_pending'):
                print('    > Processing pending buffers')
                buffer.process_pending()

        OrganizationAccessRequest.objects.create_or_update(
            member=dummy_member,
            team=team,
        )

    Activity.objects.create(
        type=Activity.RELEASE,
        project=project,
        ident='4f38b65c62c4565aa94bba391ff8946922a8eed4',
        user=dummy_user,
        data={'version': '4f38b65c62c4565aa94bba391ff8946922a8eed4'},
    )

    create_system_time_series()

    Host.objects.create(host_name='host_demo_' + str(datetime.now()),
                        host_key=generate_host_key(datetime.now()),
                        host_type='demo host',
                        distver='1.0',
                        system='linux',
                        mac_addr='01-aa-32-33-44-fd',
                        user_id=request.user.id,
                        organization_id=org.id)



if __name__ == '__main__':
    settings.CELERY_ALWAYS_EAGER = True

    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option('--events', dest='num_events', default=1, type=int)
    parser.add_option('--username', dest='user_name', type=str)
    parser.add_option('--orgname', dest='org_name', type=str)
    (options, args) = parser.parse_args()

    create_demo_sample(num_events=options.num_events, user_name=options.user_name, org_name=options.org_name)
