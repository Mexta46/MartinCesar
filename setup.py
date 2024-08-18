from setuptools import setup, find_packages

setup(
    name='MartinCesar',
    version='0.1.2',    
    packages=find_packages(), 
    author='Martin',
    author_email='tu.email@example.com',
    description='Descripción de lo que hace tu librería',
    long_description=open('Readme.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
