# -*- coding: utf-8 -*-

import logging

from elasticsearch import Elasticsearch


class ElasticsearchsEngine(object):
    """
    ElasticSearch Engine
    """

    def __init__(self, context=None):
        self.context = context
        self.es = None

    def __repr__(self):
        return '<Elasticsearch Engine server=%s>' % self.hosts

    def connect(self):
        es_hosts = self.context.config.get('ELASTICSEARCH_HOSTS')
        self.hosts = map(lambda x: dict(host=x.split(':')[0],
                                        port=x.split(':')[1]),
                         es_hosts.split(','),
                         )
        print self.hosts
        self.es = Elasticsearch(
            self.hosts,
            sniff_on_start=False,
            sniff_on_connection_fail=True,
            sniffer_timeout=300,
            sniff_timeout=10,
        )
        return self.es

    def add(self, index, doc_type, body, doc_id=None):
        try:
            return self.es.index(index=index, doc_type=doc_type,
                                 body=body, id=doc_id)
        except Exception as e:
            logging.error(e, exc_info=True)

    def delete(self, index, doc_type, doc_id):
        try:
            self.es.delete(index=index, doc_type=doc_type, id=doc_id)
        except Exception as e:
            logging.error(e, exc_info=True)
