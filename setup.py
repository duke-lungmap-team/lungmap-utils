from setuptools import setup

setup(
    name='lungmap_utils',
    version='1.1',
    packages=['lungmap_utils'],
    license='BSD 2-Clause License',
    long_description=open('README.md').read(),
    author='Scott White',
    description='Python utilities for interacting with LungMap.net APIs',
    install_requires=[
        'SPARQLWrapper',
        'requests'
    ]
)
