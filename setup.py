from setuptools import setup

setup(
    name='lungmap_utils',
    version='1.0',
    packages=['lungmap_utils'],
    license='BSD 2-Clause License',
    long_description=open('README.md').read(),
    author='Scott White',
    description='Python utilities for interacting with LungMap.net APIs',
    install_requires=[
        'numpy (==1.13)',
        'opencv-python (==3.2.0.7)',
        'scipy (==0.19.1)',
        'pandas (==0.19.2)',
        'scikit_learn (==0.18.2)', 'SPARQLWrapper', 'requests'
    ]
)
