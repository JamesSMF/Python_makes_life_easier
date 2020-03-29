from distutils.core import setup
from Cython.Build import cythonize

setup(name="My first Cython app",
      ext_modules=cythonize('split_urls.pyx'),  # accepts a glob pattern
      )
