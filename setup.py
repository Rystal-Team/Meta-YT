from setuptools import setup, find_packages

setup(
    name="meta_yt",
    version="0.1.1-beta",
    packages=find_packages(),
    author="Rystal-Team",
    author_email="code@rystal.xyz",
    description="A lightweight Python library for fetching YouTube videos\' metadata.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Rystal-Team/Meta-YT",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests",
        "xmltodict",
    ],
)
