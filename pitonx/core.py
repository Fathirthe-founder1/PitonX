import sys
from .builtins import KAMUS_INTI

def translate(kode: str) -> str:
    lines = kode.split('\n')
    hasil = []
    for line in lines:
        # Mode Super Singkat (string langsung)
        if line.strip().startswith('"') and line.strip().endswith('"') and '=' not in line:
            hasil.append(f'print({line.strip()})')
        else:
            # Ganti semua keyword PitonX dengan Python
            for kata, py in KAMUS_INTI.items():
                line = line.replace(kata, py)
            hasil.append(line)
    return '\n'.join(hasil)

def run(kode: str):
    try:
        py_kode = translate(kode)
        exec(py_kode, {'__builtins__': __builtins__})
    except Exception as e:
        print(f"Error: {e}")
