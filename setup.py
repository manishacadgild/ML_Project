from setuptools import setup,find_packages
from typing import List

PROJECT_NAME='housing-predictor'
VERSION='0.0.6'
AUTHOR='Manish Jha'
DESCRIPTION='This is my first machine learning project'
PACKAGES=['housing']
REQUIREMENT_FILE_NAME='requirements.txt'
HYPHEN_E_DOT = "-e ."

def get_requirements_list()->List[str]:
   with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list
"""
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
"""

setup( 
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
    )