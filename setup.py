#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='octodns_lexicon',
    version='0.1.dev4',
    description='Lexicon provider for OctoDNS',
    url='http://github.com/doddo/octodns-lexiconprovider',
    author='Petter Hassberg',
    author_email='dr.doddo@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    py_modules=["octodns_lexicon"],
    classifiers=[
         'Intended Audience :: Developers',
         'Intended Audience :: System Administrators',
         'Topic :: Software Development :: Libraries :: Python Modules',
         'Topic :: Internet :: Name Service (DNS)',
         'Topic :: System :: Systems Administration',
         'Topic :: Utilities',
         "License :: OSI Approved :: MIT License",
         'Programming Language :: Python :: 3',
    ],
    tests_require=["pytest"],
    install_requires=[
        'octodns>=0.9.21',
        'dns-lexicon>=3.3.23']
)
