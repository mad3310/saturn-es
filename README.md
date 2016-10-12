saturn-es
=========

---
saturn-es是Elasticsearch系统包，包含了一些常用的方法。

```python
app = 'saturn'
from mimas.es.context import init_context
from mimas.es import ElasticsearchEngine

# context创建只需传入APP
context = init_context(app)
es = ElasticsearchEngine.init_by_context(context)

# 也可自己创建context：
servers = '10.154.255.131:9200,10.154.255.242:9200,10.154.255.90:9200'
context = init_context(APP='saturn',
                       ELASTICSEARCH_SERVERS=servers)
es = ElasticsearchEngine.init_by_context(context)
```
