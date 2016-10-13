#!/bin/bash

MODULE_TAR_PATH=/tmp/saturn-es
cd $MODULE_TAR_PATH
ES_MODULE_PATH=saturn-es
mkdir $ES_MODULE_PATH && tar zxf *.tar.gz -C ./$ES_MODULE_PATH --strip-components 1
cd $ES_MODULE_PATH && python setup.py build && python setup.py install && cd -

exit 0
