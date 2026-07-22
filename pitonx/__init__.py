"""
PitonX - A Python Programming Language with Indonesian Keywords
Version: 1.0.0
Author: Fathirthe-founder1
Repository: https://github.com/Fathirthe-founder1/PitonX
"""

__version__ = "1.0.0"
__author__ = "Fathirthe-founder1"
__description__ = "A library, package, modified Python with Indonesian keywords"

from pitonx.core import run, transpile
from pitonx.lexer import Lexer
from pitonx.parser import Parser
from pitonx.transpiler import Transpiler
from pitonx.errors import PitonXError, LexerError, ParserError, TranspilerError

__all__ = [
    "run",
    "transpile",
    "Lexer",
    "Parser",
    "Transpiler",
    "PitonXError",
    "LexerError",
    "ParserError",
    "TranspilerError",
    "__version__",
    "__author__",
    "__description__",
]
