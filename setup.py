import os
import sys

from setuptools import setup
from codecs import open

# Get the long description from the README.md file
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Don't import guesty module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'guesty'))
from version import VERSION

setup(
    name='guesty-python',
    version=VERSION,
    description='guesty python library',
    long_description=long_description,
    license='MIT',
    author='Denis Angell',
    author_email='denis@harpangell.com',
    url='https://bitbucket.org/angellenterprises/guesty-python',
    packages=['guesty', 'guesty.resource'],
    install_requires=['requests >= 2.8.1'],
    test_suite='pytest',  # 'guesty.test.all?'
    tests_require=['pytest'],  # TODO: stripe uses unittest2 and mock?
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
    ],
)
