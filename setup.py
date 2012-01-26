from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()



version = '0.9.dev'

install_requires = [
    'BeautifulSoup',
]


setup(name='readability',
    version=version,
    description="Python version of readability.js",
    long_description=README + '\n\n',
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='html parsing readability',
    author='Abhinav Gupta',
    license='GPL3',
    py_modules=["readability"],
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['readability=readability:main']
    }
)
