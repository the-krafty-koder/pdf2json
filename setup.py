from distutils.core import setup
setup(
  name = 'pdf2json',
  packages = ['pdf2json'],
  version = '0.2',
  license='MIT',
  description = 'A python package that converts pdfdocs into json format',
  author = 'Omoga Omondi',
  author_email = 'omondio254@gmail.com',
  url = 'https://github.com/the-krafty-koder/pdf2json',
  download_url = 'https://github.com/the-krafty-koder/pdf2json/archive/v_02.tar.gz',
  keywords = ['algolia', 'pdf', 'json'],
  install_requires=[
          'beautifulsoup4',
          'PyPDF2',
          'algoliasearch',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
