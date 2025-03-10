from setuptools import setup

setup(
   name='PracticeLibrary',
   version='1.0',
   description='Library for python practice and development.',
   author='John Kacir',
   author_email='kacirjt@gmail.com',
   packages=['PracticeLibrary', 'PracticeLibrary.*'],  #same as name
   install_requires=['wheel', 'pandas', 'PyYaml'], #external packages as dependencies
)