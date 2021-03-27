from setuptools import setup, find_packages

version = open('VERSION').read().strip()
license = open('LICENSE').read().strip()

setup(
    name = 'budapp-core-db',
    version = version,
    license = license,
    author = 'Jonathan Rodríguez Alejos',
    author_email = 'jrodriguez.5716@gmail.com',
    url = 'https://github.com/Budapp',
    description = 'Dynamic database core manager',
    long_description = open('README.md').read().strip(),
    packages = find_packages(),
    install_requires=[
        'SQLAlchemy',
    ],
    test_suite = 'tests',
)
