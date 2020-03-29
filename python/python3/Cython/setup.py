from distutils.core import setup
from Cython.Build import cythonize
import re

prog = input('Enter the program name: ')

setup(
   ext_modules = cythonize(prog) # if re.search('*.py*', prog) else cythonize(prog + '.py')
)
