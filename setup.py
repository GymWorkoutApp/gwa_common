import setuptools
from setuptools import find_packages
import gwa_common


def long_description():
    with open('README.md', encoding='utf8') as f:
        return f.read()


setuptools.setup(
    name='gwa_common.server',
    version=gwa_common.__version__,

    url='https://bitbucket.org/serasaecs/ecs-lib-boleto-python',
    description='Microservice that keep endpoints commons to GWA.',
    long_description=long_description(),
    long_description_content_type="text/markdown",

    author='Guilherme Dalmarco',
    author_email='dalmarco.br@gmail.com',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],

    include_package_data=True,
    zip_safe=False,
    platforms='any',
    packages=find_packages(exclude=['tests*']),
    install_requires=[],
    extras_require={},
)
