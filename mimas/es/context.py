# -*- coding: utf-8 -*-


class ElasticsearchContext(object):

    def __init__(self, **config):
        assert config.get('APP')
        assert config.get('ELASTICSEARCH_SERVER')
        self.config = config


def get_by_env_prefix(name):
    mod = __import__('envcfg.json.%s' % name,
                     fromlist=[name])
    config = vars(mod)
    return config


def init_context(app_config_prefix_name, server=None):
    develop_mode = True
    name = app_config_prefix_name

    config = get_by_env_prefix(name)
    elasticsearch_server = server or config.get('ELASTICSEARCH_SERVER')
    if not elasticsearch_server:
        raise Exception('ELASTICSEARCH_SERVER should not be empty.')

    return ElasticsearchContext(APP=app_config_prefix_name,
                                DEVELOP_MODE=develop_mode,
                                ELASTICSEARCH_SERVER=elasticsearch_server)
