from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    LONG_DESCRIPTION = "\n" + fh.read()
with open(os.path.join(here, "LICENSE"), encoding="utf-8") as fh:
    LICENSE = "\n" + fh.read()



setup(
    name='im2dhist',
    version='0.0.1',
    author="mamdasn s",
    author_email="<mamdassn@gmail.com>",
    url='https://github.com/Mamdasn/im2dhist',
    description='This small piece of code is intended to help researchers, especially those in field of image processing, to easily calculate two dimensional histogram of a given image.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="markdown",
    license=LICENSE,
    packages=find_packages(),
    install_requires=[
        "numpy ~= 1.18.4", 
        "tqdm ~= 4.51.0",
        ],
    keywords=['python', 'histogram', 'imhist', '2dhist', 'hist2d'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Researchers",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ]
)