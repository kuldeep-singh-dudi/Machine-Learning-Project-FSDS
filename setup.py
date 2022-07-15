from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "housing-price-prediction"
VERSION="0.0.3"
AUTHOR="Kuldeep Singh Dudi"
DESCRIPTION="prediction of housing prices based on different factors"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()-> List[str]:
    with open(REQUIREMENT_FILE_NAME)as requirements_file:
        return requirements_file.readline()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)
