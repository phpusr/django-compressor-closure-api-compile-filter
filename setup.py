#!/usr/bin/env python3

import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='django-compressor-closure-api-compile-filter',
    version='0.1',
    author='phpusr',
    author_email='phpusr@gmail.com',
    description='Django Compressor Closure API Compile Filter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/phpusr/django-compressor-closure-api-compile-filter',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    test_suite='tests'
)
