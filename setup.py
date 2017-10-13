#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 11:52
# @Author  : wangzz
# @File    : setup.py.py

from setuptools import find_packages, setup

setup(name='demo',
      version='0.0.1',
      author='wangzz',
      author_email='wzhizhao@gmail.com',
      description='',
      license='PRIVATE',
      packages=find_packages(),
      install_requires=[
          'tornado'
      ],
      entry_points={
          'console_scripts': [
              'demo = demo.main:main',
          ],
      })
