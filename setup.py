from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='yanwu',
   version='0.0.2',
   description='A tiny framework for python cli tools',
   long_description=long_description,
   license='MIT',
   author='Richard Ma',
   author_email='richard.ma.19850509@gmail.com',
   url='https://github.com/richard-ma/yanwu',
   packages=['yanwu'],  #same as name
   install_requires=[],
)