#!/usr/bin/env python

import sys

from setuptools import setup, find_packages


def which(program):
    import os

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    f_path, _ = os.path.split(program)
    if f_path:
        if is_exe(program):
            return program
    else:
        for path in os.environ['PATH'].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


if sys.version_info.major == 3 and sys.version_info.minor < 3:
    print('Unfortunately, your python version is not supported!\n Please upgrade at least to python 3.3!')
    sys.exit(1)

if sys.platform == 'darwin' or sys.platform == 'win32':
    print('Unfortunately, we do not support your platform %s' % sys.platform)
    sys.exit(1)

if which('protoc') is None:
    print('Unable to find protoc executable, please install it.')
    print('On Debian-like OS, run sudo apt-get install protobuf-compiler')
    sys.exit(1)

install_requires = [
    'mitmproxy==3.0.4',
    'bitstring==3.1.5',
    'flatten-json==0.1.6',
    'requests==2.18.4',
    'beautifulsoup4==4.6.0',
    'tinycss==0.4',
    'yara-python==3.7.0',
    'yapsy==1.11.223'
]

setup(name = 'phorcys',
      version = '1.0.0',
      description = 'Network payload analyzer',
      author = 'U+039b',
      author_email = 'forensic@0x39b.fr',
      url = 'https://github.com/U039b/Phorcys.git',
      packages = find_packages(exclude = ['*.tests', '*.tests.*', 'test*', 'tests']),
      install_requires = install_requires,
      # zip_safe = False,
      scripts = ['./phorcys_decode.py'],
      classifiers = [
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: GNU Affero General Public License v3',
          'Natural Language :: English',
          'Topic :: Security',
          'Topic :: Utilities',
      ]
      )
