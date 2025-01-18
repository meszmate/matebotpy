from setuptools import setup, find_packages

setup(
    name="matebotpy", 
    version="0.0.6",
    description="Python API Wrapper for Matebot.",
    author="Máté Mészáros",
    author_email="meszmatew@gmail.com",
    url="https://github.com/meszmate/matebotpy",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
    python_requires='>=3.8',
)