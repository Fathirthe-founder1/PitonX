"""
PitonX Error Classes
Custom exceptions for PitonX language
"""


class PitonXError(Exception):
    """Base exception for all PitonX errors"""
    pass


class LexerError(PitonXError):
    """Exception raised during lexical analysis"""
    def __init__(self, message, line=None, column=None):
        self.message = message
        self.line = line
        self.column = column
        if line is not None and column is not None:
            super().__init__(f"Kesalahan Lexer pada baris {line}, kolom {column}: {message}")
        elif line is not None:
            super().__init__(f"Kesalahan Lexer pada baris {line}: {message}")
        else:
            super().__init__(f"Kesalahan Lexer: {message}")


class ParserError(PitonXError):
    """Exception raised during parsing"""
    def __init__(self, message, line=None, token=None):
        self.message = message
        self.line = line
        self.token = token
        if line is not None:
            super().__init__(f"Kesalahan Parser pada baris {line}: {message}")
        else:
            super().__init__(f"Kesalahan Parser: {message}")


class TranspilerError(PitonXError):
    """Exception raised during transpilation"""
    def __init__(self, message, line=None):
        self.message = message
        self.line = line
        if line is not None:
            super().__init__(f"Kesalahan Transpiler pada baris {line}: {message}")
        else:
            super().__init__(f"Kesalahan Transpiler: {message}")
