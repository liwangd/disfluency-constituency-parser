import setuptools
import sys


def get_requirements(path):
    with open(path, encoding="utf-8") as requirements:
        return [requirement.strip() for requirement in requirements]


install_requires = get_requirements(os.path.join(base_dir, "requirements.txt"))

with open("README.md", "r") as f:
    long_description = f.read()

extensions = cythonize("dc_parser/*.pyx")
for ext_module in extensions:
    ext_module.include_dirs.append(np.get_include())

setuptools.setup(
    name="disfluency-constituency-parser",
    version="0.0.2",
    author="Li Wang",
    author_email="li@liwang.info",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liwangd/disfluency-constituency-parser",
    packages=setuptools.find_packages(),
    package_data={'': ['*.pyx']},
    ext_modules=cythonize(extensions),
    classifiers=(
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ),
    setup_requires=["cython", "numpy"],
    install_requires=install_requires,
)
