from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


setup(
    name='im2dhist',
    version='0.0.2.2',
    author="mamdasn s",
    author_email="<mamdassn@gmail.com>",
    url="https://github.com/Mamdasn/im2dhist",
    description='This small piece of code is intended to help researchers, especially those in field of image processing, to easily calculate two dimensional histogram of a given image.',
    long_description=long_description,
    long_description_content_type = "text/markdown",
    package_dir={'': 'src'},
    py_modules=["im2dhist"],
    install_requires=[
        "numpy", 
        "tqdm",
        ],
    keywords=['python', 'histogram', 'imhist', '2dhist', 'hist2d'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ]
)