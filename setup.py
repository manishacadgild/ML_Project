
<<<<<<< HEAD
from setuptools import setup,find_packages
from typing import List

PROJECT_NAME='housing-predictor'
VERSION='0.0.4'
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
=======
from setuptools import setup
from typing import List

def get_requirements_list()->List[str]:
    pass

PROJECT_NAME='housing-predictor'
VERSION='0.0.1'
AUTHOR='Manish Jha'
DESCRIPTION='This is my first machine learning project'
PACKAGES=['housing']
>>>>>>> 36e7b66 (component files added)

setup( 
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
<<<<<<< HEAD
    packages=find_packages(),
=======
    packages=PACKAGES,
>>>>>>> 36e7b66 (component files added)
    install_requires=get_requirements_list()
    )