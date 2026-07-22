import sys
import builtins
from .core import translate, run
from .kamusx import tampilkan_kamus

def main():
    # Jika ada argumen file
    if len(sys.argv) > 1:
        if sys.argv[1] == 'kamusx':
            tampilkan_kamus()
            return
        try:
            with open(sys.argv[1], 'r', encoding='utf-8') as f:
                kode = f.read()
            run(kode)
            return
        except FileNotFoundError:
            print(f"File '{sys.argv[1]}' tidak ditemukan.")
            return
        except Exception as e:
            print(f"Error: {e}")
            return

    # Jika tidak ada argumen → masuk REPL
    print("PitonX REPL — Ketik 'exit' untuk keluar")
    print("Ketik 'kamusx' untuk melihat kamus PitonX")
    while True:
        try:
            line = input(">>> ")
            if line.strip() == 'exit':
                break
            if line.strip() == 'kamusx':
                tampilkan_kamus()
                continue
            if not line.strip():
                continue
            py = translate(line)
            exec(py, {'__builtins__': builtins.__dict__})
        except KeyboardInterrupt:
            print("\nKeluar...")
            break
        except Exception as e:
            print(f"Error: {e}")
