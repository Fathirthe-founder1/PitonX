
<div align="center">

![PitonX](assets/pitonx.png)

# PitonX - Transpiler Python X

A lightweight Python-based transpiler that enables you to write Python code with Indonesian syntax.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Made with 🧠](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F%E2%80%8D%F0%9F%94%A5-red.svg)](https://github.com/Fathirthe-founder1)

</div>

---

## 🌟 Tentang PitonX

PitonX adalah transpiler Python yang memungkinkan Anda menulis code Python menggunakan syntax bahasa Indonesia. Proyek ini dirancang untuk membuat pemrograman lebih accessible bagi programmer Indonesia dan memfasilitasi pembelajaran programming dalam bahasa lokal.

**Fitur Utama:**
- ✅ Transpiler Python → Indonesian Syntax
- ✅ REPL Interactive Shell
- ✅ Library Python yang bisa diimpor
- ✅ CLI Terminal Commands
- ✅ Support untuk file `.px`
- ✅ Syntax yang intuitif dan mudah dipelajari

---

## 📦 Instalasi

### Menggunakan pip

```bash
pip install pitonx
```

### Clone dari GitHub

```bash
git clone https://github.com/Fathirthe-founder1/PitonX.git
cd PitonX
pip install -e .
```

---

## 🚀 Quick Start

### 1. REPL Interactive Mode

Untuk membuka shell interaktif PitonX:

```bash
piton
```

Output:
```
╔══════════════════════════════════════════╗
║  PitonX REPL - Interactive Shell        ║
║  Ketik 'keluar' untuk menutup           ║
╚══════════════════════════════════════════╝

x> ketik("Halo Dunia dari PitonX!")
Halo Dunia dari PitonX!

x> x = 10
•••

x> ketik(x)
10

x> keluar
Sampai jumpa! 👋
```

### 2. Menjalankan File `.px`

Buat file `program.px`:

```python
ketik("Halo Dunia!")
x = 5
jika x > 3:
    ketik("x lebih dari 3")
```

Jalankan dengan:

```bash
pitonx program.px
```

Output:
```
Halo Dunia!
x lebih dari 3
```

### 3. Menggunakan sebagai Library Python

```python
import pitonx as px

code = """
buat hitung_faktorial(n):
    jika n == 1:
        kembalikan 1
    kembalikan n * hitung_faktorial(n - 1)

hasil = hitung_faktorial(5)
ketik(hasil)
"""

px.run(code)
```

Output:
```
120
```

---

## 📚 Dokumentasi Lengkap

### A. Perintah CLI

| Perintah | Deskripsi |
|----------|----------|
| `pitonx` | Tampilkan tutorial |
| `pitonx --help` | Tampilkan bantuan |
| `piton` | Buka REPL interactive mode |
| `pitonx file.px` | Jalankan file PitonX |

### B. Kamus Lengkap (Dictionary)

#### INPUT / OUTPUT
| Indonesian | Python | Fungsi |
|-----------|--------|--------|
| `ketik` | `print` | Menampilkan output |
| `masukan` | `input` | Menerima input dari user |
| `buka` | `open` | Membuka file |
| `tutup` | `close` | Menutup file |
| `baca` | `read` | Membaca file |
| `tulis` | `write` | Menulis ke file |

#### FUNGSI & KELAS
| Indonesian | Python | Fungsi |
|-----------|--------|--------|
| `buat` | `def` | Mendefinisikan fungsi |
| `kembalikan` | `return` | Mengembalikan nilai dari fungsi |
| `wadah` | `class` | Mendefinisikan class |
| `anon` | `lambda` | Fungsi anonymous |
| `serahkan` | `yield` | Generator function |

#### KONTROL ALUR (CONDITIONAL)
| Indonesian | Python | Fungsi |
|-----------|--------|--------|
| `jika` | `if` | Kondisi jika |
| `jikalau` | `elif` | Kondisi alternatif |
| `selain` | `else` | Kondisi selain |
| `pasti` | `assert` | Assertion |

#### PERULANGAN (LOOPS)
| Indonesian | Python | Fungsi |
|-----------|--------|--------|
| `selagi` | `while` | Perulangan while |
| `ulangi` | `for` | Perulangan for |
| `henti` | `break` | Hentikan loop |
| `lanjut` | `continue` | Lanjutkan ke iterasi berikutnya |
| `lewat` | `pass` | Pass statement |

#### TIPE DATA
| Indonesian | Python | Fungsi |
|-----------|--------|--------|
| `teks` | `str` | String/Text |
| `bilangan` | `int` | Integer |
| `desimal` | `float` | Float |
| `logika` | `bool` | Boolean |
| `daftar` | `list` | List/Array |
| `peta` | `dict` | Dictionary |
| `panjang` | `len` | Panjang |
| `jenis` | `type` | Tipe data |
| `rentang` | `range` | Range |

#### BOOLEAN & SPECIAL VALUES
| Indonesian | Python | Fungsi |
|-----------|--------|--------|
| `BENAR` | `True` | Boolean true |
| `SALAH` | `False` | Boolean false |
| `KOSONG` | `None` | Null/None value |

#### OPERATOR LOGIKA
| Indonesian | Python | Fungsi |
|-----------|--------|--------|
| `dan` | `and` | Logical AND |
| `atau` | `or` | Logical OR |
| `bukan` | `not` | Logical NOT |
| `dalam` | `in` | Membership test |
| `adalah` | `is` | Identity test |

#### MODUL & IMPORT
| Indonesian | Python | Fungsi |
|-----------|--------|--------|
| `impor` | `import` | Import module |
| `dari` | `from` | Import from module |
| `sbg` | `as` | Alias untuk import |

#### ERROR HANDLING
| Indonesian | Python | Fungsi |
|-----------|--------|--------|
| `coba` | `try` | Try block |
| `tangkapi` | `except` | Except block |
| `lontar` | `raise` | Raise exception |

#### SCOPE & VARIABEL
| Indonesian | Python | Fungsi |
|-----------|--------|--------|
| `umum` | `global` | Global variable |
| `lokal` | `nonlocal` | Nonlocal variable |
| `hapus` | `del` | Delete variable |

#### MATEMATIKA & UTILITAS
| Indonesian | Python | Fungsi |
|-----------|--------|--------|
| `maks` | `max` | Maksimum |
| `min` | `min` | Minimum |
| `total` | `sum` | Jumlah total |
| `urut` | `sorted` | Sorting |
| `abs` | `abs` | Absolute value |
| `bulat` | `round` | Pembulatan |
| `pangkat` | `pow` | Perpangkatan |

---

### C. Contoh Penggunaan

#### 1. Hello World

**PitonX:**
```python
ketik("Halo Dunia dari PitonX!")
```

**Python Equivalent:**
```python
print("Halo Dunia dari PitonX!")
```

#### 2. Variabel & Tipe Data

**PitonX:**
```python
nama = "Fathir"
usia = 25
tinggi = 175.5
aktif = BENAR

ketik(nama)
ketik(usia)
ketik(tinggi)
ketik(aktif)
```

**Python Equivalent:**
```python
nama = "Fathir"
usia = 25
tinggi = 175.5
aktif = True

print(nama)
print(usia)
print(tinggi)
print(aktif)
```

#### 3. Kondisi If-Else

**PitonX:**
```python
nilai = 85

jika nilai >= 90:
    ketik("Grade A")
jikalau nilai >= 80:
    ketik("Grade B")
jikalau nilai >= 70:
    ketik("Grade C")
selain:
    ketik("Grade D")
```

**Python Equivalent:**
```python
nilai = 85

if nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
elif nilai >= 70:
    print("Grade C")
else:
    print("Grade D")
```

#### 4. Perulangan For

**PitonX:**
```python
ulangi i dalam rentang(1, 6):
    ketik(i)
```

**Python Equivalent:**
```python
for i in range(1, 6):
    print(i)
```

Output:
```
1
2
3
4
5
```

#### 5. Fungsi

**PitonX:**
```python
buat jumlah(a, b):
    kembalikan a + b

buat halo(nama):
    ketik("Halo, " + nama + "!")

hasil = jumlah(10, 20)
ketik(hasil)

halo("Fathir")
```

**Python Equivalent:**
```python
def jumlah(a, b):
    return a + b

def halo(nama):
    print("Halo, " + nama + "!")

hasil = jumlah(10, 20)
print(hasil)

halo("Fathir")
```

---

## 🏗️ Arsitektur Sistem

PitonX terdiri dari beberapa komponen utama:

```
pitonx/
├── __init__.py          # Entry point package
├── builtins.py          # Kamus Indonesian-Python dictionary
├── lexer.py             # Tokenizer untuk source code
├── parser.py            # Parser untuk membangun AST
├── transpiler.py        # Main transpiler (lexer + parser + codegen)
├── interpreter.py       # Executor untuk Python code
├── repl.py              # Interactive shell (REPL)
└── cli.py               # Command-line interface

setup.py                # Package configuration
README.md              # Documentation
LICENSE               # MIT License
assets/
├── pitonx.png         # Logo
```

### Alur Kerja (Workflow)

```
PitonX Source Code
        ↓
    LEXER (lexer.py)
    Tokenization
        ↓
    PARSER (parser.py)
    AST Generation
        ↓
    TRANSPILER (transpiler.py)
    Python Code Generation
        ↓
    INTERPRETER (interpreter.py)
    Execution
        ↓
    Output
```

---

## 🎮 REPL Interactive Commands

Dalam mode interactive (`piton`), Anda bisa menggunakan perintah khusus:

| Perintah | Deskripsi |
|----------|----------|
| `keluar` / `exit` | Keluar dari REPL |
| `bantuan` | Tampilkan bantuan |
| `kamus` | Tampilkan kamus lengkap |

**Contoh:**

```
x> bantuan
[Menampilkan bantuan]

x> kamus
[Menampilkan kamus lengkap]

x> x = 10
•••

x> ketik(x)
10

x> keluar
Sampai jumpa! 👋
```

---

## 💻 Python Library API

### Import PitonX

```python
import pitonx as px
```

### Method: `run(code, variables=None)`

Menjalankan code PitonX dan mengembalikan result.

**Parameter:**
- `code` (str): Source code PitonX
- `variables` (dict): Optional, variabel yang diinjeksi

**Return:**
- Dictionary dari environment execution

**Contoh:**

```python
import pitonx as px

code = """
x = 10
y = 20
total = x + y
ketik(total)
"""

px.run(code)
```

### Method: `transpile(code)`

Transpile code PitonX ke Python.

**Parameter:**
- `code` (str): Source code PitonX

**Return:**
- str: Python source code

**Contoh:**

```python
import pitonx as px

pitonx_code = "ketik('Halo Dunia')"
python_code = px.transpile(pitonx_code)
print(python_code)
# Output: print('Halo Dunia')
```

---

## 🧪 Testing

```bash
python -m pytest tests/
```

---

## 🤝 Kontribusi

Kami menerima kontribusi! Untuk berkontribusi:

1. Fork repository
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buka Pull Request

---

## 📝 Lisensi

Proyek ini dilisensikan di bawah MIT License - lihat file [LICENSE](LICENSE) untuk detail.

---

## 👨‍💻 Author

**Jameson AlFathir Void**

- GitHub: [@Fathirthe-founder1](https://github.com/Fathirthe-founder1)
- Email: fathirthefound@example.com

---

## 🙏 Terima Kasih

Terima kasih kepada semua kontributor dan pengguna PitonX!

---

## 📞 Support & Feedback

Jika Anda menemukan bug atau punya saran:

1. Buka [GitHub Issues](https://github.com/Fathirthe-founder1/PitonX/issues)
2. Jelaskan masalah atau fitur yang diinginkan
3. Kami akan merespons sesegera mungkin

---

<div align="center">

**Made with 🧠 by Jameson AlFathir Void**

⭐ Jika project ini membantu Anda, jangan lupa kasih bintang! ⭐

</div>
