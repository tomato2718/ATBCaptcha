from setuptools import setup, find_namespace_packages

from atbcaptcha import __about__

with open('./atbcaptcha/requirements.txt', 'r') as file:
    req = file.readlines()

setup(
    name = __about__.__project__,
    version = __about__.__version__,
    author = __about__.__author__,
    maintainer = __about__.__maintainer__,
    description = __about__.__summary__,
    url = '', 
    packages = find_namespace_packages(include=['atbcaptcha*']),
    include_package_data = True,
    install_requires=req,
)