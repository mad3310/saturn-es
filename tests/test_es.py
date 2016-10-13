# coding=utf-8

__import__('framework').init()

import unittest
from datetime import datetime

from mimas.es.context import init_context
from mimas.es import ElasticsearchEngine


APP = 'saturn'
SERVERS = '10.154.255.131:9200,10.154.255.242:9200,10.154.255.90:9200'


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

        doc = {
            'author': 'kimchy',
            'text': 'Elasticsearch: cool. bonsai cool.',
            'timestamp': datetime.now(),
        }

        result = engine.add("test_index", "tweet", doc)
        self.assertEqual(True, result.get('created'))

        result = engine.add("test_indexs", "tweetd", doc)
        self.assertEqual(True, result.get('created'))

if __name__ == '__main__':
    unittest.main()
