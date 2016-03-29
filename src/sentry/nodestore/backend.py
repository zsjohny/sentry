# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from sentry.nodestore.base import NodeStorage
from sentry.utils.cache import memoize
from tarantool import Connection


class TarantoolNodeStorage(NodeStorage):
    """
    A Tarantool-based backend for storing node data.
    You can initialize tarantool,create space for 'sentry'
    grant user for sentry to read and write
    >>> TarantoolNodeStorage(
    ...     servers='127.0.0.1',
    ...     port = 3301,
    ...     space='sentry',
    ... )
    """
    def __init__(self, server, port, keyspace='sentry'):
        self.server = server
        self.port = port
        self.keyspace = keyspace
        super(TarantoolNodeStorage, self).__init__()

    @memoize
    def connection(self):
        return Connection(self.server, self.port)

    @memoize
    def space(self):
        return self.connection.space(self.keyspace)

    def delete(self, id):
        self.space.delete(id)

    def get(self, id):
        return self.space.select(id).data[0][1]

    def get_multi(self, id_list):
        if len(id_list) == 1:
            id = id_list[0]
            return {id: self.get(id)}
        results = {}
        for id in id_list:
            results[id] = self.get(id)
        return results

    def set(self, id, data):
        self.space.insert((id, data))
