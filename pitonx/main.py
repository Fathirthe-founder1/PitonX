"""
PitonX Command Line Interface
Entry point for pitonx command
"""

import sys
import os
from pathlib import Path

from pitonx import __version__
from pitonx.core import transpile, run
from pitonx.repl import start_repl
from pitonx.errors import PitonXError


def print_help():
    """
    Print help message
    """
    help_text = f"""
PitonX {__version__} - Bahasa Pemrograman Indonesia

Penggunaan:
  piton              Masuk ke REPL interaktif
  pitonx FILE        Jalankan file .px
  pitonx --help      Tampilkan pesan bantuan ini
  pitonx --version   Tampilkan versi PitonX
  pitonx --transpile FILE   Tampilkan kode Python yang dihasilkan

Contoh:
  pitonx program.px
  pitonx --transpile program.px

Kata Kunci PitonX:
  ketik (print)       - Cetak ke layar
  masukan (input)     - Masukkan dari pengguna
  buat (def)          - Definisikan fungsi
  kembalikan (return) - Kembalikan nilai dari fungsi
  jika (if)           - Kondisi jika
  jikalau (elif)      - Kondisi jika tidak
  selain (else)       - Kondisi selainnya
  selagi (while)      - Loop selama
  ulangi (for)        - Loop ulangi
  henti (break)       - Henti loop
  lanjut (continue)   - Lanjut ke iterasi berikutnya
  coba (try)          - Coba eksekusi
  tangkapi (except)   - Tangkap exception
  lontar (raise)      - Lontar exception
  impor (import)      - Impor modul
  dari (from)         - Dari modul
  sbg (as)            - Sebagai alias

Tipe Data:
  teks (str)          - String/Teks
  bilangan (int)      - Integer/Bilangan bulat
  desimal (float)     - Float/Desimal
  logika (bool)       - Boolean/Logika
  daftar (list)       - List/Daftar
  peta (dict)         - Dictionary/Peta

Konstan:
  BENAR (True)        - Benar
  SALAH (False)       - Salah
  KOSONG (None)       - Kosong/Tidak ada

Operator Logika:
  dan (and)           - Dan
  atau (or)           - Atau
  bukan (not)         - Bukan

Fungsi Bawaan:
  panjang (len)       - Panjang
  rentang (range)     - Rentang

"""
    print(help_text)


def print_version():
    """
    Print version information
    """
    print(f"PitonX {__version__}")
    print("Bahasa Pemrograman Indonesia yang dikompilasi ke Python")
    print("Repository: https://github.com/Fathirthe-founder1/PitonX")


def transpile_file(filepath):
    """
    Transpile a PitonX file and print the Python code
    
    Args:
        filepath (str): Path to the .px file
    """
    try:
        path = Path(filepath)
        if not path.exists():
            print(f"❌ Kesalahan: File '{filepath}' tidak ditemukan", file=sys.stderr)
            sys.exit(1)

        with open(path, 'r', encoding='utf-8') as f:
            source = f.read()

        python_code = transpile(source)
        print(python_code)
    except PitonXError as e:
        print(f"❌ {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Kesalahan: {e}", file=sys.stderr)
        sys.exit(1)


def run_file(filepath):
    """
    Run a PitonX file
    
    Args:
        filepath (str): Path to the .px file
    """
    try:
        path = Path(filepath)
        if not path.exists():
            print(f"❌ Kesalahan: File '{filepath}' tidak ditemukan", file=sys.stderr)
            sys.exit(1)

        with open(path, 'r', encoding='utf-8') as f:
            source = f.read()

        run(source)
    except PitonXError as e:
        print(f"❌ {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nDihentikan oleh pengguna", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Kesalahan: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """
    Main entry point for pitonx CLI
    """
    if len(sys.argv) == 1:
        # No arguments - start REPL
        start_repl()
    elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
        print_help()
    elif sys.argv[1] == '--version' or sys.argv[1] == '-v':
        print_version()
    elif sys.argv[1] == '--transpile' or sys.argv[1] == '-t':
        if len(sys.argv) < 3:
            print("❌ Kesalahan: File harus diberikan dengan opsi --transpile", file=sys.stderr)
            sys.exit(1)
        transpile_file(sys.argv[2])
    elif sys.argv[1].endswith('.px'):
        # Run file
        run_file(sys.argv[1])
    else:
        print(f"❌ Kesalahan: Argumen tidak dikenali '{sys.argv[1]}'", file=sys.stderr)
        print("Gunakan 'pitonx --help' untuk bantuan", file=sys.stderr)
        sys.exit(1)


def repl_main():
    """
    Main entry point for piton command (REPL only)
    """
    start_repl()


if __name__ == '__main__':
    main()
