from setuptools import setup

with open('README.rst') as README:
    long_description = README.read()
    long_description = long_description[long_description.index('Description'):]

setup(name='infinite',
      version='0.1',
      description='itertools operations on infinite generators.',
      long_description=long_description,
      url='http://github.com/enricobacis/infinite',
      author='Enrico Bacis',
      author_email='enrico.bacis@gmail.com',
      license='MIT',
      packages=['infinite'],
      keywords='infinite itertools product generators infinity'
)
