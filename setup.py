import setuptools
import sys

try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    sys.exit("""Could not import Cython, which is required to build benepar extension modules.
Please install cython and numpy prior to installing benepar.""")

try:
    import numpy as np
except ImportError:
    sys.exit("""Could not import numpy, which is required to build the extension modules.
Please install cython and numpy prior to installing benepar.""")

with open("README.md", "r") as f:
    long_description = f.read()

extensions = cythonize("benepar/*.pyx")
for ext_module in extensions:
    ext_module.include_dirs.append(np.get_include())

setuptools.setup(
    name="dc_parser",
    version="0.0.1",
    author="Li Wang",
    author_email="li@liwang.info",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liwangd/disfluency-constituency-parser",
    packages=setuptools.find_packages(),
    package_data={'': ['*.pyx']},
    ext_modules = cythonize(extensions),
    classifiers=(
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ),
    setup_requires = ["cython", "numpy"],
    install_requires = ["cython", "numpy", "nltk>=3.2"],
)
