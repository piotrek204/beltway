# -*- coding: utf-8 -*-
import os.path
import re
import warnings
import sys
import uuid


from setuptools import setup, find_packages
from beltway import __version__ as version


long_description = """
Beltway is a threaded WAMP client (a loose port of Autobahn).
"""

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

setup(
    name='beltway',
    version=version,
    author='Unspecified',
    url='https://github.com/piotrek204/beltway',
    license='MIT',
    description='Threaded WAMP client',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
    setup_requires=['nose>=1.0'],
    tests_require=['nose>=1.0.3'],
    test_suite='nose.collector',
    zip_safe=False
)
