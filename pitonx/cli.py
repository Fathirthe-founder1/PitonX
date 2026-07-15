import sys
from pathlib import Path
from .core import translate, run_pitonx

def main():
    if len(sys.argv) < 2:
        print("PitonX CLI")
        print("Cara pakai: pitonx nama_file.pt")
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
