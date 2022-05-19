# !/usr/bin/env python

from setuptools import setup

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

package_version = None
exec(open('replicate/package_version.py').read())

setup(
    name="replicate",
    packages=["replicate"],
    version=package_version,
    description="Python client for Replicate",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Replicate, Inc.",
    license="BSD",
    url="https://github.com/replicate/replicate-python",
    python_requires=">=3.6",
    install_requires=["requests", "pydantic"],
    classifiers=[],
)
