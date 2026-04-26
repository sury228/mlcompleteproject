from setuptools import setup, find_packages 
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    ''''
    This function will return the list of requirements
    '''

    requirments = []
    with open('requirements.txt') as file_obj:
        requirments = file_obj.readlines()
        [req.replace('\n','') for req in requirments]
        
        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)



setup(
name='mlproject',
version='0.0.1',
author='suryansh',
author_email='cloudsuryansh9@gmail.com',
pakages=find_packages(),
install_requires=get_requirements('requirements.txt')
)