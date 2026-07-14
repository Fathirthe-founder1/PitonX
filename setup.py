from setuptools import setup, find_packages

setup(
    name='piton',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'piton = piton.cli:main'
        ]
    },
    description='Bahasa Pemrograman Indonesia berbasis Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Fathirthe-founder1',
    url='https://github.com/Fathirthe-founder1/Piton',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
