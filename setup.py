import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cvr-lookup",
    version="0.0.1",
    author="Heini Leander Ovason",
    author_email="heini.ovason@gmail.com",
    description="Integration with The Danish Business Authority Web API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/magenta-aps/cvr-lookup",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License Version 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)