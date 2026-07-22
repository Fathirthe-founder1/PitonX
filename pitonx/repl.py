import code
import builtins
from .core import translate

def main():
    safe_globals = {'__builtins__': builtins.__dict__}
    console = code.InteractiveConsole(locals=safe_globals)
    
    print("PitonX REPL — Ketik 'exit' untuk keluar")
    print("Ketik 'kamusx' untuk melihat kamus PitonX")
    
    while True:
        try:
            line = input(">>> ")
            if line.strip() == 'exit':
                break
            if line.strip() == 'kamusx':
                from .kamusx import tampilkan_kamus
                tampilkan_kamus()
                continue
            if not line.strip():
                continue
            
            
            py_code = translate(line)
            
            console.push(py_code)
            
        except KeyboardInterrupt:
            print("\nKeluar...")
            break
        except Exception as e:
            print(f"Error: {e}")
