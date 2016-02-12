#!/usr/bin/env python

import os

from setuptools import setup

from getTimer import VERSION

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst'), 'rU') as f:
    long_description = f.read()

required = [
]

extras = {
}

setup(
    name='getTimer',
    version=VERSION,
    packages=['getTimer', 'getTimer.resources'],
    url='https://github.com/maxwellgerber/getTimer',
    license='MIT',
    author='Maxwell Gerber',
    author_email='maxwell.gerber42@gmail.com',
    description='Get python datetime objects from CLI users easily',
    long_description=long_description,
    install_requires=required,
    extras_require=extras,
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'Topic :: System :: Shells',
        'Topic :: System :: System Shells',

        'Environment :: Console :: Curses',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)