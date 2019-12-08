import logging
import os

from setuptools import find_packages, setup


logging.basicConfig()



# load requirements from requirements.txt
PKG_ROOT = os.path.abspath(os.path.dirname(__file__))

setup(
    name="rtk8s",
    version="0.0.1",
    packages=find_packages(exclude=["contrib", "test-docs", "tests*"]),
    install_requires=["click", "pyyaml"],
    include_package_data=True,
    scripts=[
        "./rtk8s/bin/rtkctl",
    ],
)