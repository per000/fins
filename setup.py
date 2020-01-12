import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fins",
    version="1.0",
    author="Per",
    author_email="perolaf@gmail.com",
    description="Omron FINS memory read",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/per000/fins",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
