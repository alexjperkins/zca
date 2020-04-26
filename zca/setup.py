import setuptools
from distutils.core import setup


setup(
    name='sigalgo',
    version='0.1.0',
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    license='SIG',
    long_description="Algorithm for time series data cleaning"
)
