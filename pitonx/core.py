import re
from .builtins import PITON_MAP

def translate(code):
    lines = code.split('\n')
    for i in range(len(lines)):
        b = lines[i].strip()
        if b and not b.startswith('=') and not b.startswith('jika') and not b.startswith('selagi') and not b.startswith('buat'):
            if (b.startswith('"') and b.endswith('"')) or (b.startswith("'") and b.endswith("'")):
                lines[i] = f'ketik({b})'
            elif b.replace('.', '', 1).isdigit() or any(op in b for op in ['+', '-', '*', '/', '%']):
                if '=' not in b:
                    lines[i] = f'ketik({b})'
            elif b.endswith(';'):
                lines[i] = f'ketik({b[:-1]})'
    code = '\n'.join(lines)
    strings = []
    idx = 0
    def save_string(match):
        nonlocal idx
        strings.append(match.group(0))
        result = f'__S{idx}__'
        idx += 1
        return result
    code = re.sub(r'"[^"\\]*(\\.[^"\\]*)*"', save_string, code)
    code = re.sub(r"'[^'\\]*(\\.[^'\\]*)*'", save_string, code)
    sorted_keys = sorted(PITON_MAP.keys(), key=len, reverse=True)
    for key in sorted_keys:
        code = re.sub(r'\b' + re.escape(key) + r'\b', PITON_MAP[key], code)
    for i in range(len(strings)):
        code = code.replace(f'__S{i}__', strings[i])
    return code

def run_pitonx(code):
    python_code = translate(code)
    exec(python_code, {'__builtins__': __builtins__, 'print': print})
