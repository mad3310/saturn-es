# coding=utf-8

__import__('framework').init()

import unittest
from datetime import datetime

from mimas.es.context import init_context
from mimas.es import ElasticsearchEngine


APP = 'saturn'
SERVERS = ""

MAPPING = {
    "tweet": {
        "properties": {
            "author": {"type": "string", "index": "not_analyzed"},
            "text": {"type": "string", "index": "not_analyzed"},
            "timestamp": {"type": "date", "index": "not_analyzed"}
        }
    }
}

INDEX_BODY = {
    "mappings": MAPPING,
}

TEMPLATE = {
    "template": "te*",
    "mappings": MAPPING,
}


class EsEngineTest(unittest.TestCase):

    def test_context(self):
        context = init_context(APP, servers=SERVERS)
        assert context
        assert context.config.get("APP")
        assert context.config.get("ELASTICSEARCH_SERVERS")

    def test_engine(self):
        context = init_context(APP, servers=SERVERS)
        engine = ElasticsearchEngine.init_by_context(context)
        assert engine
        assert engine.hosts

        r = engine.put_template('mcluster_satus', TEMPLATE)
        assert r.get('acknowledged')
        r = engine.exists_template('mcluster_satus')
        assert r

        doc = {
            'author': 'kimchy',
            'text': 'Elasticsearch: cool. bonsai cool.',
            'timestamp': datetime.now()
        }

        result = engine.add("test", "tweet", doc)
        self.assertEqual(True, result.get('created'))

        result = engine.add("test", "facebook", doc)
        self.assertEqual(True, result.get('created'))

        result = engine.add("tessss", "tweet", doc)
        self.assertEqual(True, result.get('created'))
