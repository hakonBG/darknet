#!/usr/bin/env python

from distutils.core import setup

setup(
    name='darknet',
    package_dir={'': 'python'},
    packages=['darknet'],
    version='1.0',
    description='Python wrapper for darknet library',
    url='https://pjreddie.com/darknet/'
    )

