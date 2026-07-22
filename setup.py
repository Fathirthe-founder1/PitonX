from setuptools import setup, find_packages

setup(
    name='pitonx',
    version='8.1.0',
    packages=find_packages(),
    entry_points={'console_scripts': ['pitonx = pitonx.repl:main']},
    description='Bahasa Pemrograman Indonesia berbasis Python',
    author='Fathirthe-founder1',
    url='https://github.com/Fathirthe-founder1/PitonX',
    python_requires='>=3.8',
)
