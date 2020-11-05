import setuptools
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="2048-py",
    version="0.1.5",
    author="Anthony Wang",
    author_email="ta180m@gmail.com",
    description="2048 written in Python by the Ladue High School Computer Science Club",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ta180m/2048",
    py_modules=[ "main" ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        'Topic :: Games/Entertainment :: Puzzle Games',
    ],
    entry_points={
        'console_scripts': [
            '2048-py = main:main',
        ],
    },
    install_requires=[ 'termcolor' ]
)
