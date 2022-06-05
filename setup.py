from setuptools import setup, find_packages
import io,os

def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("project_name", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]

setup(name='YouTube-Indexer',
version='1.0.0',
description='Dependency for YAS',
author='Anand, Xosrov',
url = 'https://github.com/DnanaDev/YouTube-Indexer',
long_description=read("README.md"),
long_description_content_type="text/markdown",
packages=find_packages(exclude=["tests"]), #"['yas', 'yas.dependencies', 'yas.src', 'yas.dependencies.youtube_collector']
install_requires =read_requirements("requirements.txt"),
license='MIT',
#extras_require={"test": read_requirements("requirements-test.txt")},
)



