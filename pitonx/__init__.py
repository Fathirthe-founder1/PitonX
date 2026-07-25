"""
PitonX - Indonesian Python Transpiler
A lightweight Python-based transpiler with Indonesian syntax.

Author: Jameson AlFathir Void
License: MIT
"""

__version__ = "1.0.0"
__author__ = "Jameson AlFathir Void"
__license__ = "MIT"

from pitonx.transpiler import Transpiler
from pitonx.interpreter import PitonXInterpreter

def run(code, variables=None):
    """
    Run PitonX code and return result.
    
    Args:
        code (str): PitonX source code
        variables (dict): Optional variables to pass to execution environment
        
    Returns:
        Result of code execution
        
    Example:
        >>> import pitonx as px
        >>> code = 'ketik("Halo Dunia dari PitonX")'
        >>> px.run(code)
        Halo Dunia dari PitonX
    """
    transpiler = Transpiler()
    python_code = transpiler.transpile(code)
    
    interpreter = PitonXInterpreter()
    return interpreter.execute(python_code, variables)

def transpile(code):
    """
    Transpile PitonX code to Python.
    
    Args:
        code (str): PitonX source code
        
    Returns:
        str: Python source code
    """
    transpiler = Transpiler()
    return transpiler.transpile(code)

__all__ = ['run', 'transpile', 'Transpiler', 'PitonXInterpreter']
