from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='stellarblue-parsing-models', 
    version='1.0.0',
    author='George Tsoumalis',
    author_email='gtsoumalis@stellarblue.eu',
    description='A Python package for parsing models',
    url='https://github.com/Power-Systems-Lab-AUTH/python-parsing-models', 
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
