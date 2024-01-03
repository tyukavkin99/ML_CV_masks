from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    function get the list of required packages
    '''
    E_DOT = '-e .'
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [i.replace('\n','') for i in requirements]

        if E_DOT in requirements:
            requirements.remove(E_DOT)
    
    return requirements



setup(
    name = 'ML_CV_masks',
    version='0.0.1',
    author='ST',
    packages = find_packages(),
    install_requirements = get_requirements('requirements.txt')
)