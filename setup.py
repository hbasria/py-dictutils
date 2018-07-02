#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='py-dictutils',
    version='0.1.2',
    description='dictionary utils',
    long_description=long_description,
    author='Hasan Basri',
    author_email='hbasria@gmail.com',
    license='MIT',
    keywords='AttrDict OrderedAttrDict xml_to_dict',
    url='https://github.com/hbasria/py-dictutils',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    test_suite='tests'
)
