#!/usr/bin/env python

"""
TT - Time Tracker
-------------

Elegant project time tracking.
"""
from setuptools import setup


setup(
    name='S3Manager',
    version='0.1',
    url='https://github.com/bwghughes/tt',
    license='See License',
    author='Ben Hughes',
    author_email='bwghughes@gmail.com',
    description='Elegant project time tracking.',
    long_description=__doc__,
    py_modules=['tt'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
    ],
    entry_points={
        'console_scripts':
            ['tt=tt:main']
    },
    classifiers=[
        'Environment :: Command Line Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)