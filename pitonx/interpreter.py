"""
Interpreter Module - Executes translated Python code
"""

from typing import Any, Dict, Optional

class PitonXInterpreter:
    """Executes Python code generated from PitonX transpiler"""
    
    def __init__(self):
        self.globals = {}
        self.locals = {}
        self._setup_builtins()
    
    def _setup_builtins(self):
        """Setup Python builtins"""
        self.globals.update({
            'print': print,
            'input': input,
            'len': len,
            'range': range,
            'str': str,
            'int': int,
            'float': float,
            'bool': bool,
            'list': list,
            'dict': dict,
            'type': type,
            'max': max,
            'min': min,
            'sum': sum,
            'sorted': sorted,
            'abs': abs,
            'round': round,
            'pow': pow,
            'open': open,
            '__name__': '__main__',
        })
    
    def execute(self, python_code: str, variables: Optional[Dict[str, Any]] = None) -> Any:
        """
        Execute Python code in isolated environment.
        
        Args:
            python_code (str): Python source code to execute
            variables (dict): Optional variables to inject into execution environment
            
        Returns:
            Result of code execution
        """
        exec_globals = self.globals.copy()
        exec_locals = self.locals.copy()
        
        if variables:
            exec_locals.update(variables)
        
        try:
            exec(python_code, exec_globals, exec_locals)
            return exec_locals
        except Exception as e:
            raise RuntimeError(f"Runtime error: {str(e)}")
    
    def eval_expression(self, python_code: str) -> Any:
        """Evaluate a Python expression"""
        try:
            return eval(python_code, self.globals, self.locals)
        except Exception as e:
            raise RuntimeError(f"Evaluation error: {str(e)}")
