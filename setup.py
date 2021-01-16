#!/usr/bin/env python

from setuptools import setup

setup(
    name="target-bigquery",
    version="0.10.2",
    description="Singer.io target for writing data to Google BigQuery",
    author="Adswerve",
    url="https://github.com/adswerve/target-bigquery",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    packages=["target_bigquery"],
    install_requires=[
        "singer-python==5.9.0",
        "google-cloud==0.34.0",
        "google-cloud-bigquery==1.25.0",
    ],
    entry_points="""
        [console_scripts]
        target-bigquery=target_bigquery:main
      """
)
