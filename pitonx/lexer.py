"""
PitonX Lexer (Tokenizer)
Converts PitonX source code into tokens
"""

import re
from pitonx.keywords import KEYWORDS
from pitonx.errors import LexerError


class Token:
    """Represents a single token"""
    def __init__(self, type_, value, line=1, column=1):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, {self.value!r}, {self.line}:{self.column})"


class Lexer:
    """Lexical analyzer for PitonX"""

    TOKEN_SPECS = [
        ('KOMENTAR', (r'#.*',)),
        ('DESIMAL', (r'\d+\.\d+',)),
        ('BILANGAN', (r'\d+',)),
        ('TEKS', (r'"(?:\\.|[^"])*"', r"'(?:\\.|[^'])*'", r'`(?:\\.|[^`])*`')),
        ('IDENTIFIER', (r'[a-zA-Z_][a-zA-Z0-9_]*',)),
        ('OPERATOR_PERBANDINGAN', (r'(==|!=|<=|>=|<|>)',)),
        ('OPERATOR_ARITMATIKA', (r'(\+|-|\*|/|//|%|\*\*)',)),
        ('OPERATOR_PENUGASAN', (r'(\+=|-=|\*=|/=|//=|%=|\*\*=|=)',)),
        ('OPERATOR_LOGIKA', (r'(&&|\|\||!)',)),
        ('TITIK_KOMA', (r';',)),
        ('TITIK_DUA', (r':',)),
        ('KOMA', (r',',)),
        ('TITIK', (r'\.',)),
        ('TANDA_KURUNG_BUKA', (r'\(',)),
        ('TANDA_KURUNG_TUTUP', (r'\)',)),
        ('KURUNG_KOTAK_BUKA', (r'\[',)),
        ('KURUNG_KOTAK_TUTUP', (r'\]',)),
        ('KURUNG_KURAWAL_BUKA', (r'\{',)),
        ('KURUNG_KURAWAL_TUTUP', (r'\}',)),
        ('PANAH', (r'->',)),
        ('WHITESPACE', (r'[ \t]+',)),
        ('NEWLINE', (r'\n',)),
        ('INDENT', (r'^[ \t]+',)),
    ]

    def __init__(self, source):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens = []
        self.indent_stack = [0]
        self._tokenize()

    def _tokenize(self):
        """Main tokenization method"""
        lines = self.source.split('\n')
        current_indent = 0
        prev_indent = 0

        for line_num, line in enumerate(lines, 1):
            # Skip empty lines and comments
            if not line.strip() or line.strip().startswith('#'):
                continue

            # Calculate indentation
            indent_match = re.match(r'^[ \t]*', line)
            current_indent = len(indent_match.group()) if indent_match else 0

            # Handle indentation changes
            if current_indent > prev_indent:
                self.tokens.append(Token('INDENT', current_indent, line_num, 1))
            elif current_indent < prev_indent:
                self.tokens.append(Token('DEDENT', prev_indent, line_num, 1))

            prev_indent = current_indent
            self._tokenize_line(line.strip(), line_num)

        # Add EOF token
        self.tokens.append(Token('EOF', '', len(lines), 1))

    def _tokenize_line(self, line, line_num):
        """Tokenize a single line"""
        col = 1
        i = 0

        while i < len(line):
            # Skip whitespace
            if line[i] in ' \t':
                i += 1
                col += 1
                continue

            # String literals
            if line[i] in '"\'\'`':
                quote = line[i]
                end = i + 1
                while end < len(line):
                    if line[end] == quote and line[end-1] != '\\':
                        break
                    end += 1
                if end >= len(line):
                    raise LexerError("String tidak ditutup", line_num, col)
                token_value = line[i:end+1]
                self.tokens.append(Token('TEKS', token_value, line_num, col))
                i = end + 1
                col += len(token_value)
                continue

            # Numbers
            if line[i].isdigit():
                j = i
                while j < len(line) and line[j].isdigit():
                    j += 1
                if j < len(line) and line[j] == '.':
                    j += 1
                    while j < len(line) and line[j].isdigit():
                        j += 1
                    token_value = line[i:j]
                    self.tokens.append(Token('DESIMAL', token_value, line_num, col))
                else:
                    token_value = line[i:j]
                    self.tokens.append(Token('BILANGAN', token_value, line_num, col))
                col += j - i
                i = j
                continue

            # Identifiers and keywords
            if line[i].isalpha() or line[i] == '_':
                j = i
                while j < len(line) and (line[j].isalnum() or line[j] == '_'):
                    j += 1
                token_value = line[i:j]
                if token_value in KEYWORDS:
                    self.tokens.append(Token('KATA_KUNCI', token_value, line_num, col))
                else:
                    self.tokens.append(Token('IDENTIFIER', token_value, line_num, col))
                col += j - i
                i = j
                continue

            # Operators and punctuation
            if line[i:i+2] == '->':
                self.tokens.append(Token('PANAH', '->', line_num, col))
                i += 2
                col += 2
            elif line[i:i+2] == '==':
                self.tokens.append(Token('OPERATOR_PERBANDINGAN', '==', line_num, col))
                i += 2
                col += 2
            elif line[i:i+2] == '!=':
                self.tokens.append(Token('OPERATOR_PERBANDINGAN', '!=', line_num, col))
                i += 2
                col += 2
            elif line[i:i+2] == '<=':
                self.tokens.append(Token('OPERATOR_PERBANDINGAN', '<=', line_num, col))
                i += 2
                col += 2
            elif line[i:i+2] == '>=':
                self.tokens.append(Token('OPERATOR_PERBANDINGAN', '>=', line_num, col))
                i += 2
                col += 2
            elif line[i:i+3] == '//': 
                self.tokens.append(Token('OPERATOR_ARITMATIKA', '//', line_num, col))
                i += 2
                col += 2
            elif line[i:i+2] == '**':
                self.tokens.append(Token('OPERATOR_ARITMATIKA', '**', line_num, col))
                i += 2
                col += 2
            elif line[i:i+2] == '+=':
                self.tokens.append(Token('OPERATOR_PENUGASAN', '+=', line_num, col))
                i += 2
                col += 2
            elif line[i:i+2] == '-=':
                self.tokens.append(Token('OPERATOR_PENUGASAN', '-=', line_num, col))
                i += 2
                col += 2
            elif line[i:i+2] == '*=':
                self.tokens.append(Token('OPERATOR_PENUGASAN', '*=', line_num, col))
                i += 2
                col += 2
            elif line[i:i+2] == '/=':
                self.tokens.append(Token('OPERATOR_PENUGASAN', '/=', line_num, col))
                i += 2
                col += 2
            elif line[i:i+3] == '//=':
                self.tokens.append(Token('OPERATOR_PENUGASAN', '//=', line_num, col))
                i += 3
                col += 3
            elif line[i:i+2] == '%=':
                self.tokens.append(Token('OPERATOR_PENUGASAN', '%=', line_num, col))
                i += 2
                col += 2
            elif line[i:i+3] == '**=':
                self.tokens.append(Token('OPERATOR_PENUGASAN', '**=', line_num, col))
                i += 3
                col += 3
            elif line[i] == '=':
                self.tokens.append(Token('OPERATOR_PENUGASAN', '=', line_num, col))
                i += 1
                col += 1
            elif line[i] in '+-*/%':
                self.tokens.append(Token('OPERATOR_ARITMATIKA', line[i], line_num, col))
                i += 1
                col += 1
            elif line[i] in '<>':
                self.tokens.append(Token('OPERATOR_PERBANDINGAN', line[i], line_num, col))
                i += 1
                col += 1
            elif line[i] == '(':
                self.tokens.append(Token('TANDA_KURUNG_BUKA', '(', line_num, col))
                i += 1
                col += 1
            elif line[i] == ')':
                self.tokens.append(Token('TANDA_KURUNG_TUTUP', ')', line_num, col))
                i += 1
                col += 1
            elif line[i] == '[':
                self.tokens.append(Token('KURUNG_KOTAK_BUKA', '[', line_num, col))
                i += 1
                col += 1
            elif line[i] == ']':
                self.tokens.append(Token('KURUNG_KOTAK_TUTUP', ']', line_num, col))
                i += 1
                col += 1
            elif line[i] == '{':
                self.tokens.append(Token('KURUNG_KURAWAL_BUKA', '{', line_num, col))
                i += 1
                col += 1
            elif line[i] == '}':
                self.tokens.append(Token('KURUNG_KURAWAL_TUTUP', '}', line_num, col))
                i += 1
                col += 1
            elif line[i] == ':':
                self.tokens.append(Token('TITIK_DUA', ':', line_num, col))
                i += 1
                col += 1
            elif line[i] == ';':
                self.tokens.append(Token('TITIK_KOMA', ';', line_num, col))
                i += 1
                col += 1
            elif line[i] == ',':
                self.tokens.append(Token('KOMA', ',', line_num, col))
                i += 1
                col += 1
            elif line[i] == '.':
                self.tokens.append(Token('TITIK', '.', line_num, col))
                i += 1
                col += 1
            else:
                raise LexerError(f"Karakter tidak dikenali: {line[i]!r}", line_num, col)

        # Add newline token
        self.tokens.append(Token('NEWLINE', '\n', line_num, col))

    def get_tokens(self):
        """Return all tokens"""
        return self.tokens
