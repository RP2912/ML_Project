from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements from the given file.
    """
    HYPEN_E_DOT = '-e .'
    requirements = []
    
    # Reading the requirements from the file
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters
        requirements = [req.replace("\n", "") for req in requirements]
    
    # Remove '-e .' if present in the requirements list
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Rinkey',
    author_email='rinkeypal2419@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
