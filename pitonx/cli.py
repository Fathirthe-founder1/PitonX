import sys
from pathlib import Path
from .core import translate, run_pitonx
from .logo import LOGO_RED

def main():
    if len(sys.argv) == 1 or sys.argv[1] in ('--help', '-h'):
        print(LOGO_RED)
        print("\nPitonX CLI")
        print("Author: Fathirthe-founder1")
        print("Credit: DeepSeek, Fathirthe-founder1")
        print("\nCommand:")
        print("  piton           - Masuk ke REPL (compiler interaktif)")
        print("  pitonx          - Tampilkan info ini")
        print("  pitonx file.px  - Jalankan file .px / .pt")
        return
    file_path = sys.argv[1]
    if not Path(file_path).exists():
        print(f"File '{file_path}' tidak ditemukan.")
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    try:
        run_pitonx(code)
    except Exception as e:
        print(f"ERROR: {e}")
