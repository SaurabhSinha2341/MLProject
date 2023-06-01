from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    rerquirements=[]
    with open(file_path) as file_obj:
        rerquirements=file_obj.readlines()
        rerquirements=[req.replace("\n", "") for req in rerquirements]
        if HYPEN_E_DOT in rerquirements:
            rerquirements.remove(HYPEN_E_DOT)
    return rerquirements

setup(
    name='mlProject',
    version='0.0.1',
    author='Saurabh',
    author_email='harsh.sinha.3682@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)