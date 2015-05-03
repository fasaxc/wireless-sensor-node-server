import logging
import sys

from setuptools import setup, find_packages
from logging import StreamHandler

_log = logging.getLogger()
_log.setLevel(logging.DEBUG)
_log.addHandler(StreamHandler(sys.stderr))

setup(
    name='sensor-node-logger',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        "SQLAlchemy",
        "pySerial",
        "python-cjson",
        "tornado",
    ],
    entry_points={
        'console_scripts': [
            'sensor-server = wirelesssensor.server:main',
            'sensor-logger = wirelesssensor.logger:main',
        ],
    }
)
