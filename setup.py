from setuptools import setup, find_packages

setup(
    name="matebotpy", 
    version="0.1.0",
    description="Python API Wrapper for Matebot.",
    author="Máté Mészáros",
    author_email="meszmatew@gmail.com",
    url="https://github.com/meszmate/matebotpy",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)