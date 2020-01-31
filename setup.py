import setuptools

with open("README.md") as f:
    long_description = f.read()

with open('VERSION') as f:
    version = f.read()

setuptools.setup(
    name="srtfix",
    version=version,
    author="Gilad Kutiel",
    author_email="gilad.kutiel@gmail.com",
    description="A tool to rename srt files",
    long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/srtfix/srtfix",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'srtfix=srtfix.srtfix:main'
        ],
    }
)
