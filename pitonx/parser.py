"""
Parser Module - Builds Abstract Syntax Tree from tokens
"""

from dataclasses import dataclass
from typing import List, Optional, Union
from pitonx.lexer import Token, TokenType, Lexer

# AST Node types
@dataclass
class ASTNode:
    """Base class for AST nodes"""
    pass

@dataclass
class Program(ASTNode):
    statements: List[ASTNode]

@dataclass
class BinaryOp(ASTNode):
    left: ASTNode
    operator: str
    right: ASTNode

@dataclass
class UnaryOp(ASTNode):
    operator: str
    operand: ASTNode

@dataclass
class Call(ASTNode):
    func: ASTNode
    args: List[ASTNode]

@dataclass
class Identifier(ASTNode):
    name: str

@dataclass
class Number(ASTNode):
    value: Union[int, float]

@dataclass
class String(ASTNode):
    value: str

@dataclass
class Assignment(ASTNode):
    target: str
    value: ASTNode

@dataclass
class IfStatement(ASTNode):
    condition: ASTNode
    body: List[ASTNode]
    elif_parts: List[tuple]
    else_body: Optional[List[ASTNode]]

@dataclass
class WhileLoop(ASTNode):
    condition: ASTNode
    body: List[ASTNode]

@dataclass
class ForLoop(ASTNode):
    target: str
    iterable: ASTNode
    body: List[ASTNode]

@dataclass
class FunctionDef(ASTNode):
    name: str
    params: List[str]
    body: List[ASTNode]

@dataclass
class ClassDef(ASTNode):
    name: str
    body: List[ASTNode]

@dataclass
class ReturnStatement(ASTNode):
    value: Optional[ASTNode]

@dataclass
class ImportStatement(ASTNode):
    module: str
    alias: Optional[str]

