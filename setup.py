import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="xml_stream",
    version="0.0.8",
    description="""
    A simple XML file and string reader to read big XML files and strings using iterators
    with optional conversion to dict
    """,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sopherapps/xml_stream",
    author="Martin Ahindura",
    author_email="team.sopherapps@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(exclude=("test",)),
    include_package_data=True,
    install_requires=[],
    entry_points={
    },
)