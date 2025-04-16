from setuptools import setup, find_packages

NAME = 'pysungrow'
VERSION = '0.0.1'

AUTHOR = 'Christopher F. Moran'
EMAIL = 'noreply@gmail.com'
DESCRIPTION = 'SunGrow iSolarCloud Interface'
LICENSE = 'BSD'
LONG_DESCRIPTION = 'Basic interface into the SunGrow iSolarCloud Environment'

setup(
    name = NAME,
    version = VERSION,
    author = AUTHOR,
    author_email= EMAIL,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'logging'],
    keywords=['python', 'sungrow', 'isolarcloud', 'solar', 'cloud'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ]
)
