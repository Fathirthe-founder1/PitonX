from setuptools import setup, find_packages

setup(
    name='pitonx',
    version='1.0.4',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pitonx = pitonx.cli:main'
        ]
    },
    description='Bahasa Pemrograman Indonesia berbasis Python',
    author='Fathirthe-founder1',
    url='https://github.com/Fathirthe-founder1/PitonX',
    python_requires='>=3.6',
)
