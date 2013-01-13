#!/usr/bin/env python
from setuptools import setup
import os

__doc__ = """
Widgy widgy widgy
"""


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


install_requires = [
    'mezzanine >= 1.3.0',
    'django-fusionbox',
    'django-treebeard',
    'South',
    'PyScss >= 1.1.4',
    'six',
]

version = '0.0.1'

setup(
    name='widgy',
    version=version,
    description=__doc__,
    long_description=read('README'),
    packages=[
        'widgy',
        'widgy.contrib',
        'widgy.contrib.cms',
    ],
    install_requires=install_requires,
    dependency_links=[
        'http://github.com/fusionbox/django-fusionbox/tarball/master#egg=django-fusionbox-0.0.2',
        'http://github.com/Kronuz/pyScss/tarball/master#egg=pyscss-1.1.4',
    ],
    zip_safe=False,
)