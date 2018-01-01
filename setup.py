'''One-line description of package

'''
import os
from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace("\r","") # Do not forget this line
except:
    print("Pandoc not found. Long_description conversion failure.")

    # pandoc is not installed, fallback to using raw contents
    with open('README.md') as f:
        long_description = f.read()

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as version_file:
    version = version_file.read().strip()

with open(os.path.join(os.path.dirname(__file__), "requirements.txt"), "r") as f:
    requirements = f.read().splitlines()

WHITESPACE_SEP_KEYWORDS = ''

CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Topic :: Scientific/Engineering",
    ]


setup(name='blank_python_project',
      version=version,
      description=__doc__,
      long_description=long_description,
      url="https://github.com/kinverarity1/blank_python_project",
      author="Kent Inverarity",
      author_email="kinverarity@hotmail.com",
      license="MIT",
      classifiers=CLASSIFIERS,
      keywords=WHITESPACE_SEP_KEYWORDS,
      packages=['blank_python_project', ],
      install_requires=requirements,
      entry_points={
          'console_scripts': [
              # 'script_executable_name = blank_python_project.module:function',
          ],
      }
      )
