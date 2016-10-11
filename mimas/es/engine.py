# -*- coding: utf-8 -*-

import threading
import Elasticsearch


class ElasticsearchsEngine(object):

    """
    ElasticSearch Engine
    """

    def __init__(self, context, retry=1):
        self.context = context
        self.retry = retry
        self.lock = threading.Lock()

    def __repr__(self):
        return '<Elasticsearch Engine server=%s>' % self.url

    def connect(self):
        # 获取elasticsearch实例
        host = self.context.config.get('ELASTICSEARCH_HOST')
        server = Elasticsearch(host)
        return server

    def search(self):
        # 搜索
        pass

    def get(self):
        # 获取索引
        pass

    def add(self):
        # 添加索引
        pass

    def delete(self):
        # 删除索引
        pass
