#!usr/bin/env python

from setuptools import setup, find_packages

setup(name="pig",
	version="0.1",
	description="Test sample",
	url="https://github.com/hfxer34/python-3.4-tool",
	packages=find_packages(),
	entry_points="""
	[console_scripts]
	pig = pig.pig:main
	""",
	)
