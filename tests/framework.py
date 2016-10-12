# -*- coding: utf-8 -*-

import os
import sys


def init():
    TEST_DIR = os.path.dirname(os.path.realpath(__file__))
    LIB_DIR = os.path.dirname(TEST_DIR)
    sys.path.insert(0, LIB_DIR)
    reload(sys)
    sys.setdefaultencoding('utf8')
