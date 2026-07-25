"""
REPL Module - Read-Eval-Print Loop for interactive PitonX shell
"""

import sys
from pitonx.transpiler import Transpiler
from pitonx.interpreter import PitonXInterpreter

class PitonXREPL:
    """Interactive PitonX REPL shell"""
    
    def __init__(self):
        self.transpiler = Transpiler()
        self.interpreter = PitonXInterpreter()
        self.history = []
        self.variables = {}
    
    def start(self):
        """Start the interactive REPL"""
        print("╔══════════════════════════════════════════╗")
        print("║  PitonX REPL - Interactive Shell        ║")
        print("║  Ketik 'keluar' untuk menutup           ║")
        print("╚══════════════════════════════════════════╝")
        print()
        
        while True:
            try:
                # Display prompt
                prompt = "x> "
                code = input(prompt)
                
                if code.strip() == '':
                    continue
                
                if code.lower() in ['keluar', 'exit', 'quit']:
                    print("Sampai jumpa! 👋")
                    break
                
                if code.lower() == 'bantuan':
                    self._show_help()
                    continue
                
                if code.lower() == 'kamus':
                    self._show_kamus()
                    continue
                
                # Execute code
                self._execute_code(code)
                self.history.append(code)
                
            except KeyboardInterrupt:
                print("\n[Dibatalkan oleh pengguna]")
            except Exception as e:
                print(f"❌ Error: {str(e)}")
    
    def _execute_code(self, code: str):
        """Execute a line of code"""
        try:
            # Check if it's an assignment or expression
            if '=' in code and not any(op in code for op in ['==', '!=', '<=', '>=']):
                # Assignment
                transpiled = self.transpiler.transpile(code)
                exec(transpiled, self.interpreter.globals, self.variables)
                
                # Extract variable name
                var_name = code.split('=')[0].strip()
                if var_name in self.variables:
                    print(f"•••")
            else:
                # Expression
                transpiled = self.transpiler.transpile(code)
                result = eval(transpiled, self.interpreter.globals, self.variables)
                if result is not None:
                    print(result)
        except Exception as e:
            raise Exception(str(e))
    
    def _show_help(self):
        """Show help information"""
        print("""
╔════════════════════════════════════════════════════════╗
║              Bantuan PitonX REPL                       ║
╠════════════════════════════════════════════════════════╣
║  Perintah Khusus:                                      ║
║  - keluar/exit/quit  : Keluar dari REPL               ║
║  - bantuan           : Tampilkan bantuan ini          ║
║  - kamus             : Tampilkan kamus PitonX         ║
║                                                        ║
║  Contoh Penggunaan:                                   ║
║  x> x = 10                                            ║
║  •••                                                  ║
║  x> ketik(x)                                          ║
║  10                                                   ║
║  x> ketik("Halo Dunia dari PitonX!")                 ║
║  Halo Dunia dari PitonX!                             ║
╚════════════════════════════════════════════════════════╝
        """)
    
    def _show_kamus(self):
        """Show Indonesian-Python keyword mapping"""
        from pitonx.builtins import KAMUS_INTI
        
        print("\n╔════════════════════════════════════════════╗")
        print("║           Kamus PitonX → Python           ║")
        print("╠════════════════════════════════════════════╣")
        
        categories = {
            'INPUT / OUTPUT': ['ketik', 'masukan', 'buka', 'tutup', 'baca', 'tulis'],
            'FUNGSI & KELAS': ['buat', 'kembalikan', 'wadah', 'anon', 'serahkan'],
            'LOGIKA': ['jika', 'jikalau', 'selain', 'pasti'],
            'PERULANGAN': ['selagi', 'ulangi', 'henti', 'lanjut', 'lewat'],
            'TIPE DATA': ['teks', 'bilangan', 'desimal', 'logika', 'daftar', 'peta'],
            'OPERATOR': ['dan', 'atau', 'bukan', 'dalam', 'adalah'],
            'MODUL': ['impor', 'dari', 'sbg'],
            'ERROR': ['coba', 'tangkapi', 'lontar'],
        }
        
        for category, keywords in categories.items():
            print(f"\n{category}:")
            for kw in keywords:
                if kw in KAMUS_INTI:
                    print(f"  {kw:15} → {KAMUS_INTI[kw]}")
        
        print("\n╚════════════════════════════════════════════╝\n")

def run_repl():
    """Entry point for REPL"""
    repl = PitonXREPL()
    repl.start()
