"""
CLI Module - Command-line interface for PitonX
"""

import sys
import os
from pathlib import Path
from pitonx.transpiler import Transpiler
from pitonx.interpreter import PitonXInterpreter
from pitonx.repl import run_repl

def show_tutorial():
    """Show PitonX tutorial"""
    tutorial = """
╔════════════════════════════════════════════════════════════════╗
║                    PitonX - Tutorial                          ║
║        A lightweight Python-based transpiler                  ║
║            with Indonesian syntax                             ║
╚════════════════════════════════════════════════════════════════╝

📚 PENGENALAN
PitonX adalah transpiler Python berbasis bahasa Indonesia yang
memungkinkan Anda menulis kode Python dengan sintaks bahasa Indonesia.

🚀 CARA PENGGUNAAN

1. MODE INTERACTIVE (REPL)
   $ piton
   
   Ini akan membuka shell interaktif di mana Anda bisa menulis
   kode PitonX baris per baris.

2. MENJALANKAN FILE
   $ pitonx file.px
   
   Menjalankan file PitonX (.px extension)

3. MENGGUNAKAN SEBAGAI LIBRARY PYTHON
   
   import pitonx as px
   
   code = '''ketik(\"Halo Dunia dari PitonX\")'''
   px.run(code)

📖 CONTOH KODE PITONX

1. Cetak Teks:
   ketik(\"Halo Dunia!\")
   
   Equivalent Python:
   print(\"Halo Dunia!\")

2. Deklarasi Variabel:
   x = 10
   nama = \"PitonX\"
   
3. Kontrol Alur (If-Else):
   jika x > 5:
       ketik(\"x lebih dari 5\")
   selain:
       ketik(\"x kurang atau sama dengan 5\")
   
   Equivalent Python:
   if x > 5:
       print(\"x lebih dari 5\")
   else:
       print(\"x kurang atau sama dengan 5\")

4. Perulangan (For Loop):
   ulangi i dalam rentang(5):
       ketik(i)
   
   Equivalent Python:
   for i in range(5):
       print(i)

5. Perulangan (While Loop):
   x = 0
   selagi x < 5:
       ketik(x)
       x = x + 1
   
   Equivalent Python:
   x = 0
   while x < 5:
       print(x)
       x = x + 1

6. Fungsi:
   buat jumlah(a, b):
       kembalikan a + b
   
   hasil = jumlah(3, 4)
   ketik(hasil)
   
   Equivalent Python:
   def jumlah(a, b):
       return a + b
   
   hasil = jumlah(3, 4)
   print(hasil)

7. Kelas (Class):
   wadah Mobil:
       buat __awal__(nama):
           saya.nama = nama
   
   mobil_saya = Mobil(\"Honda\")

📋 KAMUS LENGKAP

INPUT/OUTPUT:
  ketik        → print
  masukan      → input

FUNGSI:
  buat         → def
  kembalikan   → return
  wadah        → class

KONTROL ALUR:
  jika         → if
  jikalau      → elif
  selain       → else

PERULANGAN:
  selagi       → while
  ulangi       → for
  henti        → break
  lanjut       → continue

TIPE DATA:
  teks         → str
  bilangan     → int
  desimal      → float
  logika       → bool
  daftar       → list
  peta         → dict

OPERATOR:
  dan          → and
  atau         → or
  bukan        → not

IMPORT:
  impor        → import
  dari         → from
  sbg          → as

ERROR HANDLING:
  coba         → try
  tangkapi     → except
  lontar       → raise

LAINNYA:
  panjang      → len
  jenis        → type
  rentang      → range
  maks         → max
  min          → min
  total        → sum

💡 TIPS

1. Gunakan file dengan extension .px untuk PitonX
2. Indentasi penting dalam PitonX (seperti Python)
3. Anda bisa mencampur code PitonX dan Python dalam library mode
4. REPL memungkinkan Anda testing code secara interaktif

🎯 INFORMASI LEBIH LANJUT

Dokumentasi: https://github.com/Fathirthe-founder1/PitonX
License: MIT
Author: Jameson AlFathir Void

Selamat menulis kode dengan PitonX! 🎉
"""
    print(tutorial)

def run_file(filepath):
    """Run a PitonX file"""
    try:
        # Check if file exists
        path = Path(filepath)
        if not path.exists():
            print(f"❌ File tidak ditemukan: {filepath}")
            sys.exit(1)
        
        # Read file
        with open(filepath, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        # Transpile and execute
        transpiler = Transpiler()
        python_code = transpiler.transpile(source_code)
        
        interpreter = PitonXInterpreter()
        interpreter.execute(python_code)
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)

def main():
    """Main CLI entry point"""
    if len(sys.argv) < 2:
        # No arguments - show tutorial
        show_tutorial()
    elif sys.argv[1] in ['bantuan', 'help', '--help', '-h']:
        show_tutorial()
    elif sys.argv[1] in ['repl', 'interaktif', 'interactive']:
        run_repl()
    elif sys.argv[1].endswith('.px'):
        run_file(sys.argv[1])
    else:
        print(f"❌ Perintah tidak dikenali: {sys.argv[1]}")
        print("Gunakan: pitonx [file.px | repl | bantuan]")
        sys.exit(1)

if __name__ == '__main__':
    main()
