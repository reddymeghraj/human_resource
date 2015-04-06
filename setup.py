from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='human_resource',
    version=version,
    description='Human Resource for medical',
    author='wayzontech',
    author_email='wayzon@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
