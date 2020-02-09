from setuptools import setup, find_packages

setup(name='pesis',
      version='0.1',
      description='A game',
      author='Fake Name',
      author_email='fake@address.com',
      url='https://www.python.org/',
      packages=find_packages()
      python_requires='3.7',
      entry_points={
          'console_scripts': [
              'pesis = pesis.__main__:main'
          ]
     )
