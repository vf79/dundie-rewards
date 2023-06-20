from setuptools import setup, find_packages
import os

def read(*paths):
    """Read the contents of a text file safely.
    >>> read("project_name", "VERSION")
    '0.1.0'
    >>> read("README.md")
    """
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as reqrmtfile:
        return reqrmtfile.read().strip()


def read_requirements(path):
    """Return a list of requirements from a text file"""
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('#', 'git+', '"', '-'))
    ]

setup(
    name="dundie",
    version="0.1.0",
    description="Reward Point System for Dunder Mifflin",
    long_description=read("README.md"),
    long_description_content_type = "text/markdown",
    author="Valmir Franca",
    packages=find_packages(),
    entry_points={
        "console_scripts":[
            "dundie = dundie.__main__:main"
        ]
    },
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "dev":read_requirements("requirements.dev.txt"),
        "test":read_requirements("requirements.test.txt"),
    },
)
