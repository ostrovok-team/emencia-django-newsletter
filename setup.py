import os
from setuptools import setup
from setuptools import find_packages

__version__ = '0.3.dev'
__license__ = 'BSD License'

__author__ = 'Fantomas42'
__email__ = 'fantomas42@gmail.com'

__url__ = 'http://emencia.fr/'

setup(name='emencia',
      version=__version__,
      description='A Django app for sending emencia by email to a contact list.',
      long_description=open('README.rst').read() + '\n' +
                       open(os.path.join('docs', 'HISTORY.txt')).read(),
      keywords='django, emencia, mailing',
      classifiers=[
          'Framework :: Django',
          'Programming Language :: Python',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: BSD License',
          'Development Status :: 5 - Production/Stable',
          'Topic :: Software Development :: Libraries :: Python Modules',],

      author=__author__,
      author_email=__email__,
      url=__url__,
      license=__license__,
      packages=find_packages(exclude=['demo']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'html2text',
                        'python-dateutil==1.5',
                        'beautifulsoup4',
                        'django-tagging',
                        'vobject',
                        'xlwt',
                        'xlrd'])
