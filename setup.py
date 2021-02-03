# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in metactical_custom/__init__.py
from metactical_custom import __version__ as version

setup(
	name='metactical_custom',
	version=version,
	description='a',
	author='shahid',
	author_email='shahid@codessoft.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
