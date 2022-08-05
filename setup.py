from setuptools import setup, find_packages
from pathlib import Path

root_dir = Path(__file__).parent.expanduser().resolve()
"""root directory for project"""

setup(
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
