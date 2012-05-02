import logging
import sys

from setuptools import setup, find_packages
from logging import StreamHandler

_log = logging.getLogger()
_log.setLevel(logging.DEBUG)
_log.addHandler(StreamHandler(sys.stderr))

setup(
    name='sensor-node-logger',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=["SQLAlchemy"],
    )
