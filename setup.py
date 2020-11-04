import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="2048-py",
    version="0.1.4-2",
    author="Anthony Wang",
    author_email="ta180m@gmail.com",
    description="2048 written in Python by the Ladue High School Computer Science Club",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ta180m/2048",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "termcolor",
    ],
    python_requires='>=3.6',
) 
