"""
Lexer Module - Tokenizes PitonX source code
"""

import re
from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Optional

class TokenType(Enum):
    """Token types for PitonX lexer"""
    # Literals
    NUMBER = auto()
    STRING = auto()
    IDENTIFIER = auto()
    
    # Keywords
    KEYWORD = auto()
    
    # Operators
    OPERATOR = auto()
    COMPARISON = auto()
    ASSIGNMENT = auto()
    
    # Delimiters
    LPAREN = auto()
    RPAREN = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    LBRACE = auto()
    RBRACE = auto()
    COLON = auto()
    COMMA = auto()
    DOT = auto()
    ARROW = auto()
    
    # Special
    NEWLINE = auto()
    INDENT = auto()
    DEDENT = auto()
    EOF = auto()
    COMMENT = auto()

@dataclass
class Token:
    """Represents a single token"""
    type: TokenType
    value: str
    line: int
    column: int

class Lexer:
    """Tokenizes PitonX source code"""
    
    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
        self.indent_stack = [0]
        
    def tokenize(self) -> List[Token]:
        """Tokenize the entire source code"""
        while self.position < len(self.source):
            self._skip_whitespace_except_newline()
            
            if self.position >= len(self.source):
                break
                
            char = self.source[self.position]
            
            # Handle comments
            if char == '#':
                self._skip_comment()
                continue
            
            # Handle newlines
            if char == '\n':
                self.tokens.append(Token(TokenType.NEWLINE, '\n', self.line, self.column))
                self._advance()
                self._handle_indentation()
                continue
            
            # Handle strings
            if char in ('"', "'"):
                self.tokens.append(self._read_string())
                continue
            
            # Handle numbers
            if char.isdigit():
                self.tokens.append(self._read_number())
                continue
            
            # Handle operators and delimiters
            if self._try_two_char_operator():
                continue
            
            if char in '()[]{}:,.<>!=+-*/%&|^':
                self.tokens.append(self._read_operator())
                continue
            
            # Handle identifiers and keywords
            if char.isalpha() or char == '_':
                self.tokens.append(self._read_identifier())
                continue
            
            # Skip unknown characters
            self._advance()
        
        self.tokens.append(Token(TokenType.EOF, '', self.line, self.column))
        return self.tokens
    
    def _advance(self) -> str:
        """Move to next character"""
        if self.position < len(self.source):
            char = self.source[self.position]
            self.position += 1
            if char == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            return char
        return ''
    
    def _peek(self, offset: int = 0) -> str:
        """Look ahead at character without advancing"""
        pos = self.position + offset
        if pos < len(self.source):
            return self.source[pos]
        return ''
    
    def _skip_whitespace_except_newline(self):
        """Skip spaces and tabs but not newlines"""
        while self.position < len(self.source) and self.source[self.position] in (' ', '\t', '\r'):
            self._advance()
    
    def _skip_comment(self):
        """Skip comment until end of line"""
        while self.position < len(self.source) and self.source[self.position] != '\n':
            self._advance()
    
    def _handle_indentation(self):
        """Handle indentation changes"""
        indent_level = 0
        start_pos = self.position
        
        while self.position < len(self.source) and self.source[self.position] in (' ', '\t'):
            if self.source[self.position] == ' ':
                indent_level += 1
            else:
                indent_level += 4
            self._advance()
        
        if self.position < len(self.source) and self.source[self.position] not in ('\n', '#'):
            current_indent = self.indent_stack[-1]
            
            if indent_level > current_indent:
                self.indent_stack.append(indent_level)
                self.tokens.append(Token(TokenType.INDENT, '    ', self.line, self.column))
            elif indent_level < current_indent:
                while self.indent_stack and self.indent_stack[-1] > indent_level:
                    self.indent_stack.pop()
                    self.tokens.append(Token(TokenType.DEDENT, '', self.line, self.column))
    
    def _read_string(self) -> Token:
        """Read string literal"""
        start_line, start_col = self.line, self.column
        quote = self.source[self.position]
        self._advance()
        
        value = ''
        while self.position < len(self.source) and self.source[self.position] != quote:
            if self.source[self.position] == '\\':
                self._advance()
                if self.position < len(self.source):
                    escape_char = self.source[self.position]
                    if escape_char == 'n':
                        value += '\n'
                    elif escape_char == 't':
                        value += '\t'
                    elif escape_char == '\\':
                        value += '\\'
                    else:
                        value += escape_char
                    self._advance()
            else:
                value += self.source[self.position]
                self._advance()
        
        if self.position < len(self.source):
            self._advance()  # closing quote
        
        return Token(TokenType.STRING, value, start_line, start_col)
    
    def _read_number(self) -> Token:
        """Read numeric literal"""
        start_line, start_col = self.line, self.column
        value = ''
        
        while self.position < len(self.source) and (self.source[self.position].isdigit() or self.source[self.position] == '.'):
            value += self.source[self.position]
            self._advance()
        
        return Token(TokenType.NUMBER, value, start_line, start_col)
    
    def _read_identifier(self) -> Token:
        """Read identifier or keyword"""
        start_line, start_col = self.line, self.column
        value = ''
        
        while self.position < len(self.source) and (self.source[self.position].isalnum() or self.source[self.position] == '_'):
            value += self.source[self.position]
            self._advance()
        
        return Token(TokenType.IDENTIFIER, value, start_line, start_col)
    
    def _try_two_char_operator(self) -> bool:
        """Try to match two-character operators"""
        two_char = self.source[self.position:self.position + 2]
        two_char_ops = {'==', '!=', '<=', '>=', '->', '**', '//', '&&', '||', '<<', '>>'}
        
        if two_char in two_char_ops:
            token_type = TokenType.COMPARISON if two_char in {'==', '!=', '<=', '>='} else TokenType.OPERATOR
            self.tokens.append(Token(token_type, two_char, self.line, self.column))
            self._advance()
            self._advance()
            return True
        
        return False
    
    def _read_operator(self) -> Token:
        """Read operator or delimiter"""
        start_line, start_col = self.line, self.column
        char = self.source[self.position]
        self._advance()
        
        if char == '(':
            return Token(TokenType.LPAREN, char, start_line, start_col)
        elif char == ')':
            return Token(TokenType.RPAREN, char, start_line, start_col)
        elif char == '[':
            return Token(TokenType.LBRACKET, char, start_line, start_col)
        elif char == ']':
            return Token(TokenType.RBRACKET, char, start_line, start_col)
        elif char == '{':
            return Token(TokenType.LBRACE, char, start_line, start_col)
        elif char == '}':
            return Token(TokenType.RBRACE, char, start_line, start_col)
        elif char == ':':
            return Token(TokenType.COLON, char, start_line, start_col)
        elif char == ',':
            return Token(TokenType.COMMA, char, start_line, start_col)
        elif char == '.':
            return Token(TokenType.DOT, char, start_line, start_col)
        elif char == '=':
            return Token(TokenType.ASSIGNMENT, char, start_line, start_col)
        else:
            return Token(TokenType.OPERATOR, char, start_line, start_col)
