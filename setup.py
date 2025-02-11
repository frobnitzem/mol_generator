#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="src",
    version="0.1.0",
    description="Molecule Generator",
    author="David M. Rogers",
    author_email="predictivestatmech gmail",
    url="https://github.com/frobnitzem/mol_generator",
    install_requires=["lightning", "hydra-core"],
    packages=find_packages(),
    # use this to customize global commands available in the terminal after installing the package
    entry_points={
        "console_scripts": [
            "mol_train    = src.train:main",
            "mol_generate = src.eval:main",
        ]
    },
)
