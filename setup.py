from setuptools import setup, find_packages
from pathlib import Path
import os
import re
import io


def parse_requirements_file(filename):
    with open(filename, encoding="utf-8") as fid:
        requires = [line.strip() for line in fid.readlines() if line]
    return requires


root_dir = Path(__file__).parent.resolve()
"""root directory for project"""

# with (root_dir / 'README.md').open('r', encoding='utf-8') as readme:
#     long_description = readme.read()

# dynamic setup values
# see setup.cfg for static values


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


version = find_version("src", "LancasterAQ", "__init__.py")
readme = open("README.md").read()

setup(
    name="lancasteraq",
    version=version,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    license="LICENSE",
    description="Lancaster air quality data.",
    long_description=readme,
    long_description_content_type="text/markdown",
)
