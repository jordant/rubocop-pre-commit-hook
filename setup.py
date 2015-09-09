#!/usr/bin/env python

from distutils.core import setup

setup(name='Distutils',
      version='0.1',
      description='Python chef tools',
      author='Jordan Tardif',
      author_email='jordan.tardif@gmail.com',
      url='https://github.com/jordant/chef-tools.git',
      scripts=['pre_commit_hooks/check_rubocop'],
      )
