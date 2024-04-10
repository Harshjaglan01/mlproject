from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.read().splitlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != HYPEN_E_DOT]
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Krish',
    author_email='krishnaik06@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
