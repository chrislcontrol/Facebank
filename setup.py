from setuptools import setup, find_packages

setup(name='User Storage',
      description='User Storage',
      long_description='User Storage',
      packages=find_packages(exclude=["*tests*"]),
      package_data={'': ['*.yaml']},
      version='1.0.0',
      install_requires=[
          'Flask==2.1.3',
          'Flask-Cors==3.0.10',
          'alembic==1.8.1',
          'SQLAlchemy==1.4.39',
          'psycopg2==2.9.3',
          'bcrypt==3.2.2'
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
