#!/usr/bin/env python

from setuptools import setup, find_packages

install_description = '''
saturn es
===========

Python library for saturn elasticsearch
'''

setup(
    name='saturn-es',
    version='0.0.1',
    license='SATURN',
    description='Python library for saturn elasticsearch system',
    long_description=install_description,
    author='wangyiyang',
    author_email='wangyiyang@le.com',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'python-envcfg>=0.2.0',
        'elasticsearch==2.4.0',
        'dsnparse>=0.1.3',
    ],
    classifiers=['Private :: Do Not Upload'],
)
