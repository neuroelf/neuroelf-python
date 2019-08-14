#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'imageio>=2.5.0',
]

setuptools.setup(
    name="neuroelf",
    version="0.0.1",
    description="NeuroElf for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jochen Weber",
    author_email="info@neuroelf.net",
    url="https://github.com/neuroelf/neuroelf-python",
    packages=setuptools.find_packages(),
    package_dir={'neuroelf': 'neuroelf'},
    python_requires=">=3.6",
    install_requires=requires,
    license='BSD',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent"
    ],
)
