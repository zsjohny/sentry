Creating test database for alias 'default'...
Saved 0.00GB (on 0.00GB) with removal of 0 duplicate files
............................................................E.E............................FF...FFF.......1457964836000:0:0
.............................................................................E.............................F.F.......F.F...............................................................FFFFF.F..........................ValueError: hello world
  File "foo/baz.py", line 1

ValueError: hello world
  File "foo/baz.py", line 1
..........exc 0 frame 0
exc 0 frame 1
exc 0 frame 2
exc 0 frame 3
exc 0 frame 4
exc 1 frame 0
exc 1 frame 1
exc 1 frame 2
exc 1 frame 3
exc 1 frame 4
exc 2 frame 0
exc 2 frame 1
exc 2 frame 2
exc 2 frame 3
exc 2 frame 4
exc 3 frame 0
exc 3 frame 1
exc 3 frame 2
exc 3 frame 3
exc 3 frame 4
exc 4 frame 0
exc 4 frame 1
exc 4 frame 2
exc 4 frame 3
exc 4 frame 4
...........................................................................F.......................................................................[WARNING] Retrying (Retry(total=1, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<urllib3.connection.HTTPConnection object at 0x119bd6510>: Failed to establish a new connection: [Errno 61] Connection refused',)': /buckets/nodes/keys/sY2y2evvS3SRKShDL%2B1D8w%3D%3D?returnbody=false
[WARNING] Retrying (Retry(total=0, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<urllib3.connection.HTTPConnection object at 0x119bd6410>: Failed to establish a new connection: [Errno 61] Connection refused',)': /buckets/nodes/keys/sY2y2evvS3SRKShDL%2B1D8w%3D%3D?returnbody=false
[WARNING] Retrying (Retry(total=1, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<urllib3.connection.HTTPConnection object at 0x119bd6790>: Failed to establish a new connection: [Errno 61] Connection refused',)': /buckets/nodes/keys/sY2y2evvS3SRKShDL%2B1D8w%3D%3D?returnbody=false
[WARNING] Retrying (Retry(total=0, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<urllib3.connection.HTTPConnection object at 0x119bd6450>: Failed to establish a new connection: [Errno 61] Connection refused',)': /buckets/nodes/keys/sY2y2evvS3SRKShDL%2B1D8w%3D%3D?returnbody=false
[WARNING] Retrying (Retry(total=1, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<urllib3.connection.HTTPConnection object at 0x119bd6550>: Failed to establish a new connection: [Errno 61] Connection refused',)': /buckets/nodes/keys/sY2y2evvS3SRKShDL%2B1D8w%3D%3D?returnbody=false
[WARNING] Retrying (Retry(total=0, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<urllib3.connection.HTTPConnection object at 0x119bd6390>: Failed to establish a new connection: [Errno 61] Connection refused',)': /buckets/nodes/keys/sY2y2evvS3SRKShDL%2B1D8w%3D%3D?returnbody=false
[WARNING] Retrying (Retry(total=1, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<urllib3.connection.HTTPConnection object at 0x119bd63d0>: Failed to establish a new connection: [Errno 61] Connection refused',)': /buckets/nodes/keys/sY2y2evvS3SRKShDL%2B1D8w%3D%3D?returnbody=false
[WARNING] Retrying (Retry(total=0, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<urllib3.connection.HTTPConnection object at 0x119bd6310>: Failed to establish a new connection: [Errno 61] Connection refused',)': /buckets/nodes/keys/sY2y2evvS3SRKShDL%2B1D8w%3D%3D?returnbody=false
E.....................['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', '__str__', '__subclasshook__', '__weakref__', '_create_alternatives', '_create_attachment', '_create_attachments', '_create_message', '_create_mime_attachment', 'alternative_subtype', 'alternatives', 'attach', 'attach_alternative', 'attach_file', 'attachments', 'bcc', 'body', 'cc', 'connection', 'content_subtype', 'encoding', 'extra_headers', 'from_email', 'get_connection', 'message', 'mixed_subtype', 'recipients', 'send', 'subject', 'to']
........Created internal Sentry project (slug=internal, id=1)
.Created internal Sentry project (slug=internal, id=1)
.........................................................................................................................<MagicMock name='send_activity_notifications' id='4792327952'>
..F.[WARNING] AuthIdentity(id=1) notified as not valid:
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/src/sentry/tasks/check_auth.py", line 78, in check_auth_identity
    provider.refresh_identity(auth_identity)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/mock-1.0.1-py2.7.egg/mock.py", line 955, in __call__
    return _mock_self._mock_call(*args, **kwargs)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/mock-1.0.1-py2.7.egg/mock.py", line 1010, in _mock_call
    raise effect
IdentityNotValid
.................................F...F..........E.......................................................F...................[ERROR] Error processing 'simple' on 'Foo':
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/src/sentry/utils/safe.py", line 26, in safe_execute
    result = func(*args, **kwargs)
  File "/Users/wanghe/work/dev/sentry/tests/sentry/utils/test_safe.py", line 51, in simple
    raise Exception()
Exception
.[ERROR] Error processing '<lambda>' on 'function': global name 'a' is not defined
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/src/sentry/utils/safe.py", line 26, in safe_execute
    result = func(*args, **kwargs)
  File "/Users/wanghe/work/dev/sentry/tests/sentry/utils/test_safe.py", line 29, in <lambda>
    assert safe_execute(lambda: a) is None  # NOQA
NameError: global name 'a' is not defined
.[ERROR] Error processing 'simple' on 'function':
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/src/sentry/utils/safe.py", line 26, in safe_execute
    result = func(*args, **kwargs)
  File "/Users/wanghe/work/dev/sentry/tests/sentry/utils/test_safe.py", line 38, in simple
    raise Exception()
Exception
..........................................FF...F.F......FFF.FF..................F.FEEF.........FE.................................FF......[ERROR] MAILGUN_API_KEY is not set
..............................................{u'mail:enabled': False, u'auto_tag:_urls:enabled': True, u'auto_tag:_operating_systems:enabled': True}
.....................[WARNING] Disabled release hook received for project_id=495, plugin_id=dummy
.[WARNING] Unable to verify signature for release hook
..FFFF...FFFF.FF...FF.FF....EEEE...............F........[ERROR] long() argument must be a string or a number, not 'Project'
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/src/sentry/utils/logging.py", line 23, in wrapped
    return func(*args, **kwargs)
  File "/Users/wanghe/work/dev/sentry/src/sentry/event_manager.py", line 370, in save
    project = Project.objects.get_from_cache(id=project)
  File "/Users/wanghe/work/dev/sentry/src/sentry/db/models/manager.py", line 259, in get_from_cache
    result = self.get(**kwargs)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/Django-1.6.11-py2.7.egg/django/db/models/manager.py", line 151, in get
    return self.get_queryset().get(*args, **kwargs)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/Django-1.6.11-py2.7.egg/django/db/models/query.py", line 301, in get
    clone = self.filter(*args, **kwargs)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/Django-1.6.11-py2.7.egg/django/db/models/query.py", line 593, in filter
    return self._filter_or_exclude(False, *args, **kwargs)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/Django-1.6.11-py2.7.egg/django/db/models/query.py", line 611, in _filter_or_exclude
    clone.query.add_q(Q(*args, **kwargs))
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/Django-1.6.11-py2.7.egg/django/db/models/sql/query.py", line 1204, in add_q
    clause = self._add_q(where_part, used_aliases)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/Django-1.6.11-py2.7.egg/django/db/models/sql/query.py", line 1240, in _add_q
    current_negated=current_negated)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/Django-1.6.11-py2.7.egg/django/db/models/sql/query.py", line 1131, in build_filter
    clause.add(constraint, AND)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/Django-1.6.11-py2.7.egg/django/utils/tree.py", line 104, in add
    data = self._prepare_data(data)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/Django-1.6.11-py2.7.egg/django/db/models/sql/where.py", line 79, in _prepare_data
    value = obj.prepare(lookup_type, value)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/Django-1.6.11-py2.7.egg/django/db/models/sql/where.py", line 352, in prepare
    return self.field.get_prep_lookup(lookup_type, value)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/Django-1.6.11-py2.7.egg/django/db/models/fields/__init__.py", line 369, in get_prep_lookup
    return self.get_prep_value(value)
  File "/Users/wanghe/work/dev/sentry/src/sentry/db/models/fields/bounded.py", line 94, in get_prep_value
    value = long(value)
TypeError: long() argument must be a string or a number, not 'Project'
E......FFE
======================================================================
ERROR: test_can_remove_as_owner (tests.sentry.api.endpoints.test_organization_details.OrganizationDeleteTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/mock-1.0.1-py2.7.egg/mock.py", line 1201, in patched
    return func(*args, **keywargs)
  File "/Users/wanghe/work/dev/sentry/tests/sentry/api/endpoints/test_organization_details.py", line 88, in test_can_remove_as_owner
    assert response.status_code == 204, response.data
AttributeError: 'HttpResponse' object has no attribute 'data'

======================================================================
ERROR: test_cannot_remove_default (tests.sentry.api.endpoints.test_organization_details.OrganizationDeleteTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/api/endpoints/test_organization_details.py", line 131, in test_cannot_remove_default
    assert response.status_code == 400, response.data
AttributeError: 'HttpResponse' object has no attribute 'data'

======================================================================
ERROR: test_can_remove_as_team_admin (tests.sentry.api.endpoints.test_team_details.TeamDeleteTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/mock-1.0.1-py2.7.egg/mock.py", line 1201, in patched
    return func(*args, **keywargs)
  File "/Users/wanghe/work/dev/sentry/tests/sentry/api/endpoints/test_team_details.py", line 69, in test_can_remove_as_team_admin
    assert response.status_code == 204, response.data
AttributeError: 'HttpResponse' object has no attribute 'data'

======================================================================
ERROR: test_integration (tests.sentry.nodestore.riak.backend.tests.RiakNodeStorageTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/nodestore/riak/backend/tests.py", line 19, in test_integration
    'foo': 'bar',
  File "/Users/wanghe/work/dev/sentry/src/sentry/nodestore/base.py", line 30, in create
    self.set(node_id, data)
  File "/Users/wanghe/work/dev/sentry/src/sentry/nodestore/riak/backend.py", line 46, in set
    self.conn.put(self.bucket, id, data, returnbody='false')
  File "/Users/wanghe/work/dev/sentry/src/sentry/nodestore/riak/client.py", line 79, in put
    body=data,
  File "/Users/wanghe/work/dev/sentry/src/sentry/nodestore/riak/client.py", line 242, in urlopen
    six.reraise(*last_error)
  File "/Users/wanghe/work/dev/sentry/src/sentry/nodestore/riak/client.py", line 234, in urlopen
    return conn.urlopen(method, path, **kwargs)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/urllib3-1.14-py2.7.egg/urllib3/connectionpool.py", line 628, in urlopen
    release_conn=release_conn, **response_kw)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/urllib3-1.14-py2.7.egg/urllib3/connectionpool.py", line 628, in urlopen
    release_conn=release_conn, **response_kw)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/urllib3-1.14-py2.7.egg/urllib3/connectionpool.py", line 608, in urlopen
    _stacktrace=sys.exc_info()[2])
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/urllib3-1.14-py2.7.egg/urllib3/util/retry.py", line 273, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
MaxRetryError: HTTPConnectionPool(host='127.0.0.1', port=8098): Max retries exceeded with url: /buckets/nodes/keys/sY2y2evvS3SRKShDL%2B1D8w%3D%3D?returnbody=false (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x119bd6810>: Failed to establish a new connection: [Errno 61] Connection refused',))

======================================================================
ERROR: test_explicit_reply_to (tests.sentry.utils.email.tests.MessageBuilderTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/utils/email/tests.py", line 49, in test_explicit_reply_to
    assert out.extra_headers['Reply-To'] == 'bar@example.com'
KeyError: 'Reply-To'

======================================================================
ERROR: test_registration_disabled (tests.sentry.web.frontend.test_auth_login.AuthLoginTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_auth_login.py", line 50, in test_registration_disabled
    assert resp.context['register_form'] is None
TypeError: 'NoneType' object has no attribute '__getitem__'

======================================================================
ERROR: test_registration_valid (tests.sentry.web.frontend.test_auth_login.AuthLoginTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_auth_login.py", line 60, in test_registration_valid
    user = User.objects.get(username='test-a-really-long-email-address@example.com')
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/Django-1.6.11-py2.7.egg/django/db/models/manager.py", line 151, in get
    return self.get_queryset().get(*args, **kwargs)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/Django-1.6.11-py2.7.egg/django/db/models/query.py", line 310, in get
    self.model._meta.object_name)
DoesNotExist: User matching query does not exist.

======================================================================
ERROR: test_valid_params (tests.sentry.web.frontend.test_create_organization.CreateOrganizationTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_create_organization.py", line 29, in test_valid_params
    org = Organization.objects.get(name='bar')
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/Django-1.6.11-py2.7.egg/django/db/models/manager.py", line 151, in get
    return self.get_queryset().get(*args, **kwargs)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/Django-1.6.11-py2.7.egg/django/db/models/query.py", line 310, in get
    self.model._meta.object_name)
DoesNotExist: Organization matching query does not exist.

======================================================================
ERROR: tests.sentry.lang.javascript.test_plugin (unittest.loader.ModuleImportFailure)
----------------------------------------------------------------------
ImportError: Failed to import test module: tests.sentry.lang.javascript.test_plugin
Traceback (most recent call last):
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/unittest/loader.py", line 254, in _find_tests
    module = self._get_module_from_name(name)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/unittest/loader.py", line 232, in _get_module_from_name
    __import__(name)
  File "/Users/wanghe/work/dev/sentry/tests/sentry/lang/javascript/test_plugin.py", line 3, in <module>
    import responses
ImportError: No module named responses


======================================================================
ERROR: tests.sentry.lang.javascript.test_processor (unittest.loader.ModuleImportFailure)
----------------------------------------------------------------------
ImportError: Failed to import test module: tests.sentry.lang.javascript.test_processor
Traceback (most recent call last):
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/unittest/loader.py", line 254, in _find_tests
    module = self._get_module_from_name(name)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/unittest/loader.py", line 232, in _get_module_from_name
    __import__(name)
  File "/Users/wanghe/work/dev/sentry/tests/sentry/lang/javascript/test_processor.py", line 6, in <module>
    import responses
ImportError: No module named responses


======================================================================
ERROR: tests.sentry.metrics.test_datadog (unittest.loader.ModuleImportFailure)
----------------------------------------------------------------------
ImportError: Failed to import test module: tests.sentry.metrics.test_datadog
Traceback (most recent call last):
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/unittest/loader.py", line 254, in _find_tests
    module = self._get_module_from_name(name)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/unittest/loader.py", line 232, in _get_module_from_name
    __import__(name)
  File "/Users/wanghe/work/dev/sentry/tests/sentry/metrics/test_datadog.py", line 5, in <module>
    from datadog.util.hostname import get_hostname
ImportError: No module named datadog.util.hostname


======================================================================
ERROR: tests.sentry.nodestore.cassandra.backend.tests (unittest.loader.ModuleImportFailure)
----------------------------------------------------------------------
ImportError: Failed to import test module: tests.sentry.nodestore.cassandra.backend.tests
Traceback (most recent call last):
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/unittest/loader.py", line 254, in _find_tests
    module = self._get_module_from_name(name)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/unittest/loader.py", line 232, in _get_module_from_name
    __import__(name)
  File "/Users/wanghe/work/dev/sentry/tests/sentry/nodestore/cassandra/backend/tests.py", line 5, in <module>
    from sentry.nodestore.cassandra.backend import CassandraNodeStorage
  File "/Users/wanghe/work/dev/sentry/src/sentry/nodestore/cassandra/__init__.py", line 10, in <module>
    from .backend import *  # NOQA
  File "/Users/wanghe/work/dev/sentry/src/sentry/nodestore/cassandra/backend.py", line 11, in <module>
    import casscache
ImportError: No module named casscache


======================================================================
ERROR: test_record_frequencies (tests.sentry.test_event_manager.EventManagerTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/test_event_manager.py", line 420, in test_record_frequencies
    (event.project.id,),
AttributeError: 'NoneType' object has no attribute 'project'

======================================================================
ERROR: tests.sentry.test_http (unittest.loader.ModuleImportFailure)
----------------------------------------------------------------------
ImportError: Failed to import test module: tests.sentry.test_http
Traceback (most recent call last):
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/unittest/loader.py", line 254, in _find_tests
    module = self._get_module_from_name(name)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/unittest/loader.py", line 232, in _get_module_from_name
    __import__(name)
  File "/Users/wanghe/work/dev/sentry/tests/sentry/test_http.py", line 3, in <module>
    import responses
ImportError: No module named responses


======================================================================
FAIL: test_internal_project (tests.sentry.api.endpoints.test_project_details.ProjectDeleteTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/mock-1.0.1-py2.7.egg/mock.py", line 1201, in patched
    return func(*args, **keywargs)
  File "/Users/wanghe/work/dev/sentry/tests/sentry/api/endpoints/test_project_details.py", line 168, in test_internal_project
    assert response.status_code == 403
AssertionError

======================================================================
FAIL: test_simple (tests.sentry.api.endpoints.test_project_details.ProjectDeleteTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/mock-1.0.1-py2.7.egg/mock.py", line 1201, in patched
    return func(*args, **keywargs)
  File "/Users/wanghe/work/dev/sentry/tests/sentry/api/endpoints/test_project_details.py", line 143, in test_simple
    assert response.status_code == 204
AssertionError

======================================================================
FAIL: test_bookmarks (tests.sentry.api.endpoints.test_project_details.ProjectUpdateTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/api/endpoints/test_project_details.py", line 112, in test_bookmarks
    assert resp.status_code == 200, resp.content
AssertionError: {"username": "admin@localhost", "sudoRequired": true, "error": "Account verification required."}

======================================================================
FAIL: test_options (tests.sentry.api.endpoints.test_project_details.ProjectUpdateTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/api/endpoints/test_project_details.py", line 94, in test_options
    assert resp.status_code == 200, resp.content
AssertionError: {"username": "admin@localhost", "sudoRequired": true, "error": "Account verification required."}

======================================================================
FAIL: test_simple (tests.sentry.api.endpoints.test_project_details.ProjectUpdateTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/api/endpoints/test_project_details.py", line 72, in test_simple
    assert resp.status_code == 200, resp.content
AssertionError: {"username": "admin@localhost", "sudoRequired": true, "error": "Account verification required."}

======================================================================
FAIL: test_simple (tests.sentry.api.test_paginator.DateTimePaginatorTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/api/test_paginator.py", line 77, in test_simple
    assert len(result3) == 1, list(result3)
AssertionError: []

======================================================================
FAIL: test_buffer_is_a_buffer (tests.sentry.app.tests.AppTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/app/tests.py", line 14, in test_buffer_is_a_buffer
    self.assertEquals(type(app.buffer), Buffer)
AssertionError: <class 'sentry.buffer.redis.RedisBuffer'> != <class 'sentry.buffer.base.Buffer'>

======================================================================
FAIL: test_incr_saves_to_redis (tests.sentry.buffer.redis.tests.RedisBufferTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/mock-1.0.1-py2.7.egg/mock.py", line 1201, in patched
    return func(*args, **keywargs)
  File "/Users/wanghe/work/dev/sentry/tests/sentry/buffer/redis/tests.py", line 68, in test_incr_saves_to_redis
    assert pending == ['foo']
AssertionError

======================================================================
FAIL: test_process_pending (tests.sentry.buffer.redis.tests.RedisBufferTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/mock-1.0.1-py2.7.egg/mock.py", line 1201, in patched
    return func(*args, **keywargs)
  File "/Users/wanghe/work/dev/sentry/tests/sentry/buffer/redis/tests.py", line 29, in test_process_pending
    assert len(process_incr.apply_async.mock_calls) == 2
AssertionError

======================================================================
FAIL: test_digesting (tests.sentry.digests.backends.test_redis.DigestTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/digests/backends/test_redis.py", line 261, in test_digesting
    self.assertChanges(get_waiting_set_size, before=0, after=1), \
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/exam-0.10.5-py2.7.egg/exam/asserts.py", line 33, in __enter__
    assert not check, message.format(**vars(self))
AssertionError: Value before is 16, not 0

======================================================================
FAIL: test_digesting_failure_recovery (tests.sentry.digests.backends.test_redis.DigestTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/digests/backends/test_redis.py", line 329, in test_digesting_failure_recovery
    self.assertChanges(get_waiting_set_size, before=0, after=1), \
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/exam-0.10.5-py2.7.egg/exam/asserts.py", line 33, in __enter__
    assert not check, message.format(**vars(self))
AssertionError: Value before is 16, not 0

======================================================================
FAIL: test_add_record (tests.sentry.digests.backends.test_redis.RedisBackendTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/digests/backends/test_redis.py", line 142, in test_add_record
    with self.assertChanges(get_timeline_score_in_ready_set, before=None, after=record.timestamp), \
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/exam-0.10.5-py2.7.egg/exam/asserts.py", line 33, in __enter__
    assert not check, message.format(**vars(self))
AssertionError: Value before is 0.0, not None

======================================================================
FAIL: test_delete (tests.sentry.digests.backends.test_redis.RedisBackendTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/digests/backends/test_redis.py", line 227, in test_delete
    backend.delete(timeline)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/exam-0.10.5-py2.7.egg/exam/asserts.py", line 49, in __exit__
    self.__raise_postcondition_error('invalid')
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/exam-0.10.5-py2.7.egg/exam/asserts.py", line 56, in __raise_postcondition_error
    raise AssertionError(message.format(**vars(self)))
AssertionError: Value changed to [True, True, False, False, False, False], not [False, False, False, False, False, False]

======================================================================
FAIL: test_scheduling (tests.sentry.digests.backends.test_redis.RedisBackendTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/digests/backends/test_redis.py", line 187, in test_scheduling
    with self.assertChanges(get_waiting_set_size, before=n, after=0), \
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/exam-0.10.5-py2.7.egg/exam/asserts.py", line 33, in __enter__
    assert not check, message.format(**vars(self))
AssertionError: Value before is 26, not 10

======================================================================
FAIL: test_ensure_timeline_scheduled_script (tests.sentry.digests.backends.test_redis.RedisScriptTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/digests/backends/test_redis.py", line 62, in test_ensure_timeline_scheduled_script
    assert ensure_timeline_scheduled(client, keys, (timeline, timestamp, 1, 10)) == 1
AssertionError

======================================================================
FAIL: test_add_tags (tests.sentry.manager.tests.SentryManagerTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/manager/tests.py", line 25, in test_add_tags
    assert len(results) == 2
AssertionError

======================================================================
FAIL: test_simple (tests.sentry.tasks.test_beacon.SendBeaconTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/mock-1.0.1-py2.7.egg/mock.py", line 1201, in patched
    return func(*args, **keywargs)
  File "/Users/wanghe/work/dev/sentry/tests/sentry/tasks/test_beacon.py", line 45, in test_simple
    }, timeout=5)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/mock-1.0.1-py2.7.egg/mock.py", line 846, in assert_called_once_with
    return self.assert_called_with(*args, **kwargs)
  File "/Users/wanghe/work/dev/sentry/env/lib/python2.7/site-packages/mock-1.0.1-py2.7.egg/mock.py", line 835, in assert_called_with
    raise AssertionError(msg)
AssertionError: Expected call: safe_urlopen('https://getsentry.com/remote/beacon/', json={'install_id': '216ea50ce254f4616cdea84726603f4badc3879a', 'version': '8.3.0.dev0.d91edd7f4d6a30d8c4db2d4db432026188e64527', 'data': {'events.24h': 0, 'organizations': 1, 'users': 0, 'projects': 1, 'teams': 1}, 'packages': {'foo': '1.0'}, 'admin_email': 'foo@example.com'}, timeout=5)
Actual call: safe_urlopen('https://getsentry.com/remote/beacon/', json={'install_id': '216ea50ce254f4616cdea84726603f4badc3879a', 'version': '8.3.0.dev0.d91edd7f4d6a30d8c4db2d4db432026188e64527', 'data': {'events.24h': 67, 'organizations': 1, 'users': 0, 'projects': 1, 'teams': 1}, 'packages': {'foo': '1.0'}, 'admin_email': 'foo@example.com'}, timeout=5)

======================================================================
FAIL: test_count_distinct (tests.sentry.tsdb.test_redis.RedisTSDBTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/tsdb/test_redis.py", line 133, in test_count_distinct
    (timestamp(dts[3]), 0),
AssertionError

======================================================================
FAIL: test_simple (tests.sentry.tsdb.test_redis.RedisTSDBTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/tsdb/test_redis.py", line 65, in test_simple
    (timestamp(dts[3]), 4),
AssertionError

======================================================================
FAIL: test_concurrent (tests.sentry.utils.test_cache.LockTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/utils/test_cache.py", line 51, in test_concurrent
    assert second.acquire() is False
AssertionError

======================================================================
FAIL: test_does_save_settings (tests.sentry.web.frontend.accounts.tests.AppearanceSettingsTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/accounts/tests.py", line 43, in test_does_save_settings
    assert options.get('language') == 'en'
AssertionError

======================================================================
FAIL: test_does_use_template (tests.sentry.web.frontend.accounts.tests.AppearanceSettingsTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/accounts/tests.py", line 28, in test_does_use_template
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_renders_with_required_context (tests.sentry.web.frontend.accounts.tests.NotificationSettingsTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/accounts/tests.py", line 138, in test_renders_with_required_context
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_valid_params (tests.sentry.web.frontend.accounts.tests.NotificationSettingsTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/accounts/tests.py", line 153, in test_valid_params
    assert options.get('alert_email') == 'foo@example.com'
AssertionError

======================================================================
FAIL: test_can_change_password (tests.sentry.web.frontend.accounts.tests.SettingsTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/accounts/tests.py", line 110, in test_can_change_password
    assert user.check_password('foobar')
AssertionError

======================================================================
FAIL: test_minimum_valid_params (tests.sentry.web.frontend.accounts.tests.SettingsTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/accounts/tests.py", line 98, in test_minimum_valid_params
    assert user.name == params['name']
AssertionError

======================================================================
FAIL: test_renders_with_required_context (tests.sentry.web.frontend.accounts.tests.SettingsTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/accounts/tests.py", line 68, in test_renders_with_required_context
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_requires_email (tests.sentry.web.frontend.accounts.tests.SettingsTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/accounts/tests.py", line 76, in test_requires_email
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_requires_name (tests.sentry.web.frontend.accounts.tests.SettingsTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/accounts/tests.py", line 85, in test_requires_name
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_login_invalid_password (tests.sentry.web.frontend.test_auth_login.AuthLoginTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_auth_login.py", line 31, in test_login_invalid_password
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_register_renders_correct_template (tests.sentry.web.frontend.test_auth_login.AuthLoginTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_auth_login.py", line 68, in test_register_renders_correct_template
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_renders_correct_template (tests.sentry.web.frontend.test_auth_login.AuthLoginTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_auth_login.py", line 19, in test_renders_correct_template
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_renders_with_context (tests.sentry.web.frontend.test_create_organization.CreateOrganizationTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_create_organization.py", line 18, in test_renders_with_context
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_renders (tests.sentry.web.frontend.test_error_page_embed.ErrorPageEmbedTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_error_page_embed.py", line 33, in test_renders
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_submission (tests.sentry.web.frontend.test_error_page_embed.ErrorPageEmbedTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_error_page_embed.py", line 42, in test_submission
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_explicit_delete (tests.sentry.web.frontend.test_remove_account.RemoveAccountTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_remove_account.py", line 87, in test_explicit_delete
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_implicit_delete (tests.sentry.web.frontend.test_remove_account.RemoveAccountTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_remove_account.py", line 57, in test_implicit_delete
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_renders_with_context (tests.sentry.web.frontend.test_remove_account.RemoveAccountTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_remove_account.py", line 42, in test_renders_with_context
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_owner_can_load (tests.sentry.web.frontend.test_remove_organization.RemoveOrganizationPermissionTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_remove_organization.py", line 21, in test_owner_can_load
    self.assert_owner_can_access(self.path)
  File "/Users/wanghe/work/dev/sentry/src/sentry/testutils/cases.py", line 383, in assert_owner_can_access
    self.assert_can_access(user, path)
  File "/Users/wanghe/work/dev/sentry/src/sentry/testutils/cases.py", line 288, in assert_can_access
    assert resp.status_code >= 200 and resp.status_code < 300
AssertionError

======================================================================
FAIL: test_renders_with_context (tests.sentry.web.frontend.test_remove_organization.RemoveOrganizationTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_remove_organization.py", line 37, in test_renders_with_context
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_success (tests.sentry.web.frontend.test_remove_organization.RemoveOrganizationTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_remove_organization.py", line 52, in test_success
    assert organization.status == OrganizationStatus.PENDING_DELETION
AssertionError

======================================================================
FAIL: test_owner_can_load (tests.sentry.web.frontend.test_remove_project.RemoveProjectPermissionTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_remove_project.py", line 22, in test_owner_can_load
    self.assert_owner_can_access(self.path)
  File "/Users/wanghe/work/dev/sentry/src/sentry/testutils/cases.py", line 383, in assert_owner_can_access
    self.assert_can_access(user, path)
  File "/Users/wanghe/work/dev/sentry/src/sentry/testutils/cases.py", line 288, in assert_can_access
    assert resp.status_code >= 200 and resp.status_code < 300
AssertionError

======================================================================
FAIL: test_team_admin_can_load (tests.sentry.web.frontend.test_remove_project.RemoveProjectPermissionTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_remove_project.py", line 19, in test_team_admin_can_load
    self.assert_team_admin_can_access(self.path)
  File "/Users/wanghe/work/dev/sentry/src/sentry/testutils/cases.py", line 338, in assert_team_admin_can_access
    self.assert_can_access(user, path)
  File "/Users/wanghe/work/dev/sentry/src/sentry/testutils/cases.py", line 288, in assert_can_access
    assert resp.status_code >= 200 and resp.status_code < 300
AssertionError

======================================================================
FAIL: test_deletion_flow (tests.sentry.web.frontend.test_remove_project.RemoveProjectTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_remove_project.py", line 51, in test_deletion_flow
    assert Project.objects.get(id=self.project.id).status == ProjectStatus.PENDING_DELETION
AssertionError

======================================================================
FAIL: test_renders_template_with_get (tests.sentry.web.frontend.test_remove_project.RemoveProjectTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_remove_project.py", line 41, in test_renders_template_with_get
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_owner_can_load (tests.sentry.web.frontend.test_remove_team.RemoveTeamPermissionTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_remove_team.py", line 21, in test_owner_can_load
    self.assert_owner_can_access(self.path)
  File "/Users/wanghe/work/dev/sentry/src/sentry/testutils/cases.py", line 383, in assert_owner_can_access
    self.assert_can_access(user, path)
  File "/Users/wanghe/work/dev/sentry/src/sentry/testutils/cases.py", line 288, in assert_can_access
    assert resp.status_code >= 200 and resp.status_code < 300
AssertionError

======================================================================
FAIL: test_team_admin_can_load (tests.sentry.web.frontend.test_remove_team.RemoveTeamPermissionTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_remove_team.py", line 18, in test_team_admin_can_load
    self.assert_team_admin_can_access(self.path)
  File "/Users/wanghe/work/dev/sentry/src/sentry/testutils/cases.py", line 338, in assert_team_admin_can_access
    self.assert_can_access(user, path)
  File "/Users/wanghe/work/dev/sentry/src/sentry/testutils/cases.py", line 288, in assert_can_access
    assert resp.status_code >= 200 and resp.status_code < 300
AssertionError

======================================================================
FAIL: test_does_load (tests.sentry.web.frontend.test_remove_team.RemoveTeamTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_remove_team.py", line 36, in test_does_load
    assert resp.status_code == 200
AssertionError

======================================================================
FAIL: test_valid_params (tests.sentry.web.frontend.test_remove_team.RemoveTeamTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/web/frontend/test_remove_team.py", line 43, in test_valid_params
    assert resp['Location'] == 'http://testserver' + reverse('sentry')
AssertionError

======================================================================
FAIL: test_event_user (tests.sentry.test_event_manager.EventManagerTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/test_event_manager.py", line 453, in test_event_user
    event.group.id: 1,
AssertionError

======================================================================
FAIL: test_updates_group (tests.sentry.test_event_manager.EventManagerTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/test_event_manager.py", line 181, in test_updates_group
    assert group.times_seen == 2
AssertionError

======================================================================
FAIL: test_updates_group_with_fingerprint (tests.sentry.test_event_manager.EventManagerTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/wanghe/work/dev/sentry/tests/sentry/test_event_manager.py", line 202, in test_updates_group_with_fingerprint
    assert group.times_seen == 2
AssertionError

----------------------------------------------------------------------
Ran 1033 tests in 120.895s

FAILED (failures=52, errors=14)
Destroying test database for alias 'default'...
