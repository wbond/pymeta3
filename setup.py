#!/usr/bin/env python

"""Setup script for the PyMeta distribution."""
from distutils.core import setup
setup(
    name="PyMeta3",
    version="0.5.1",
    url="https://github.com/wbond/pymeta3",
    description="Pattern-matching language based on OMeta for Python 3 and 2",
    long_description=open('README').read(),
    author="wbond",
    author_email="will@wbond.net",
    license="MIT License",
    packages=["pymeta"],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ]
    )
