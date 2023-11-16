from setuptools import setup, find_packages

setup(
    name='stellarblue-parsing-models', 
    version='1.0.0',
    author='George Tsoumalis',
    author_email='gtsoumalis@stellarblue.eu',
    description='A Python package for parsing models',
    url='https://github.com/Power-Systems-Lab-AUTH/python-parsing-models', 
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'fastapi==0.104.1',
        'pydantic==2.5.1',
        'typing-extensions==4.8.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
