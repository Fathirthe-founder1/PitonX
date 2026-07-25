"""
Transpiler Module - Converts PitonX code to Python
"""

from pitonx.lexer import Lexer
from pitonx.parser import Parser, ASTNode, Program, BinaryOp, UnaryOp, Call, Identifier, Number, String
from pitonx.parser import Assignment, IfStatement, WhileLoop, ForLoop, FunctionDef, ClassDef, ReturnStatement, ImportStatement
from pitonx.builtins import KAMUS_INTI, is_indonesian_keyword, get_python_equivalent

class Transpiler:
    """Transpiles PitonX source code to Python"""
    
    def __init__(self):
        self.indent_level = 0
        self.kamus = KAMUS_INTI.copy()
    
    def transpile(self, source: str) -> str:
        """Convert PitonX source code to Python"""
        # Lexical analysis
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        # Parsing
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Code generation
        python_code = self._generate_code(ast)
        return python_code
    
    def _generate_code(self, node: ASTNode) -> str:
        """Generate Python code from AST node"""
        if isinstance(node, Program):
            lines = []
            for stmt in node.statements:
                code = self._generate_code(stmt)
                if code:
                    lines.append(code)
            return '\n'.join(lines)
        
        elif isinstance(node, BinaryOp):
            return self._generate_binary_op(node)
        
        elif isinstance(node, UnaryOp):
            return self._generate_unary_op(node)
        
        elif isinstance(node, Call):
            return self._generate_call(node)
        
        elif isinstance(node, Identifier):
            return self._translate_identifier(node.name)
        
        elif isinstance(node, Number):
            return str(node.value)
        
        elif isinstance(node, String):
            return f'"{node.value}"'
        
        elif isinstance(node, Assignment):
            return self._generate_assignment(node)
        
        elif isinstance(node, IfStatement):
            return self._generate_if_statement(node)
        
        elif isinstance(node, WhileLoop):
            return self._generate_while_loop(node)
        
        elif isinstance(node, ForLoop):
            return self._generate_for_loop(node)
        
        elif isinstance(node, FunctionDef):
            return self._generate_function_def(node)
        
        elif isinstance(node, ClassDef):
            return self._generate_class_def(node)
        
        elif isinstance(node, ReturnStatement):
            return self._generate_return_statement(node)
        
        elif isinstance(node, ImportStatement):
            return self._generate_import_statement(node)
        
        return ""
    
    def _translate_identifier(self, name: str) -> str:
        """Translate Indonesian identifier to Python equivalent"""
        if is_indonesian_keyword(name):
            return get_python_equivalent(name)
        return name
    
    def _generate_binary_op(self, node: BinaryOp) -> str:
        """Generate binary operation"""
        left = self._generate_code(node.left)
        right = self._generate_code(node.right)
        op = self._translate_identifier(node.operator)
        
        if op == '.':
            return f"{left}.{right}"
        
        return f"({left} {op} {right})"
    
    def _generate_unary_op(self, node: UnaryOp) -> str:
        """Generate unary operation"""
        operand = self._generate_code(node.operand)
        op = self._translate_identifier(node.operator)
        
        if op == 'not':
            return f"(not {operand})"
        
        return f"({op}{operand})"
    
    def _generate_call(self, node: Call) -> str:
        """Generate function call"""
        func = self._generate_code(node.func)
        args = ', '.join(self._generate_code(arg) for arg in node.args)
        return f"{func}({args})"
    
    def _generate_assignment(self, node: Assignment) -> str:
        """Generate assignment statement"""
        var = self._translate_identifier(node.target)
        value = self._generate_code(node.value)
        return f"{var} = {value}"
    
    def _generate_if_statement(self, node: IfStatement) -> str:
        """Generate if statement"""
        lines = []
        
        condition = self._generate_code(node.condition)
        lines.append(f"if {condition}:")
        
        self.indent_level += 1
        for stmt in node.body:
            code = self._generate_code(stmt)
            if code:
                lines.append(self._indent(code))
        self.indent_level -= 1
        
        for elif_condition, elif_body in node.elif_parts:
            condition = self._generate_code(elif_condition)
            lines.append(f"elif {condition}:")
            
            self.indent_level += 1
            for stmt in elif_body:
                code = self._generate_code(stmt)
                if code:
                    lines.append(self._indent(code))
            self.indent_level -= 1
        
        if node.else_body:
            lines.append("else:")
            
            self.indent_level += 1
            for stmt in node.else_body:
                code = self._generate_code(stmt)
                if code:
                    lines.append(self._indent(code))
            self.indent_level -= 1
        
        return '\n'.join(lines)
    
    def _generate_while_loop(self, node: WhileLoop) -> str:
        """Generate while loop"""
        lines = []
        
        condition = self._generate_code(node.condition)
        lines.append(f"while {condition}:")
        
        self.indent_level += 1
        for stmt in node.body:
            code = self._generate_code(stmt)
            if code:
                lines.append(self._indent(code))
        self.indent_level -= 1
        
        return '\n'.join(lines)
    
    def _generate_for_loop(self, node: ForLoop) -> str:
        """Generate for loop"""
        lines = []
        
        target = self._translate_identifier(node.target)
        iterable = self._generate_code(node.iterable)
        lines.append(f"for {target} in {iterable}:")
        
        self.indent_level += 1
        for stmt in node.body:
            code = self._generate_code(stmt)
            if code:
                lines.append(self._indent(code))
        self.indent_level -= 1
        
        return '\n'.join(lines)
    
    def _generate_function_def(self, node: FunctionDef) -> str:
        """Generate function definition"""
        lines = []
        
        name = self._translate_identifier(node.name)
        params = ', '.join(self._translate_identifier(p) for p in node.params)
        lines.append(f"def {name}({params}):")
        
        self.indent_level += 1
        for stmt in node.body:
            code = self._generate_code(stmt)
            if code:
                lines.append(self._indent(code))
        self.indent_level -= 1
        
        return '\n'.join(lines)
    
    def _generate_class_def(self, node: ClassDef) -> str:
        """Generate class definition"""
        lines = []
        
        name = self._translate_identifier(node.name)
        lines.append(f"class {name}:")
        
        self.indent_level += 1
        for stmt in node.body:
            code = self._generate_code(stmt)
            if code:
                lines.append(self._indent(code))
        self.indent_level -= 1
        
        return '\n'.join(lines)
    
    def _generate_return_statement(self, node: ReturnStatement) -> str:
        """Generate return statement"""
        if node.value:
            value = self._generate_code(node.value)
            return f"return {value}"
        return "return"
    
    def _generate_import_statement(self, node: ImportStatement) -> str:
        """Generate import statement"""
        module = node.module
        if node.alias:
            return f"import {module} as {node.alias}"
        return f"import {module}"
    
    def _indent(self, code: str) -> str:
        """Add indentation to code"""
        return "    " * self.indent_level + code
