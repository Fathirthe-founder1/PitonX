"""
PitonX Keywords Dictionary
Maps Indonesian keywords to Python equivalents
"""

KEYWORDS = {
    # Output
    "ketik": "print",
    # Input
    "masukan": "input",
    # Function definition
    "buat": "def",
    # Return statement
    "kembalikan": "return",
    # Conditional
    "jika": "if",
    "jikalau": "elif",
    "selain": "else",
    # Loops
    "selagi": "while",
    "ulangi": "for",
    "henti": "break",
    "lanjut": "continue",
    # Data types
    "teks": "str",
    "bilangan": "int",
    "desimal": "float",
    "logika": "bool",
    "daftar": "list",
    "peta": "dict",
    # Built-in functions
    "panjang": "len",
    "rentang": "range",
    # Boolean values
    "BENAR": "True",
    "SALAH": "False",
    "KOSONG": "None",
    # Logical operators
    "dan": "and",
    "atau": "or",
    "bukan": "not",
    # Import statements
    "impor": "import",
    "dari": "from",
    "sbg": "as",
    # Exception handling
    "coba": "try",
    "tangkapi": "except",
    "lontar": "raise",
}

# Reverse mapping for Python to Indonesian
REVERSE_KEYWORDS = {v: k for k, v in KEYWORDS.items()}

# All valid PitonX identifiers
VALID_KEYWORDS = set(KEYWORDS.keys())
