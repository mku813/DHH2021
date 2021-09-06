from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup

# with open("requirements.txt") as f:
#     required = f.read().splitlines()

import pathlib
import pkg_resources

with pathlib.Path("requirements.txt").open() as requirements_txt:
    install_requires = [str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt)]
    
setup(
    name="DHH",
    version="0.1",
    python_requires=">=3.8",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="srlee,kumin",
    install_requires=install_requires,
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
)
