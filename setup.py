from setuptools import setup

version = '0.5.7'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('TODO.rst').read(),
    open('CREDITS.rst').read(),
    open('CHANGES.rst').read(),
    ])

install_requires = [
    'Django',
    'django-extensions',
    'django-nose',
    'django-load',
    'lizard-ui >= 3.0',
    'lizard-map >= 1.71',
    'lizard_area',
    'lizard_measure',
    'lizard_security',
    'lizard_workspace',
    'pkginfo',
    'djangorestframework',
    ],

tests_require = [
    ]

setup(name='lizard-annotation',
      version=version,
      description="Manages annotations of various objects.",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Programming Language :: Python',
                   'Framework :: Django',
                   ],
      keywords=[],
      author='alexandr seleznev',
      author_email='alexandr.seleznev@nelen-schuurmans.nl',
      url='',
      license='GPL',
      packages=['lizard_annotation'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require = {'test': tests_require},
      entry_points={
          'console_scripts': [
          ]},
      )
