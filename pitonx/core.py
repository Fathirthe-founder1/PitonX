"""
PitonX Core Module
Main logic for transpiling and running PitonX code
"""

from pitonx.lexer import Lexer
from pitonx.parser import Parser
from pitonx.transpiler import Transpiler
from pitonx.errors import PitonXError


def transpile(source_code):
    """
    Transpile PitonX source code to Python
    
    Args:
        source_code (str): PitonX source code
        
    Returns:
        str: Equivalent Python code
        
    Raises:
        PitonXError: If transpilation fails
    """
    try:
        # Lexical analysis
        lexer = Lexer(source_code)
        tokens = lexer.get_tokens()
        
        # Parsing
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Transpilation
        transpiler = Transpiler(ast)
        python_code = transpiler.transpile()
        
        return python_code
    except PitonXError as e:
        raise e
    except Exception as e:
        raise PitonXError(f"Kesalahan transpilasi: {str(e)}")


def run(source_code, globals_dict=None, locals_dict=None):
    """
    Transpile and execute PitonX code
    
    Args:
        source_code (str): PitonX source code
        globals_dict (dict): Global namespace (optional)
        locals_dict (dict): Local namespace (optional)
        
    Returns:
        The result of executing the code
        
    Raises:
        PitonXError: If transpilation fails
    """
    try:
        python_code = transpile(source_code)
        
        if globals_dict is None:
            globals_dict = {}
        if locals_dict is None:
            locals_dict = {}
            
        exec(python_code, globals_dict, locals_dict)
        return locals_dict
    except PitonXError as e:
        raise e
    except Exception as e:
        raise PitonXError(f"Kesalahan eksekusi: {str(e)}")
