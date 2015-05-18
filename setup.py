# -*- coding:utf-8 -*-
# PROJECT_NAME : sandiego
# AUTHOR       : younger shen
# EMAIL        : younger.x.shen@gmail.com

from setuptools import setup, find_packages

version = '0.0.1a1'

setup(name='sandiego',
      version=version,
      description="a lightweight web framework, only for python3 and django haters",
      long_description="""\
      a lightweight web framework, only for python3 and django haters
      """,
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 3.4',
                   ],
      keywords='sandiego, web framework',
      author='younger shen',
      author_email='younger.x.shen@gmail.com',
      url='https://github.com/youngershen/sandiego',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=['jinja2'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
