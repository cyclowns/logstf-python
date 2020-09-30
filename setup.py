import setuptools

with open("README.md", "r") as fh:
    long_desc = fh.read()

setuptools.setup(
    name="logstf-python",
    version="0.1.0",
    author="cyclowns",
    author_email="cyclowns@protonmail.ch",
    description="Python wrapper around the Logs.tf data, search & upload APIs",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/cyclowns/logstf-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries"
    ]
)
