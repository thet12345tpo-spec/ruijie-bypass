from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("free1_fixed.py")
)
