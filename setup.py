import setuptools
import sys

from Cython.Build import cythonize
USE_CYTHON = True

# try:
#     from Cython.Build import cythonize
#     USE_CYTHON = True
# except ImportError:
#     sys.exit("Could not import Cython, which is required to build extension modules.")

try:
    import numpy as np
except ImportError:
    sys.exit("Could not import numpy, which is required to build the extension modules.")

extensions = cythonize("dc_parser/*.pyx")
for ext_module in extensions:
    ext_module.include_dirs.append(np.get_include())


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="disfluency-constituency-parser",
    version="0.0.11",
    author="Li Wang",
    author_email="li@liwang.info",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liwangd/disfluency-constituency-parser",
    packages=setuptools.find_packages(),
    ext_modules = cythonize(extensions),
    classifiers=(
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ),
    setup_requires=["cython", "numpy"],
    install_requires=["cython", "numpy", "nltk>=3.2"],
)
