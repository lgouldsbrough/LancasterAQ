from setuptools import setup, find_packages
from pathlib import Path

root_dir = Path(__file__).parent.resolve()
"""root directory for project"""

# with (root_dir / 'README.md').open('r', encoding='utf-8') as readme:
#     long_description = readme.read()

# dynamic setup values
# see setup.cfg for static values
setup(
        package_dir={'': 'src'},
        packages=find_packages(where='src'),
)
