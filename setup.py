from setuptools import find_packages,setup
from typing import List


def get_requirements()->list[str]:
  requirments_list=list[str]=[]
  return requirments_list
   


setup(
    name='sensor',
    version="0.0.1",
    author="shreshth",
    author_email="goswamishreshth100@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)