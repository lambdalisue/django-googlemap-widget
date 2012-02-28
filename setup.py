#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author:        alisue
# date:            2011/03/22
#
from setuptools import setup, find_packages

version = "0.1.3"

def read(filename):
    import os.path
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name="django-googlemap-widget",
    version=version,
    description = "Googlemap field, widget, model for Django",
    long_description=read('README.rst'),
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords = "django googlemap map ajax",
    author = "Alisue",
    author_email = "lambdalisue@hashnote.net",
    url=r"https://github.com/lambdalisue/django-googlemap-widget",
    download_url = r"https://github.com/lambdalisue/django-googlemap-widget/tarball/master",
    license = 'BSD',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = True,
    install_requires=['setuptools',],
)

