"""
PitonX Parser
Converts tokens into an Abstract Syntax Tree (AST)
"""

from pitonx.errors import ParserError
from pitonx.keywords import KEYWORDS


class ASTNode:
    """Base class for all AST nodes"""
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"


class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements


class Assignment(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class BinaryOp(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class UnaryOp(ASTNode):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand


class FunctionCall(ASTNode):
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments


class FunctionDef(ASTNode):
    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body


class IfStatement(ASTNode):
    def __init__(self, condition, then_body, else_body=None):
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body


class WhileStatement(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class ForStatement(ASTNode):
    def __init__(self, variable, iterable, body):
        self.variable = variable
        self.iterable = iterable
        self.body = body


class ReturnStatement(ASTNode):
    def __init__(self, value=None):
        self.value = value


class BreakStatement(ASTNode):
    pass


class ContinueStatement(ASTNode):
    pass


class Literal(ASTNode):
    def __init__(self, value, type_):
        self.value = value
        self.type = type_


class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name


class ListLiteral(ASTNode):
    def __init__(self, elements):
        self.elements = elements


class DictLiteral(ASTNode):
    def __init__(self, pairs):
        self.pairs = pairs


class IndexAccess(ASTNode):
    def __init__(self, object_, index):
        self.object = object_
        self.index = index


class AttributeAccess(ASTNode):
    def __init__(self, object_, attribute):
        self.object = object_
        self.attribute = attribute


class Parser:
    """PitonX Parser"""

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        """Parse tokens into AST"""
        statements = []
        while not self.is_at_end():
            if self.peek().type in ('NEWLINE', 'EOF'):
                self.advance()
                continue
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        return Program(statements)

    def parse_statement(self):
        """Parse a single statement"""
        token = self.peek()

        if token.type == 'KATA_KUNCI':
            keyword = KEYWORDS.get(token.value)
            if keyword == 'def':
                return self.parse_function_def()
            elif keyword == 'if':
                return self.parse_if_statement()
            elif keyword == 'while':
                return self.parse_while_statement()
            elif keyword == 'for':
                return self.parse_for_statement()
            elif keyword == 'return':
                return self.parse_return_statement()
            elif keyword == 'break':
                self.advance()
                self.skip_newline()
                return BreakStatement()
            elif keyword == 'continue':
                self.advance()
                self.skip_newline()
                return ContinueStatement()

        expr = self.parse_expression()
        self.skip_newline()
        return expr

    def parse_function_def(self):
        """Parse function definition"""
        self.expect_keyword('buat')
        name = self.expect('IDENTIFIER').value
        self.expect('TANDA_KURUNG_BUKA')

        parameters = []
        while self.peek().type != 'TANDA_KURUNG_TUTUP':
            param = self.expect('IDENTIFIER').value
            parameters.append(param)
            if self.peek().type == 'KOMA':
                self.advance()
            elif self.peek().type != 'TANDA_KURUNG_TUTUP':
                raise ParserError("Expected ',' or ')'")

        self.expect('TANDA_KURUNG_TUTUP')
        self.expect('TITIK_DUA')
        self.skip_newline()
        body = self.parse_block()

        return FunctionDef(name, parameters, body)

    def parse_if_statement(self):
        """Parse if statement"""
        self.expect_keyword('jika')
        condition = self.parse_expression()
        self.expect('TITIK_DUA')
        self.skip_newline()
        then_body = self.parse_block()

        else_body = None
        if self.peek().type == 'KATA_KUNCI' and KEYWORDS.get(self.peek().value) in ('elif', 'else'):
            if KEYWORDS.get(self.peek().value) == 'elif':
                else_body = self.parse_if_statement()
            else:
                self.expect_keyword('selain')
                self.expect('TITIK_DUA')
                self.skip_newline()
                else_body = self.parse_block()

        return IfStatement(condition, then_body, else_body)

    def parse_while_statement(self):
        """Parse while loop"""
        self.expect_keyword('selagi')
        condition = self.parse_expression()
        self.expect('TITIK_DUA')
        self.skip_newline()
        body = self.parse_block()
        return WhileStatement(condition, body)

    def parse_for_statement(self):
        """Parse for loop"""
        self.expect_keyword('ulangi')
        variable = self.expect('IDENTIFIER').value
        self.expect_keyword('dalam') if self.peek().type == 'KATA_KUNCI' and self.peek().value == 'dalam' else None
        iterable = self.parse_expression()
        self.expect('TITIK_DUA')
        self.skip_newline()
        body = self.parse_block()
        return ForStatement(variable, iterable, body)

    def parse_return_statement(self):
        """Parse return statement"""
        self.expect_keyword('kembalikan')
        value = None
        if self.peek().type != 'NEWLINE' and self.peek().type != 'EOF':
            value = self.parse_expression()
        self.skip_newline()
        return ReturnStatement(value)

    def parse_block(self):
        """Parse a block of statements"""
        statements = []
        self.expect('INDENT')
        while self.peek().type != 'DEDENT' and not self.is_at_end():
            if self.peek().type == 'NEWLINE':
                self.advance()
                continue
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        self.expect('DEDENT')
        return statements

    def parse_expression(self):
        """Parse an expression"""
        return self.parse_assignment()

    def parse_assignment(self):
        """Parse assignment or other expressions"""
        expr = self.parse_or()

        if self.peek().type == 'OPERATOR_PENUGASAN':
            if expr.__class__.__name__ != 'Identifier':
                raise ParserError("Invalid assignment target")
            op = self.advance().value
            value = self.parse_assignment()
            return Assignment(expr.name, value)

        return expr

    def parse_or(self):
        """Parse logical OR"""
        left = self.parse_and()
        while self.peek().type == 'KATA_KUNCI' and KEYWORDS.get(self.peek().value) == 'or':
            self.advance()
            right = self.parse_and()
            left = BinaryOp(left, 'atau', right)
        return left

    def parse_and(self):
        """Parse logical AND"""
        left = self.parse_not()
        while self.peek().type == 'KATA_KUNCI' and KEYWORDS.get(self.peek().value) == 'and':
            self.advance()
            right = self.parse_not()
            left = BinaryOp(left, 'dan', right)
        return left

    def parse_not(self):
        """Parse logical NOT"""
        if self.peek().type == 'KATA_KUNCI' and KEYWORDS.get(self.peek().value) == 'not':
            self.advance()
            expr = self.parse_not()
            return UnaryOp('bukan', expr)
        return self.parse_comparison()

    def parse_comparison(self):
        """Parse comparison operators"""
        left = self.parse_additive()
        while self.peek().type == 'OPERATOR_PERBANDINGAN':
            op = self.advance().value
            right = self.parse_additive()
            left = BinaryOp(left, op, right)
        return left

    def parse_additive(self):
        """Parse addition and subtraction"""
        left = self.parse_multiplicative()
        while self.peek().type == 'OPERATOR_ARITMATIKA' and self.peek().value in ('+', '-'):
            op = self.advance().value
            right = self.parse_multiplicative()
            left = BinaryOp(left, op, right)
        return left

    def parse_multiplicative(self):
        """Parse multiplication and division"""
        left = self.parse_power()
        while self.peek().type == 'OPERATOR_ARITMATIKA' and self.peek().value in ('*', '/', '//', '%'):
            op = self.advance().value
            right = self.parse_power()
            left = BinaryOp(left, op, right)
        return left

    def parse_power(self):
        """Parse exponentiation"""
        left = self.parse_unary()
        if self.peek().type == 'OPERATOR_ARITMATIKA' and self.peek().value == '**':
            op = self.advance().value
            right = self.parse_power()
            left = BinaryOp(left, op, right)
        return left

    def parse_unary(self):
        """Parse unary expressions"""
        if self.peek().type == 'OPERATOR_ARITMATIKA' and self.peek().value in ('+', '-'):
            op = self.advance().value
            expr = self.parse_unary()
            return UnaryOp(op, expr)
        return self.parse_postfix()

    def parse_postfix(self):
        """Parse postfix expressions (function calls, indexing, attribute access)"""
        expr = self.parse_primary()

        while True:
            if self.peek().type == 'TANDA_KURUNG_BUKA':
                self.advance()
                args = []
                while self.peek().type != 'TANDA_KURUNG_TUTUP':
                    args.append(self.parse_expression())
                    if self.peek().type == 'KOMA':
                        self.advance()
                self.expect('TANDA_KURUNG_TUTUP')
                expr = FunctionCall(expr.name if isinstance(expr, Identifier) else str(expr), args)
            elif self.peek().type == 'KURUNG_KOTAK_BUKA':
                self.advance()
                index = self.parse_expression()
                self.expect('KURUNG_KOTAK_TUTUP')
                expr = IndexAccess(expr, index)
            elif self.peek().type == 'TITIK':
                self.advance()
                attr = self.expect('IDENTIFIER').value
                expr = AttributeAccess(expr, attr)
            else:
                break

        return expr

    def parse_primary(self):
        """Parse primary expressions"""
        token = self.peek()

        # Literals
        if token.type == 'BILANGAN':
            self.advance()
            return Literal(int(token.value), 'int')

        if token.type == 'DESIMAL':
            self.advance()
            return Literal(float(token.value), 'float')

        if token.type == 'TEKS':
            self.advance()
            # Remove quotes
            value = token.value[1:-1]
            return Literal(value, 'str')

        if token.type == 'KATA_KUNCI':
            keyword = KEYWORDS.get(token.value)
            if keyword == 'True':
                self.advance()
                return Literal(True, 'bool')
            elif keyword == 'False':
                self.advance()
                return Literal(False, 'bool')
            elif keyword == 'None':
                self.advance()
                return Literal(None, 'NoneType')

        if token.type == 'IDENTIFIER':
            self.advance()
            return Identifier(token.value)

        if token.type == 'TANDA_KURUNG_BUKA':
            self.advance()
            expr = self.parse_expression()
            self.expect('TANDA_KURUNG_TUTUP')
            return expr

        if token.type == 'KURUNG_KOTAK_BUKA':
            self.advance()
            elements = []
            while self.peek().type != 'KURUNG_KOTAK_TUTUP':
                elements.append(self.parse_expression())
                if self.peek().type == 'KOMA':
                    self.advance()
            self.expect('KURUNG_KOTAK_TUTUP')
            return ListLiteral(elements)

        if token.type == 'KURUNG_KURAWAL_BUKA':
            self.advance()
            pairs = []
            while self.peek().type != 'KURUNG_KURAWAL_TUTUP':
                key = self.parse_expression()
                self.expect('TITIK_DUA')
                value = self.parse_expression()
                pairs.append((key, value))
                if self.peek().type == 'KOMA':
                    self.advance()
            self.expect('KURUNG_KURAWAL_TUTUP')
            return DictLiteral(pairs)

        raise ParserError(f"Unexpected token: {token}")

    def expect_keyword(self, indonesian_keyword):
        """Expect a specific keyword"""
        token = self.peek()
        if token.type != 'KATA_KUNCI' or token.value != indonesian_keyword:
            raise ParserError(f"Expected keyword '{indonesian_keyword}', got {token.value}")
        return self.advance()

    def expect(self, token_type):
        """Expect a token of a specific type"""
        token = self.peek()
        if token.type != token_type:
            raise ParserError(f"Expected {token_type}, got {token.type}")
        return self.advance()

    def peek(self):
        """Look at the current token without consuming it"""
        if self.is_at_end():
            return self.tokens[-1]  # EOF token
        return self.tokens[self.position]

    def advance(self):
        """Consume and return the current token"""
        token = self.peek()
        if not self.is_at_end():
            self.position += 1
        return token

    def skip_newline(self):
        """Skip newline tokens"""
        while self.peek().type == 'NEWLINE':
            self.advance()

    def is_at_end(self):
        """Check if we're at the end of tokens"""
        return self.position >= len(self.tokens) or self.peek().type == 'EOF'
