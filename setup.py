"""
Setup configuration for PitonX package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pitonx",
    version="8.0.7",
    author="Jameson AlFathir Void",
    description="A lightweight Python-based transpiler with Indonesian syntax",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fathirthe-founder1/PitonX",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Education",
    ],
    python_requires=">=3.7",
    keywords="transpiler python indonesian syntax interpreter",
    project_urls={
        "Bug Reports": "https://github.com/Fathirthe-founder1/PitonX/issues",
        "Source": "https://github.com/Fathirthe-founder1/PitonX",
    },
    entry_points={
        "console_scripts": [
            "pitonx=pitonx.cli:main",
            "piton=pitonx.repl:run_repl",
        ],
    },
)
