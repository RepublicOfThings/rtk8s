import logging
import os

from setuptools import find_packages, setup


MANIFEST_DIRS = ["rtk8s/templates"]
# .rtk8s_apps/v1/default/src

logging.basicConfig()


def build_manifest():

    paths = []
    for included in MANIFEST_DIRS:
        for root, dirs, files in os.walk(included):
            for file in files:
                paths.append(os.path.join(root, file))

    with open("MANIFEST.in", "w") as manifest:
        manifest.write("\n".join([f"include {x}" for x in paths]))


PKG_ROOT = os.path.abspath(os.path.dirname(__file__))

build_manifest()

setup(
    name="rtk8s",
    version="0.0.5",
    packages=find_packages(exclude=["contrib", "test-docs", "tests*"]),
    install_requires=["click", "pyyaml"],
    include_package_data=True,
    scripts=[
        "./rtk8s/bin/rtkctl",
    ],
)