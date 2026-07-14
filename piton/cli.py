import sys
from pathlib import Path
from .core import translate, run_piton

def main():
    if len(sys.argv) < 2:
        print("Piton CLI")
        print("Cara pakai: piton nama_file.pt")
        return

    file_path = sys.argv[1]
    if not Path(file_path).exists():
        print(f"File '{file_path}' tidak ditemukan.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    try:
        run_piton(code)
    except Exception as e:
        print(f"ERROR: {e}")
