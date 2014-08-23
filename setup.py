from setuptools import setup

setup(
    name='beetle_sass',
    author='Jeppe Toustrup',
    author_email='jeppe@tenzer.dk',
    packages=[
        'beetle_sass'
    ],
    install_requires=[
        'libsass==0.5.0',
    ],
)
