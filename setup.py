from setuptools import setup, find_packages

setup(name='Facebank',
      description='Facebank',
      long_description='Facebank',
      packages=find_packages(exclude=["*tests*"]),
      package_data={'': ['*.yaml']},
      version='1.0.0',
      install_requires=[
      ],
      extras_require={
          'dev': [
              'pycodestyle>=2.6.*',
              'pytest>=6.2.*',
              'pytest-cov>=2.10.*',
              'requests-mock>=1.8.*',
              'pytest-mock>=3.4.*',
              'pytest-sugar>=0.9.4',
              'pytest-factoryboy==2.0.*',
              'pytest-lazy-fixture>=0.6.*',
              'Faker==8.1.3',
              'flake8>=3.8.3',
              'freezegun==1.*'
          ],
      }
      )
