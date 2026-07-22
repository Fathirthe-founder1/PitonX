"""
PitonX REPL (Read-Eval-Print Loop)
Interactive console for PitonX
"""

import code
import sys
from pitonx.core import transpile, run
from pitonx.errors import PitonXError
from pitonx import __version__


class PitonXREPL:
    """
    Interactive REPL for PitonX
    """

    def __init__(self):
        self.namespace = {}
        self.console = code.InteractiveConsole(self.namespace)
        self.banner = self._get_banner()

    def _get_banner(self):
        """Get welcome banner for REPL"""
        return (
            f"PitonX {__version__} - Bahasa Pemrograman Indonesia\n"
            f"Python {sys.version}\n"
            f'Ketik "exit" atau "keluar" untuk keluar, "help()" untuk bantuan'
        )

    def _transpile_and_exec(self, source):
        """
        Transpile PitonX code and execute it in the console namespace
        
        Args:
            source (str): PitonX source code
            
        Returns:
            bool: True if executed successfully, False otherwise
        """
        try:
            # Check for exit commands
            if source.strip() in ('exit', 'keluar'):
                return False
            
            # Transpile
            python_code = transpile(source)
            
            # Execute in console namespace
            self.console.push(python_code)
            
            return True
        except PitonXError as e:
            print(f"❌ {e}", file=sys.stderr)
            return True
        except KeyboardInterrupt:
            print("\nDihentikan oleh pengguna", file=sys.stderr)
            return True
        except EOFError:
            return False
        except Exception as e:
            print(f"❌ Kesalahan: {e}", file=sys.stderr)
            return True

    def run(self):
        """
        Start the interactive REPL
        """
        print(self.banner)
        print()

        buffer = ""
        in_multiline = False

        while True:
            try:
                if in_multiline:
                    prompt = "... "
                else:
                    prompt = "piton> "

                line = input(prompt)

                buffer += line + "\n"

                # Check if we need to continue reading (for multiline statements)
                if line.rstrip().endswith(':'):
                    in_multiline = True
                    continue
                elif in_multiline and line and not line[0].isspace():
                    in_multiline = False
                elif in_multiline and not line.strip():
                    in_multiline = False

                # Execute buffer if not in multiline mode
                if not in_multiline:
                    if not self._transpile_and_exec(buffer.strip()):
                        print("\nTerima kasih telah menggunakan PitonX!")
                        break
                    buffer = ""

            except KeyboardInterrupt:
                print("\n\nDihentikan oleh pengguna (Ctrl+C)")
                buffer = ""
                in_multiline = False
            except EOFError:
                print("\n\nTerima kasih telah menggunakan PitonX!")
                break


def start_repl():
    """
    Start the PitonX REPL
    """
    repl = PitonXREPL()
    repl.run()