class Parser:
    """Parses tokens into an AST"""
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.position = 0
    
    def parse(self) -> Program:
        """Parse tokens into a program AST"""
        statements = []
        
        while not self._is_at_end():
            if self._check(TokenType.NEWLINE):
                self._advance()
                continue
            
            stmt = self._parse_statement()
            if stmt:
                statements.append(stmt)
        
        return Program(statements)
    
    def _parse_statement(self) -> Optional[ASTNode]:
        """Parse a single statement"""
        if self._check(TokenType.EOF):
            return None
        
        # Skip newlines
        while self._check(TokenType.NEWLINE):
            self._advance()
        
        if self._check(TokenType.EOF):
            return None
        
        # Try to parse different statement types
        if self._check_keyword('jika'):
            return self._parse_if_statement()
        elif self._check_keyword('selagi'):
            return self._parse_while_loop()
        elif self._check_keyword('ulangi'):
            return self._parse_for_loop()
        elif self._check_keyword('buat'):
            return self._parse_function_def()
        elif self._check_keyword('wadah'):
            return self._parse_class_def()
        elif self._check_keyword('kembalikan'):
            return self._parse_return_statement()
        elif self._check_keyword('impor'):
            return self._parse_import_statement()
        else:
            return self._parse_expression_statement()
    
    def _parse_if_statement(self) -> IfStatement:
        """Parse if statement"""
        self._consume_keyword('jika')
        condition = self._parse_expression()
        self._consume(TokenType.COLON)
        self._skip_newlines()
        
        body = self._parse_block()
        elif_parts = []
        else_body = None
        
        while self._check_keyword('jikalau'):
            self._consume_keyword('jikalau')
            elif_condition = self._parse_expression()
            self._consume(TokenType.COLON)
            self._skip_newlines()
            elif_body = self._parse_block()
            elif_parts.append((elif_condition, elif_body))
        
        if self._check_keyword('selain'):
            self._consume_keyword('selain')
            self._consume(TokenType.COLON)
            self._skip_newlines()
            else_body = self._parse_block()
        
        return IfStatement(condition, body, elif_parts, else_body)
    
    def _parse_while_loop(self) -> WhileLoop:
        """Parse while loop"""
        self._consume_keyword('selagi')
        condition = self._parse_expression()
        self._consume(TokenType.COLON)
        self._skip_newlines()
        body = self._parse_block()
        return WhileLoop(condition, body)
    
    def _parse_for_loop(self) -> ForLoop:
        """Parse for loop"""
        self._consume_keyword('ulangi')
        target = self._advance().value
        self._consume_keyword('dalam')
        iterable = self._parse_expression()
        self._consume(TokenType.COLON)
        self._skip_newlines()
        body = self._parse_block()
        return ForLoop(target, iterable, body)
    
    def _parse_function_def(self) -> FunctionDef:
        """Parse function definition"""
        self._consume_keyword('buat')
        name = self._advance().value
        self._consume(TokenType.LPAREN)
        
        params = []
        if not self._check(TokenType.RPAREN):
            params.append(self._advance().value)
            while self._check(TokenType.COMMA):
                self._advance()
                params.append(self._advance().value)
        
        self._consume(TokenType.RPAREN)
        self._consume(TokenType.COLON)
        self._skip_newlines()
        body = self._parse_block()
        
        return FunctionDef(name, params, body)
    
    def _parse_class_def(self) -> ClassDef:
        """Parse class definition"""
        self._consume_keyword('wadah')
        name = self._advance().value
        self._consume(TokenType.COLON)
        self._skip_newlines()
        body = self._parse_block()
        return ClassDef(name, body)
    
    def _parse_return_statement(self) -> ReturnStatement:
        """Parse return statement"""
        self._consume_keyword('kembalikan')
        value = None
        if not self._check(TokenType.NEWLINE) and not self._check(TokenType.EOF):
            value = self._parse_expression()
        return ReturnStatement(value)
    
    def _parse_import_statement(self) -> ImportStatement:
        """Parse import statement"""
        self._consume_keyword('impor')
        module = self._advance().value
        
        alias = None
        if self._check_keyword('sbg'):
            self._consume_keyword('sbg')
            alias = self._advance().value
        
        return ImportStatement(module, alias)
    
    def _parse_expression_statement(self) -> ASTNode:
        """Parse expression or assignment"""
        expr = self._parse_assignment()
        self._skip_newlines()
        return expr
    
    def _parse_assignment(self) -> ASTNode:
        """Parse assignment or expression"""
        expr = self._parse_logical_or()
        
        if self._check(TokenType.ASSIGNMENT):
            self._advance()
            value = self._parse_assignment()
            if isinstance(expr, Identifier):
                return Assignment(expr.name, value)
        
        return expr
    
    def _parse_logical_or(self) -> ASTNode:
        """Parse logical OR expression"""
        left = self._parse_logical_and()
        
        while self._check_keyword('atau'):
            op = self._advance().value
            right = self._parse_logical_and()
            left = BinaryOp(left, op, right)
        
        return left
    
    def _parse_logical_and(self) -> ASTNode:
        """Parse logical AND expression"""
        left = self._parse_comparison()
        
        while self._check_keyword('dan'):
            op = self._advance().value
            right = self._parse_comparison()
            left = BinaryOp(left, op, right)
        
        return left
    
    def _parse_comparison(self) -> ASTNode:
        """Parse comparison expression"""
        left = self._parse_additive()
        
        while self._check(TokenType.COMPARISON):
            op = self._advance().value
            right = self._parse_additive()
            left = BinaryOp(left, op, right)
        
        return left
    
    def _parse_additive(self) -> ASTNode:
        """Parse addition/subtraction"""
        left = self._parse_multiplicative()
        
        while self.position < len(self.tokens) and self.tokens[self.position].value in ('+', '-'):
            op = self._advance().value
            right = self._parse_multiplicative()
            left = BinaryOp(left, op, right)
        
        return left
    
    def _parse_multiplicative(self) -> ASTNode:
        """Parse multiplication/division"""
        left = self._parse_unary()
        
        while self.position < len(self.tokens) and self.tokens[self.position].value in ('*', '/', '%', '//'):
            op = self._advance().value
            right = self._parse_unary()
            left = BinaryOp(left, op, right)
        
        return left
    
    def _parse_unary(self) -> ASTNode:
        """Parse unary expressions"""
        if self._check_keyword('bukan'):
            op = self._advance().value
            operand = self._parse_unary()
            return UnaryOp(op, operand)
        
        if self.position < len(self.tokens) and self.tokens[self.position].value in ('-', '+'):
            op = self._advance().value
            operand = self._parse_unary()
            return UnaryOp(op, operand)
        
        return self._parse_postfix()
    
    def _parse_postfix(self) -> ASTNode:
        """Parse postfix expressions (function calls, member access)"""
        expr = self._parse_primary()
        
        while True:
            if self._check(TokenType.LPAREN):
                self._advance()
                args = []
                if not self._check(TokenType.RPAREN):
                    args.append(self._parse_expression())
                    while self._check(TokenType.COMMA):
                        self._advance()
                        args.append(self._parse_expression())
                self._consume(TokenType.RPAREN)
                expr = Call(expr, args)
            elif self._check(TokenType.DOT):
                self._advance()
                member = self._advance().value
                expr = BinaryOp(expr, '.', Identifier(member))
            else:
                break
        
        return expr
    
    def _parse_primary(self) -> ASTNode:
        """Parse primary expressions"""
        if self._check(TokenType.NUMBER):
            value = self._advance().value
            if '.' in value:
                return Number(float(value))
            return Number(int(value))
        
        if self._check(TokenType.STRING):
            return String(self._advance().value)
        
        if self._check(TokenType.IDENTIFIER):
            return Identifier(self._advance().value)
        
        if self._check(TokenType.LPAREN):
            self._advance()
            expr = self._parse_expression()
            self._consume(TokenType.RPAREN)
            return expr
        
        # Handle boolean and None literals
        if self._check_keyword('BENAR'):
            self._advance()
            return Identifier('BENAR')
        if self._check_keyword('SALAH'):
            self._advance()
            return Identifier('SALAH')
        if self._check_keyword('KOSONG'):
            self._advance()
            return Identifier('KOSONG')
        
        raise Exception(f"Unexpected token: {self._current_token()}")
    
    def _parse_expression(self) -> ASTNode:
        """Parse a complete expression"""
        return self._parse_assignment()
    
    def _parse_block(self) -> List[ASTNode]:
        """Parse an indented block of statements"""
        if self._check(TokenType.INDENT):
            self._advance()
        
        statements = []
        while not self._check(TokenType.DEDENT) and not self._is_at_end():
            if self._check(TokenType.NEWLINE):
                self._advance()
                continue
            stmt = self._parse_statement()
            if stmt:
                statements.append(stmt)
        
        if self._check(TokenType.DEDENT):
            self._advance()
        
        return statements
    
    def _check(self, token_type: TokenType) -> bool:
        """Check if current token is of given type"""
        if self._is_at_end():
            return False
        return self._current_token().type == token_type
    
    def _check_keyword(self, keyword: str) -> bool:
        """Check if current token is an identifier with given value"""
        if self._is_at_end():
            return False
        token = self._current_token()
        return token.type == TokenType.IDENTIFIER and token.value == keyword
    
    def _advance(self) -> Token:
        """Move to next token and return current"""
        token = self._current_token()
        if not self._is_at_end():
            self.position += 1
        return token
    
    def _consume(self, token_type: TokenType) -> Token:
        """Consume token of given type or raise error"""
        if self._check(token_type):
            return self._advance()
        raise Exception(f"Expected {token_type}, got {self._current_token()}")
    
    def _consume_keyword(self, keyword: str) -> Token:
        """Consume keyword or raise error"""
        if self._check_keyword(keyword):
            return self._advance()
        raise Exception(f"Expected keyword '{keyword}', got {self._current_token()}")
    
    def _skip_newlines(self):
        """Skip any newline tokens"""
        while self._check(TokenType.NEWLINE):
            self._advance()
    
    def _current_token(self) -> Token:
        """Get current token without advancing"""
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return self.tokens[-1]  # EOF
    
    def _is_at_end(self) -> bool:
        """Check if we're at end of tokens"""
        return self.position >= len(self.tokens) or self._current_token().type == TokenType.EOF
