#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup


install_description = '''
saturn es
===========

Python library for saturn elasticsearch
'''

setup(
    name='saturn-es',
    version='0.0.3',
    packages=['mimas', 'mimas.es'],
    author='chenwenquan',
    author_email='chenwenquan@le.com',
    description='Python library for saturn elasticsearch System',
)
