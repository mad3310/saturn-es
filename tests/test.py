# coding=utf-8

import unittest
import datetime
import time
import requests

from mimas.es.engine import ElasticsearchsEngine


class context():
    config = {'ELASTICSEARCH_HOSTS': '10.154.255.131:9200,10.154.255.242:9200,10.154.255.90:9200'}


class ESTestCase(unittest.TestCase):
    es = ElasticsearchsEngine(context=context)
    es.connect()

    def write_test(self):
        result = self.es.add("test_index", "test_type", "test_doc")
        self.assertEqual(True, result.get('created'))
