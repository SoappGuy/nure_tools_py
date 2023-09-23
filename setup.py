from setuptools import setup, find_packages

setup(
    name='nure_tools',
    version='1.0.2',
    author='pencel_z_kavunom',
    packages=find_packages(),
    description="Simple python library to use nure-dev API",
    install_requires=[
        'requests>=2.31.0',
    ],
)
