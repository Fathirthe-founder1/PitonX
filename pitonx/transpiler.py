"""
PitonX Transpiler
Converts AST to Python code
"""

from pitonx.parser import (
    Program, Assignment, BinaryOp, UnaryOp, FunctionCall,
    FunctionDef, IfStatement, WhileStatement, ForStatement,
    ReturnStatement, BreakStatement, ContinueStatement,
    Literal, Identifier, ListLiteral, DictLiteral,
    IndexAccess, AttributeAccess
)
from pitonx.keywords import KEYWORDS
from pitonx.errors import TranspilerError


class Transpiler:
    """Converts PitonX AST to Python code"""

    def __init__(self, ast):
        self.ast = ast
        self.indent_level = 0
        self.output = []

    def transpile(self):
        """Transpile AST to Python code"""
        self.visit(self.ast)
        return '\n'.join(self.output)

    def visit(self, node):
        """Visit a node in the AST"""
        if node is None:
            return

        method_name = f'visit_{node.__class__.__name__}'
        if hasattr(self, method_name):
            return getattr(self, method_name)(node)
        else:
            raise TranspilerError(f"No visitor for {node.__class__.__name__}")

    def visit_Program(self, node):
        """Visit program node"""
        for statement in node.statements:
            self.visit(statement)

    def visit_Assignment(self, node):
        """Visit assignment node"""
        value = self.visit_expr(node.value)
        self.emit(f"{node.name} = {value}")

    def visit_BinaryOp(self, node):
        """Visit binary operation node"""
        left = self.visit_expr(node.left)
        right = self.visit_expr(node.right)
        op = self.translate_operator(node.operator)
        return f"{left} {op} {right}"

    def visit_UnaryOp(self, node):
        """Visit unary operation node"""
        operand = self.visit_expr(node.operand)
        if node.operator == 'bukan':
            return f"not {operand}"
        else:
            return f"{node.operator}{operand}"

    def visit_FunctionCall(self, node):
        """Visit function call node"""
        func_name = self.translate_function_name(node.name)
        args = ', '.join(self.visit_expr(arg) for arg in node.arguments)
        return f"{func_name}({args})"

    def visit_FunctionDef(self, node):
        """Visit function definition node"""
        params = ', '.join(node.parameters)
        self.emit(f"def {node.name}({params}):")
        self.indent_level += 1
        for statement in node.body:
            self.visit(statement)
        self.indent_level -= 1

    def visit_IfStatement(self, node):
        """Visit if statement node"""
        condition = self.visit_expr(node.condition)
        self.emit(f"if {condition}:")
        self.indent_level += 1
        for statement in node.then_body:
            self.visit(statement)
        self.indent_level -= 1

        if node.else_body:
            if isinstance(node.else_body, IfStatement):
                # elif case
                condition = self.visit_expr(node.else_body.condition)
                self.emit(f"elif {condition}:")
                self.indent_level += 1
                for statement in node.else_body.then_body:
                    self.visit(statement)
                self.indent_level -= 1
                if node.else_body.else_body:
                    self.visit_IfStatement(
                        IfStatement(
                            node.else_body.else_body.condition if hasattr(node.else_body.else_body, 'condition') else None,
                            node.else_body.else_body.then_body if hasattr(node.else_body.else_body, 'then_body') else [node.else_body.else_body],
                            node.else_body.else_body.else_body if hasattr(node.else_body.else_body, 'else_body') else None
                        )
                    )
            else:
                # else case
                self.emit("else:")
                self.indent_level += 1
                for statement in node.else_body:
                    self.visit(statement)
                self.indent_level -= 1

    def visit_WhileStatement(self, node):
        """Visit while loop node"""
        condition = self.visit_expr(node.condition)
        self.emit(f"while {condition}:")
        self.indent_level += 1
        for statement in node.body:
            self.visit(statement)
        self.indent_level -= 1

    def visit_ForStatement(self, node):
        """Visit for loop node"""
        iterable = self.visit_expr(node.iterable)
        self.emit(f"for {node.variable} in {iterable}:")
        self.indent_level += 1
        for statement in node.body:
            self.visit(statement)
        self.indent_level -= 1

    def visit_ReturnStatement(self, node):
        """Visit return statement node"""
        if node.value:
            value = self.visit_expr(node.value)
            self.emit(f"return {value}")
        else:
            self.emit("return")

    def visit_BreakStatement(self, node):
        """Visit break statement node"""
        self.emit("break")

    def visit_ContinueStatement(self, node):
        """Visit continue statement node"""
        self.emit("continue")

    def visit_expr(self, node):
        """Visit expression and return its string representation"""
        if node is None:
            return ''

        if isinstance(node, Literal):
            return self.visit_Literal(node)
        elif isinstance(node, Identifier):
            return self.visit_Identifier(node)
        elif isinstance(node, BinaryOp):
            return self.visit_BinaryOp(node)
        elif isinstance(node, UnaryOp):
            return self.visit_UnaryOp(node)
        elif isinstance(node, FunctionCall):
            return self.visit_FunctionCall(node)
        elif isinstance(node, ListLiteral):
            return self.visit_ListLiteral(node)
        elif isinstance(node, DictLiteral):
            return self.visit_DictLiteral(node)
        elif isinstance(node, IndexAccess):
            return self.visit_IndexAccess(node)
        elif isinstance(node, AttributeAccess):
            return self.visit_AttributeAccess(node)
        else:
            raise TranspilerError(f"Unknown expression type: {type(node)}")

    def visit_Literal(self, node):
        """Visit literal node"""
        if node.type == 'str':
            return f"'{node.value}'"
        elif node.type == 'bool':
            return str(node.value)
        elif node.type == 'NoneType':
            return 'None'
        else:
            return str(node.value)

    def visit_Identifier(self, node):
        """Visit identifier node"""
        return node.name

    def visit_ListLiteral(self, node):
        """Visit list literal node"""
        elements = ', '.join(self.visit_expr(elem) for elem in node.elements)
        return f"[{elements}]"

    def visit_DictLiteral(self, node):
        """Visit dict literal node"""
        pairs = ', '.join(
            f"{self.visit_expr(k)}: {self.visit_expr(v)}"
            for k, v in node.pairs
        )
        return f"{{{pairs}}}"

    def visit_IndexAccess(self, node):
        """Visit index access node"""
        obj = self.visit_expr(node.object)
        index = self.visit_expr(node.index)
        return f"{obj}[{index}]"

    def visit_AttributeAccess(self, node):
        """Visit attribute access node"""
        obj = self.visit_expr(node.object)
        return f"{obj}.{node.attribute}"

    def translate_operator(self, operator):
        """Translate PitonX operator to Python"""
        mapping = {
            'dan': 'and',
            'atau': 'or',
            'bukan': 'not',
            '+': '+',
            '-': '-',
            '*': '*',
            '/': '/',
            '//': '//',
            '%': '%',
            '**': '**',
            '==': '==',
            '!=': '!=',
            '<': '<',
            '>': '>',
            '<=': '<=',
            '>=': '>=',
        }
        return mapping.get(operator, operator)

    def translate_function_name(self, name):
        """Translate PitonX function name to Python"""
        return KEYWORDS.get(name, name)

    def emit(self, code):
        """Emit a line of Python code"""
        indent = '    ' * self.indent_level
        self.output.append(f"{indent}{code}")
