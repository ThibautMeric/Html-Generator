from setuptools import setup, find_packages
import html_generator
setup(name = 'html_generator',
      version = html_generator.__version__,
      packages = find_packages(),
      entry_points = {'gui_scripts': ['html-generator = html_generator.htmlgenerator:main',]},
      description='Generate html code for Bootstrap 3 & 4',
      long_description='You can create Panel, Well, Thumbails, Cards, header, footer, paragraph, images define size padding etc',
      author='Thibaut Meric',
      author_email='thibaut.meric@microchip.com',
      url='www.microchip.com/iot/',
      maintainer= 'Iot & HASG Group',
      maintainer_email='xxxxxx@microchip.com',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers'
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                  ],
      platforms=['Operating System :: MacOS :: MacOS X','Operating System :: Microsoft :: Windows'],
      keywords='CSS HTML',
     )
# documentation -> https://packaging.python.org/en/latest/distributing/#setup-args
# classifiers list -> https://pypi.python.org/pypi?%3Aaction=list_classifiers
# Wheel name documentation -> https://www.python.org/dev/peps/pep-0427/
