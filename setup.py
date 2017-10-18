from setuptools import setup, find_packages

setup(
    name='CommandoMaths',
    author='John Crickett',
    author_email='john@trivialbusiness.co.uk',
    version='0.1.0.dev',
    packages=find_packages(),
    license='See LICENSE',
    long_description=open('README.md').read(),
    install_requires=["pygame >= 1.9.2a0"
                      ],
    entry_points={
        'console_scripts': [
            'commandomaths=commandomaths.main:main',
        ],
    },
)