#!/usr/bin/env python

from distutils.core import setup

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
    packages=['mimas'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'elasticsearch==2.4.0',
    ],
    classifiers=['Private :: Do Not Upload'],
)
