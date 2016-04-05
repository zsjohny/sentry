from __future__ import absolute_import, print_function

from django.conf.urls import patterns, url, include
from sentry.api.endpoints.project_issue_tracking import ProjectIssueTrackingEndpoint
from sentry.api.endpoints.upload_token import UploadTokenEndpoint
from .endpoints.auth_index import AuthIndexEndpoint
from .endpoints.broadcast_index import BroadcastIndexEndpoint
from .endpoints.catchall import CatchallEndpoint
from .endpoints.dashboard_details import DashboardDetailsEndpoint
from .endpoints.dashboard_index import DashboardIndexEndpoint
from .endpoints.demo_exception import DemoExceptionEndpoint
from .endpoints.dsym_files import DSymFilesEndpoint, GlobalDSymFilesEndpoint, \
    UnknownDSymFilesEndpoint, UnknownGlobalDSymFilesEndpoint
from .endpoints.event_details import EventDetailsEndpoint
from .endpoints.group_details import GroupDetailsEndpoint
from .endpoints.group_events import GroupEventsEndpoint
from .endpoints.group_events_latest import GroupEventsLatestEndpoint
from .endpoints.group_events_oldest import GroupEventsOldestEndpoint
from .endpoints.group_hashes import GroupHashesEndpoint
from .endpoints.group_notes import GroupNotesEndpoint
from .endpoints.group_notes_details import GroupNotesDetailsEndpoint
from .endpoints.group_stats import GroupStatsEndpoint
from .endpoints.group_tagkey_details import GroupTagKeyDetailsEndpoint
from .endpoints.group_tagkey_values import GroupTagKeyValuesEndpoint
from .endpoints.group_tags import GroupTagsEndpoint
from .endpoints.group_user_reports import GroupUserReportsEndpoint
from .endpoints.host_index import AccessTokenView
from .endpoints.host_index import HelloToken
from .endpoints.host_index import HostIndexEndpoint, LogAgentHostIndexEndpoint
from .endpoints.index import IndexEndpoint
from .endpoints.indexes_details import IndexesDetailsEndpoint
from .endpoints.indexes_fields_index import IndexesFieldsIndexEndpoint
from .endpoints.indexes_index import IndexesIndexEndpoint
from .endpoints.internal_stats import InternalStatsEndpoint
from .endpoints.legacy_project_redirect import LegacyProjectRedirectEndpoint
from .endpoints.logevents import LogEventIndexEndpoint
from .endpoints.logfiles_index import LogfileIndexEndpoint
from .endpoints.organization_access_request_details import OrganizationAccessRequestDetailsEndpoint
from .endpoints.organization_activity import OrganizationActivityEndpoint
from .endpoints.organization_details import OrganizationDetailsEndpoint
from .endpoints.organization_index import OrganizationIndexEndpoint
from .endpoints.organization_issues_new import OrganizationIssuesNewEndpoint
from .endpoints.organization_member_details import OrganizationMemberDetailsEndpoint
from .endpoints.organization_member_index import OrganizationMemberIndexEndpoint
from .endpoints.organization_member_issues_assigned import OrganizationMemberIssuesAssignedEndpoint
from .endpoints.organization_member_issues_bookmarked import OrganizationMemberIssuesBookmarkedEndpoint
from .endpoints.organization_member_issues_viewed import OrganizationMemberIssuesViewedEndpoint
from .endpoints.organization_member_team_details import OrganizationMemberTeamDetailsEndpoint
from .endpoints.organization_onboarding_tasks import OrganizationOnboardingTaskEndpoint
from .endpoints.organization_projects import OrganizationProjectsEndpoint
from .endpoints.organization_shortid import ShortIdLookupEndpoint
from .endpoints.organization_shortids import ShortIdsUpdateEndpoint
from .endpoints.organization_stats import OrganizationStatsEndpoint
from .endpoints.organization_teams import OrganizationTeamsEndpoint
from .endpoints.project_details import ProjectDetailsEndpoint
from .endpoints.project_docs import ProjectDocsEndpoint
from .endpoints.project_docs_platform import ProjectDocsPlatformEndpoint
from .endpoints.project_event_details import ProjectEventDetailsEndpoint
from .endpoints.project_events import ProjectEventsEndpoint
from .endpoints.project_group_index import ProjectGroupIndexEndpoint
from .endpoints.project_group_stats import ProjectGroupStatsEndpoint
from .endpoints.project_key_details import ProjectKeyDetailsEndpoint
from .endpoints.project_keys import ProjectKeysEndpoint
from .endpoints.project_member_index import ProjectMemberIndexEndpoint
from .endpoints.project_plugins import ProjectPluginsEndpoint
from .endpoints.project_quotas import ProjectQuotasEndpoint
from .endpoints.project_releases import ProjectReleasesEndpoint
from .endpoints.project_rule_details import ProjectRuleDetailsEndpoint
from .endpoints.project_rules import ProjectRulesEndpoint
from .endpoints.project_search_details import ProjectSearchDetailsEndpoint
from .endpoints.project_searches import ProjectSearchesEndpoint
from .endpoints.project_settings import ProjectSettingsEndpoint
from .endpoints.project_stats import ProjectStatsEndpoint
from .endpoints.project_tagkey_details import ProjectTagKeyDetailsEndpoint
from .endpoints.project_tagkey_values import ProjectTagKeyValuesEndpoint
from .endpoints.project_tags import ProjectTagsEndpoint
from .endpoints.project_user_reports import ProjectUserReportsEndpoint
from .endpoints.project_users import ProjectUsersEndpoint
from .endpoints.react import ReactEnpoint
from .endpoints.release_details import ReleaseDetailsEndpoint
from .endpoints.release_file_details import ReleaseFileDetailsEndpoint
from .endpoints.release_files import ReleaseFilesEndpoint
from .endpoints.search_details import SearchDetailsEndpoint
from .endpoints.search_index import SearchIndexEndpoint
from .endpoints.search_index import SearchResultEndpoint
from .endpoints.settings_rules import SettingsRulesEndpoint
from .endpoints.shared_group_details import SharedGroupDetailsEndpoint
from .endpoints.stream_index import StreamIndexEndpoint, LogAgentStreamEndpoint
from .endpoints.stream_timeseries_index import StreamTimeSeriesIndexEndpoint
from .endpoints.system_health import SystemHealthEndpoint
from .endpoints.system_options import SystemOptionsEndpoint
from .endpoints.team_details import TeamDetailsEndpoint
from .endpoints.team_groups_new import TeamGroupsNewEndpoint
from .endpoints.team_groups_trending import TeamGroupsTrendingEndpoint
from .endpoints.team_members import TeamMembersEndpoint
from .endpoints.team_project_index import TeamProjectIndexEndpoint
from .endpoints.team_stats import TeamStatsEndpoint
from .endpoints.upload_index import UploadIndexEndpoint
from .endpoints.user_details import UserDetailsEndpoint
from .endpoints.user_index import UserIndexEndpoint
from .endpoints.user_key import UserkeyEndpoint
from .endpoints.user_organizations import UserOrganizationsEndpoint
from .endpoints.visualization_details import VisualizationDetailsEndpoint
from .endpoints.visualization_index import VisualizationIndexEndpoint
from .endpoints.widget_details import WidgetDetailsEndpoint
from .endpoints.widget_index import WidgetIndexEndpoint
from .endpoints.user_info import LogAgentUserInfoEndpoint
from .endpoints.account_appearance import AppearanceSettingsEndpoint
from .endpoints.notification_settings import NotificationSettingsEndpoint
from .endpoints.indexes_fields_index import IndexesFieldsCountIndexEndpoint
from django.conf.urls import url, include
from rest_framework import routers
from sentry.api.endpoints.user_info import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users/$', UserViewSet)
router.register(r'groups/$', GroupViewSet)
# router.register(r'^user_key', UserkeyEndpoint.as_view(), base_name='sentry-api-0-user-key')
# routers.register(r'user_key', Use)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += patterns(
    '',
    #  loginsight
    url(r'^docs/$', include('rest_framework_swagger.urls')),

    url(r'^user_key', UserkeyEndpoint.as_view(), name='sentry-api-0-user-key'),
    url(r'^streams', StreamIndexEndpoint.as_view(), name='sentry-api-0-streams'),
    url(r'^logfiles', LogfileIndexEndpoint.as_view(), name='sentry-api-0-logfiles'),
    url(r'^logevents', LogEventIndexEndpoint.as_view(), name='sentry-api-0-events'),
    url(r'^create_demo', DemoExceptionEndpoint.as_view(), name='sentry-api-0-create-demo'),
    url(r'^hosts', HostIndexEndpoint.as_view(), name='sentry-api-0-hosts'),
    url(r'^stream_timeseries', StreamTimeSeriesIndexEndpoint.as_view(), name='sentry-api-0-stream-timeseries'),
    url(r'^agent/hosts', LogAgentHostIndexEndpoint.as_view(), name='sentry-api-0-agent-hosts'),
    url(r'^agent/streams', LogAgentStreamEndpoint.as_view(), name='sentry-api-0-agent-streams'),
    url(r'^agent/hello', HelloToken.as_view(), name='hello-token'),
    url(r'^accesstoken', AccessTokenView.as_view(), name='access-token'),
    url(r'^dashboard/$', DashboardIndexEndpoint.as_view(), name='sentry-api-0-log-dashboard'),
    url(r'^dashboard/(?P<dashboard_id>[^\/]+)/$', DashboardDetailsEndpoint.as_view(), name='sentry-api-0-log-dashboard-details'),
    url(r'^visualization/$', VisualizationIndexEndpoint.as_view(), name='sentry-log-visualization'),
    url(r'^visualization/(?P<visualization_id>[^\/]+)/$', VisualizationDetailsEndpoint.as_view(), name='sentry-api-0-log-visualization-details'),
    url(r'^widget/$', WidgetIndexEndpoint.as_view(), name='sentry-log-widget'),
    url(r'^widget/(?P<widget_id>[^\/]+)/$', WidgetDetailsEndpoint.as_view(), name='sentry-api-0-log-widget-details'),
    url(r'^search/$', SearchIndexEndpoint.as_view(), name='sentry-log-search'),
    url(r'^search/(?P<search_id>[^\/]+)/$', SearchDetailsEndpoint.as_view(), name='sentry-api-0-log-search-details'),
    url(r'^query/(?P<index_name>[^\/]+)/$', SearchResultEndpoint.as_view(), name='sentry-api-0-log-search-result'),
    url(r'^indexes/$', IndexesIndexEndpoint.as_view(), name='sentry-log-indexes'),
    url(r'^indexes/(?P<index_name>[^\/]+)/$', IndexesDetailsEndpoint.as_view(), name='sentry-api-0-log-index-details'),
    url(r'^indexes/(?P<index_name>[^\/]+)/fields/$', IndexesFieldsIndexEndpoint.as_view(), name='sentry-api-0-log-index-fields'),
    url(r'^indexes/(?P<index_name>[^\/]+)/fields/count/$', IndexesFieldsCountIndexEndpoint.as_view(), name='sentry-api-0-log-index-fields-count'),
    url(r'^upload/$', UploadIndexEndpoint.as_view(), name='sentry-api-0-log-index-fields'),
    url(r'^react/$', ReactEnpoint.as_view(), name='sentry-api-0-react'),
    url(r'^userinfo/$',LogAgentUserInfoEndpoint.as_view(),name='sentry-api-0-agent-configuration'),
    url(r'^upload_token/$',UploadTokenEndpoint.as_view(),name='sentry-api-0-upload-token'),



    url(r'^account/settings/appearance/$', AppearanceSettingsEndpoint.as_view(),
        name='sentry-api-0-account-settings-appearance'),

    url(r'^account/settings/notifications/$', NotificationSettingsEndpoint.as_view(),
        name='sentry-api-0-account-settings-notifications'),

    # settings
    url(r'^(?P<organization_slug>[\w_-]+)/(?P<project_slug>[\w_-]+)/settings/$',
        ProjectSettingsEndpoint.as_view(),
        name='sentry-manage-project'),
    url(r'^(?P<organization_slug>[\w_-]+)/(?P<project_slug>[\w_-]+)/settings/quotas/$',
        ProjectQuotasEndpoint.as_view(),
        name='sentry-api-0-manage-project-quotas'),

    url(r'^(?P<organization_slug>[\w_-]+)/(?P<project_slug>[\w_-]+)/settings/issue-tracking/$',
        ProjectIssueTrackingEndpoint.as_view(),
        name='sentry-api-0-project-issue-tracking'),
    # Auth
    url(r'^auth/$',
        AuthIndexEndpoint.as_view(),
        name='sentry-api-0-auth'),

    url(r'^(?P<organization_slug>[\w_-]+)/(?P<project_slug>[\w_-]+)/settings/rules/$',
        SettingsRulesEndpoint.as_view(),
        name='sentry-api-0-project-rules'),

    # url(r'^(?P<organization_slug>[\w_-]+)/(?P<project_slug>[\w_-]+)/settings/notifications/$',
    #     ProjectNotificationsEndpoint.as_view(),
    #     name='sentry-api-0-project-notifications'),

    url(r'^(?P<organization_slug>[\w_-]+)/(?P<project_slug>[\w_-]+)/settings/plugins/$',
        ProjectPluginsEndpoint.as_view(),
        name='sentry-api-0-manage-project-plugins'),

    # Broadcasts
    url(r'^broadcasts/$',
        BroadcastIndexEndpoint.as_view(),
        name='sentry-api-0-broadcast-index'),

    # Users
    url(r'^users/$',
        UserIndexEndpoint.as_view(),
        name='sentry-api-0-user-index'),
    url(r'^users/(?P<user_id>[^\/]+)/$',
        UserDetailsEndpoint.as_view(),
        name='sentry-api-0-user-details'),
    url(r'^users/(?P<user_id>[^\/]+)/organizations/$',
        UserOrganizationsEndpoint.as_view(),
        name='sentry-api-0-user-organizations'),

    # Organizations
    url(r'^organizations/$',
        OrganizationIndexEndpoint.as_view(),
        name='sentry-api-0-organizations'),
    url(r'^organizations/(?P<organization_slug>[^\/]+)/$',
        OrganizationDetailsEndpoint.as_view(),
        name='sentry-api-0-organization-details'),
    url(r'^organizations/(?P<organization_slug>[^\/]+)/shortids/(?P<short_id>[^\/]+)/$',
        ShortIdLookupEndpoint.as_view(),
        name='sentry-api-0-short-id-lookup'),
    url(r'^organizations/(?P<organization_slug>[^\/]+)/shortids/$',
        ShortIdsUpdateEndpoint.as_view(),
        name='sentry-api-0-short-ids-update'),
    url(r'^organizations/(?P<organization_slug>[^\/]+)/access-requests/(?P<request_id>\d+)/$',
        OrganizationAccessRequestDetailsEndpoint.as_view(),
        name='sentry-api-0-organization-access-request-details'),
    url(r'^organizations/(?P<organization_slug>[^\/]+)/activity/$',
        OrganizationActivityEndpoint.as_view(),
        name='sentry-api-0-organization-activity'),
    url(r'^organizations/(?P<organization_slug>[^\/]+)/issues/new/$',
        OrganizationIssuesNewEndpoint.as_view(),
        name='sentry-api-0-organization-issues-new'),
    url(r'^organizations/(?P<organization_slug>[^\/]+)/members/$',
        OrganizationMemberIndexEndpoint.as_view(),
        name='sentry-api-0-organization-member-index'),
    url(r'^organizations/(?P<organization_slug>[^\/]+)/members/(?P<member_id>[^\/]+)/$',
        OrganizationMemberDetailsEndpoint.as_view(),
        name='sentry-api-0-organization-member-details'),
    url(r'^organizations/(?P<organization_slug>[^\/]+)/members/(?P<member_id>[^\/]+)/issues/assigned/$',
        OrganizationMemberIssuesAssignedEndpoint.as_view(),
        name='sentry-api-0-organization-member-issues-assigned'),
    url(r'^organizations/(?P<organization_slug>[^\/]+)/members/(?P<member_id>[^\/]+)/issues/bookmarked/$',
        OrganizationMemberIssuesBookmarkedEndpoint.as_view(),
        name='sentry-api-0-organization-member-issues-bookmarked'),
    url(r'^organizations/(?P<organization_slug>[^\/]+)/members/(?P<member_id>[^\/]+)/issues/viewed/$',
        OrganizationMemberIssuesViewedEndpoint.as_view(),
        name='sentry-api-0-organization-member-issues-viewed'),
    url(r'^organizations/(?P<organization_slug>[^\/]+)/members/(?P<member_id>[^\/]+)/teams/(?P<team_slug>[^\/]+)/$',
        OrganizationMemberTeamDetailsEndpoint.as_view(),
        name='sentry-api-0-organization-member-team-details'),
    url(r'^organizations/(?P<organization_slug>[^\/]+)/projects/$',
        OrganizationProjectsEndpoint.as_view(),
        name='sentry-api-0-organization-projects'),
    url(r'^organizations/(?P<organization_slug>[^\/]+)/stats/$',
        OrganizationStatsEndpoint.as_view(),
        name='sentry-api-0-organization-stats'),
    url(r'^organizations/(?P<organization_slug>[^\/]+)/teams/$',
        OrganizationTeamsEndpoint.as_view(),
        name='sentry-api-0-organization-teams'),
    url(r'^organizations/(?P<organization_slug>[^\/]+)/onboarding-tasks/$',
        OrganizationOnboardingTaskEndpoint.as_view(),
        name='sentry-api-0-organization-onboardingtasks'),

    # Teams
    url(r'^teams/(?P<organization_slug>[^\/]+)/(?P<team_slug>[^\/]+)/$',
        TeamDetailsEndpoint.as_view(),
        name='sentry-api-0-team-details'),
    url(r'^teams/(?P<organization_slug>[^\/]+)/(?P<team_slug>[^\/]+)/(?:groups|issues)/new/$',
        TeamGroupsNewEndpoint.as_view(),
        name='sentry-api-0-team-groups-new'),
    url(r'^teams/(?P<organization_slug>[^\/]+)/(?P<team_slug>[^\/]+)/(?:groups|issues)/trending/$',
        TeamGroupsTrendingEndpoint.as_view(),
        name='sentry-api-0-team-groups-trending'),
    url(r'^teams/(?P<organization_slug>[^\/]+)/(?P<team_slug>[^\/]+)/members/$',
        TeamMembersEndpoint.as_view(),
        name='sentry-api-0-team-members'),
    url(r'^teams/(?P<organization_slug>[^\/]+)/(?P<team_slug>[^\/]+)/projects/$',
        TeamProjectIndexEndpoint.as_view(),
        name='sentry-api-0-team-project-index'),
    url(r'^teams/(?P<organization_slug>[^\/]+)/(?P<team_slug>[^\/]+)/stats/$',
        TeamStatsEndpoint.as_view(),
        name='sentry-api-0-team-stats'),

    # Handles redirecting project_id => org_slug/project_slug
    # TODO(dcramer): remove this after a reasonable period of time
    url(r'^projects/(?P<project_id>\d+)/(?P<path>(?:groups|releases|stats|tags)/.*)$',
        LegacyProjectRedirectEndpoint.as_view()),

    # Projects
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/$',
        ProjectDetailsEndpoint.as_view(),
        name='sentry-api-0-project-details'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/docs/$',
        ProjectDocsEndpoint.as_view(),
        name='sentry-api-0-project-docs'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/docs/(?P<platform>[\w-]+)/$',
        ProjectDocsPlatformEndpoint.as_view(),
        name='sentry-api-0-project-docs-platform'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/events/$',
        ProjectEventsEndpoint.as_view(),
        name='sentry-api-0-project-events'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/events/(?P<event_id>[\w-]+)/$',
        ProjectEventDetailsEndpoint.as_view(),
        name='sentry-api-0-project-event-details'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/(?:groups|issues)/$',
        ProjectGroupIndexEndpoint.as_view(),
        name='sentry-api-0-project-group-index'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/(?:groups|issues)/stats/$',
        ProjectGroupStatsEndpoint.as_view(),
        name='sentry-api-0-project-group-stats'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/keys/$',
        ProjectKeysEndpoint.as_view(),
        name='sentry-api-0-project-keys'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/keys/(?P<key_id>[^\/]+)/$',
        ProjectKeyDetailsEndpoint.as_view(),
        name='sentry-api-0-project-key-details'),
    url(r'^projects/(?P<organization_slug>[^/]+)/(?P<project_slug>[^/]+)/members/$',
        ProjectMemberIndexEndpoint.as_view(),
        name='sentry-api-0-project-member-index'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/releases/$',
        ProjectReleasesEndpoint.as_view(),
        name='sentry-api-0-project-releases'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/releases/(?P<version>[^/]+)/$',
        ReleaseDetailsEndpoint.as_view(),
        name='sentry-api-0-release-details'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/releases/(?P<version>[^/]+)/files/$',
        ReleaseFilesEndpoint.as_view(),
        name='sentry-api-0-release-files'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/releases/(?P<version>[^/]+)/files/(?P<file_id>\d+)/$',
        ReleaseFileDetailsEndpoint.as_view(),
        name='sentry-api-0-release-file-details'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/files/dsyms/$',
        DSymFilesEndpoint.as_view(),
        name='sentry-api-0-dsym-files'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/files/dsyms/unknown/$',
        UnknownDSymFilesEndpoint.as_view(),
        name='sentry-api-0-unknown-dsym-files'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/rules/$',
        ProjectRulesEndpoint.as_view(),
        name='sentry-api-0-project-rules'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/rules/(?P<rule_id>[^\/]+)/$',
        ProjectRuleDetailsEndpoint.as_view(),
        name='sentry-api-0-project-rule-details'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/searches/$',
        ProjectSearchesEndpoint.as_view(),
        name='sentry-api-0-project-searches'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/searches/(?P<search_id>[^\/]+)/$',
        ProjectSearchDetailsEndpoint.as_view(),
        name='sentry-api-0-project-search-details'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/stats/$',
        ProjectStatsEndpoint.as_view(),
        name='sentry-api-0-project-stats'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/tags/$',
        ProjectTagsEndpoint.as_view(),
        name='sentry-api-0-project-tags'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/tags/(?P<key>[^/]+)/$',
        ProjectTagKeyDetailsEndpoint.as_view(),
        name='sentry-api-0-project-tagkey-details'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/tags/(?P<key>[^/]+)/values/$',
        ProjectTagKeyValuesEndpoint.as_view(),
        name='sentry-api-0-project-tagkey-values'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/users/$',
        ProjectUsersEndpoint.as_view(),
        name='sentry-api-0-project-users'),
    url(r'^projects/(?P<organization_slug>[^\/]+)/(?P<project_slug>[^\/]+)/user-reports/$',
        ProjectUserReportsEndpoint.as_view(),
        name='sentry-api-0-project-user-reports'),

    # Groups
    url(r'^(?:groups|issues)/(?P<issue_id>\d+)/$',
        GroupDetailsEndpoint.as_view(),
        name='sentry-api-0-group-details'),
    url(r'^(?:groups|issues)/(?P<issue_id>\d+)/events/$',
        GroupEventsEndpoint.as_view(),
        name='sentry-api-0-group-events'),
    url(r'^(?:groups|issues)/(?P<issue_id>\d+)/events/latest/$',
        GroupEventsLatestEndpoint.as_view(),
        name='sentry-api-0-group-events-latest'),
    url(r'^(?:groups|issues)/(?P<issue_id>\d+)/events/oldest/$',
        GroupEventsOldestEndpoint.as_view(),
        name='sentry-api-0-group-events-oldest'),
    url(r'^(?:groups|issues)/(?P<issue_id>\d+)/(?:notes|comments)/$',
        GroupNotesEndpoint.as_view(),
        name='sentry-api-0-group-notes'),
    url(r'^(?:groups|issues)/(?P<issue_id>\d+)/(?:notes|comments)/(?P<note_id>[^\/]+)/$',
        GroupNotesDetailsEndpoint.as_view(),
        name='sentry-api-0-group-notes-details'),
    url(r'^(?:groups|issues)/(?P<issue_id>\d+)/hashes/$',
        GroupHashesEndpoint.as_view(),
        name='sentry-api-0-group-events'),
    url(r'^(?:groups|issues)/(?P<issue_id>\d+)/stats/$',
        GroupStatsEndpoint.as_view(),
        name='sentry-api-0-group-stats'),
    url(r'^(?:groups|issues)/(?P<issue_id>\d+)/tags/$',
        GroupTagsEndpoint.as_view(),
        name='sentry-api-0-group-tags'),
    url(r'^(?:groups|issues)/(?P<issue_id>\d+)/tags/(?P<key>[^/]+)/$',
        GroupTagKeyDetailsEndpoint.as_view(),
        name='sentry-api-0-group-tagkey-details'),
    url(r'^(?:groups|issues)/(?P<issue_id>\d+)/tags/(?P<key>[^/]+)/values/$',
        GroupTagKeyValuesEndpoint.as_view(),
        name='sentry-api-0-group-tagkey-values'),
    url(r'^(?:groups|issues)/(?P<issue_id>\d+)/user-reports/$',
        GroupUserReportsEndpoint.as_view(),
        name='sentry-api-0-group-user-reports'),

    url(r'^shared/(?:groups|issues)/(?P<share_id>[^\/]+)/$',
        SharedGroupDetailsEndpoint.as_view(),
        name='sentry-api-0-shared-group-details'),

    # Events
    url(r'^events/(?P<event_id>\d+)/$',
        EventDetailsEndpoint.as_view(),
            name='sentry-api-0-event-details'),

    # Installation Global Endpoints
    url(r'^system/global-dsyms/$',
        GlobalDSymFilesEndpoint.as_view(),
        name='sentry-api-0-global-dsym-files'),
    url(r'^system/global-dsyms/unknown/$',
        UnknownGlobalDSymFilesEndpoint.as_view(),
        name='sentry-api-0-unknown-global-dsym-files'),

    # Internal
    url(r'^internal/health/$',
        SystemHealthEndpoint.as_view(),
        name='sentry-api-0-system-health'),
    url(r'^internal/options/$',
        SystemOptionsEndpoint.as_view(),
        name='sentry-api-0-system-options'),
    url(r'^internal/stats/$',
        InternalStatsEndpoint.as_view(),
        name='sentry-api-0-internal-stats'),

    url(r'^$',
        IndexEndpoint.as_view(),
        name='sentry-api-index'),


    url(r'^',
        CatchallEndpoint.as_view(),
        name='sentry-api-catchall'),

    url(r'^(?P<organization_slug>[\w_-]+)/(?P<project_slug>[\w_-]+)/settings/plugins/$',
        ProjectPluginsEndpoint.as_view(),
        name='sentry-api-0-manage-project-plugins'),

    #settings/rules

    # url(r'^(?P<organization_slug>[\w_-]+)/(?P<project_slug>[\w_-]+)/settings/rules/$',
    #     SettingsRulesEndpoint.as_view(),
    #     name='sentry-api-0-project-rules'),
#
    # url(r'^(?P<organization_slug>[\w_-]+)/(?P<project_slug>[\w_-]+)/settings/notifications/$',
    #     ProjectNotificationsEndpoint.as_view(),
    #     name='sentry-api-0-project-notifications'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
