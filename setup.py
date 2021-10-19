from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='1.0',
    author='nicholas Hillier',
    author_email='nicholas@ghostmonk.com',
    description='A utility for backing up PostgreSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://www.github.com/ghostmonk/pgbackup',
    packages=find_packages('src'),
)

