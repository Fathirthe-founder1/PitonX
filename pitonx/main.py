"""
PitonX Command Line Interface
Entry point for pitonx command
"""
import sys
from pitonx.repl import start_repl
from pitonx.transpiler import transpile_file


def main():
    """Main entry point for pitonx command"""
    if len(sys.argv) < 2:
        print("PitonX - Python with Indonesian Syntax")
        print("\nUsage:")
        print("  pitonx <file.piton>    - Transpile and run PitonX file")
        print("  pitonx -h, --help      - Show this help message")
        sys.exit(1)
    
    if sys.argv[1] in ['-h', '--help']:
        print("PitonX - Python with Indonesian Syntax")
        print("\nUsage:")
        print("  pitonx <file.piton>    - Transpile and run PitonX file")
        print("  piton                  - Start interactive REPL mode")
        sys.exit(0)
    
    # Try to transpile and run the file
    try:
        transpile_file(sys.argv[1])
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def repl_main():
    """Main entry point for piton REPL command"""
    start_repl()


if __name__ == "__main__":
    main()
