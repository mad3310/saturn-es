#!/bin/bash

MODULE_TAR_PATH=/tmp/es_pack
cd $MODULE_TAR_PATH
ES_MODULE_PATH=es_pack
mkdir $ES_MODULE_PATH && tar zxf *.tar.gz -C ./$ES_MODULE_PATH --strip-components 1
cd $ES_MODULE_PATH && python setup.py build && python setup.py install && cd -

exit 0
