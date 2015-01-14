#!/usr/bin/env python

"""Setup script for the PyMeta distribution."""
from distutils.core import setup
setup(
    name="PyMeta3",
    version="0.5.0",
    url="https://github.com/wbond/pymeta3",
    description="Pattern-matching language based on OMeta for Python 2 and 3",
    long_description=open('README').read(),
    author="wbond",
    author_email="will@wbond.net",
    license="MIT License",
    packages=["pymeta"]
    )
