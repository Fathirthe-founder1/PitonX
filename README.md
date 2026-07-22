<p align="center">
  <img src="assets/pitonx.png" alt="PitonX Logo" width="120">
</p>

# PitonX - Bahasa Pemrograman Indonesia

> "Dreams will not be hindered by your weaknesses, dreams will only be hindered if you don't do it." — Fathir

PitonX adalah bahasa pemrograman dengan kata kunci berbahasa Indonesia yang dikompilasi ke Python. Dirancang dengan arsitektur yang terstruktur (Lexer → Parser → Transpiler) untuk memberikan pengalaman pemrograman yang intuitif dan mudah dipelajari bagi penutur bahasa Indonesia.

## 🌟 Fitur Utama

- **Kata Kunci Bahasa Indonesia** - Gunakan bahasa Indonesia untuk menulis kode
- **Transpilasi ke Python** - Kode PitonX dikompilasi langsung ke Python yang valid
- **REPL Interaktif** - Mode interaktif untuk eksperimen dan pembelajaran
- **Arsitektur Terstruktur** - Lexer, Parser, dan Transpiler yang modular
- **Library Support** - Gunakan PitonX sebagai library dalam proyek Python Anda
- **Error Handling** - Pesan kesalahan yang jelas dan informatif dalam Bahasa Indonesia

## 📥 Instalasi

### Via pip (Rekomendasi)

```bash
pip install pitonx
```

### Dari Source

```bash
git clone https://github.com/Fathirthe-founder1/PitonX.git
cd PitonX
pip install -e .
```

## 🚀 Penggunaan

### Mode REPL Interaktif

```bash
# Masuk ke REPL interaktif
piton
```

Contoh di REPL:
```
piton> bilangan = 5
piton> ketik(bilangan)
5
piton> keluar
```

### Menjalankan File .px

```bash
pitonx program.px
```

Contoh file `program.px`:
```pitonx
ketik("Halo, Dunia!")
angka = 42
ketik(angka)
```

### Melihat Kamus Kata Kunci

```bash
pitonx --kamusx
```

Ini akan menampilkan daftar lengkap kata kunci PitonX dan artinya:

```
✓ Kamus Kata Kunci PitonX
════════════════════════════════════════

OUTPUT & INPUT:
  ketik          →  print
  masukan        →  input

FUNGSI & KONTROL ALUR:
  buat           →  def
  kembalikan     →  return
  jika           →  if
  jikalau        →  elif
  selain         →  else

LOOP:
  selagi         →  while
  ulangi         →  for
  henti          →  break
  lanjut         →  continue

... dan banyak lagi!
```

### Transpilasi ke Python

Untuk melihat kode Python yang dihasilkan:

```bash
pitonx --transpile program.px
```

### Bantuan Perintah

```bash
pitonx --help
```

### Versi

```bash
pitonx --version
```

## 📚 Penggunaan Sebagai Library

Gunakan PitonX dalam kode Python Anda:

### Transpilasi Kode

```python
from pitonx import transpile

code_pitonx = """
ketik("Halo dari library PitonX!")
angka = 10
ketik(angka * 2)
"""

python_code = transpile(code_pitonx)
print(python_code)
```

### Menjalankan Kode

```python
from pitonx import run

code_pitonx = """
buat hitung_jumlah(a, b):
    kembalikan a + b

hasil = hitung_jumlah(5, 3)
ketik(hasil)
"""

namespace = run(code_pitonx)
print(namespace)
```

### Menggunakan Lexer, Parser, dan Transpiler Secara Terpisah

```python
from pitonx.lexer import Lexer
from pitonx.parser import Parser
from pitonx.transpiler import Transpiler

code = "ketik('Hello')"

# Tokenize
lexer = Lexer(code)
tokens = lexer.get_tokens()

# Parse
parser = Parser(tokens)
ast = parser.parse()

# Transpile
transpiler = Transpiler(ast)
python_code = transpiler.transpile()

print(python_code)
```

## 📖 Kamus Kata Kunci PitonX

### Output & Input

| PitonX | Python | Fungsi |
|--------|--------|--------|
| `ketik` | `print` | Cetak ke layar |
| `masukan` | `input` | Masukkan dari pengguna |

### Fungsi & Kontrol Alur

| PitonX | Python | Fungsi |
|--------|--------|--------|
| `buat` | `def` | Definisikan fungsi |
| `kembalikan` | `return` | Kembalikan nilai |
| `jika` | `if` | Kondisi jika |
| `jikalau` | `elif` | Kondisi jika tidak |
| `selain` | `else` | Kondisi selainnya |

### Loop

| PitonX | Python | Fungsi |
|--------|--------|--------|
| `selagi` | `while` | Loop selama |
| `ulangi` | `for` | Loop ulangi |
| `henti` | `break` | Henti loop |
| `lanjut` | `continue` | Lanjut iterasi berikutnya |

### Tipe Data

| PitonX | Python | Fungsi |
|--------|--------|--------|
| `teks` | `str` | String/Teks |
| `bilangan` | `int` | Integer/Bilangan bulat |
| `desimal` | `float` | Float/Desimal |
| `logika` | `bool` | Boolean/Logika |
| `daftar` | `list` | List/Daftar |
| `peta` | `dict` | Dictionary/Peta |

### Fungsi Bawaan

| PitonX | Python | Fungsi |
|--------|--------|--------|
| `panjang` | `len` | Panjang/Jumlah elemen |
| `rentang` | `range` | Rentang angka |

### Konstanta

| PitonX | Python | Fungsi |
|--------|--------|--------|
| `BENAR` | `True` | Benar |
| `SALAH` | `False` | Salah |
| `KOSONG` | `None` | Kosong/Tidak ada |

### Operator Logika

| PitonX | Python | Fungsi |
|--------|--------|--------|
| `dan` | `and` | Dan logika |
| `atau` | `or` | Atau logika |
| `bukan` | `not` | Bukan logika |

### Import & Modul

| PitonX | Python | Fungsi |
|--------|--------|--------|
| `impor` | `import` | Impor modul |
| `dari` | `from` | Dari modul |
| `sbg` | `as` | Sebagai alias |

### Exception Handling

| PitonX | Python | Fungsi |
|--------|--------|--------|
| `coba` | `try` | Coba eksekusi |
| `tangkapi` | `except` | Tangkap exception |
| `lontar` | `raise` | Lontar exception |

## 📝 Contoh Program

### 1. Program Sederhana

**File: `hello.px`**

```pitonx
ketik("Halo, Dunia!")
nama = masukan("Siapa nama Anda? ")
ketik("Halo, " + nama + "!")
```

### 2. Fungsi dan Loop

**File: `faktorial.px`**

```pitonx
buat hitung_faktorial(n):
    jika n == 0:
        kembalikan 1
    selain:
        kembalikan n * hitung_faktorial(n - 1)

hasil = hitung_faktorial(5)
ketik("Faktorial 5 adalah: " + teks(hasil))
```

### 3. Loop dan Kondisi

**File: `tabel_perkalian.px`**

```pitonx
ulangi i dalam rentang(1, 11):
    ulangi j dalam rentang(1, 11):
        ketik(i * j, " ", akhir="")
    ketik()
```

### 4. List dan Dictionary

**File: `data.px`**

```pitonx
daftar_angka = [1, 2, 3, 4, 5]
ketik("List: ", daftar_angka)
ketik("Panjang: ", panjang(daftar_angka))

data_siswa = {
    "nama": "Budi",
    "umur": 20,
    "nilai": 85
}

ketik("Nama: ", data_siswa["nama"])
ketik("Nilai: ", data_siswa["nilai"])
```

## 🔧 Perintah CLI Lengkap

```
PitonX 8.0.3 - Bahasa Pemrograman Indonesia

Penggunaan:
  piton                    Masuk ke REPL interaktif
  pitonx FILE              Jalankan file .px
  pitonx --help            Tampilkan pesan bantuan
  pitonx --version         Tampilkan versi PitonX
  pitonx --transpile FILE  Tampilkan kode Python yang dihasilkan
  pitonx --kamusx          Tampilkan daftar kamus kata kunci

Contoh:
  pitonx program.px
  pitonx --transpile program.px
  pitonx --kamusx
  piton
```

## 🏗️ Arsitektur Sistem

PitonX memiliki arsitektur 3 lapisan:

```
┌─────────────────────────────────┐
│    Input: Kode PitonX           │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│    LEXER (Tokenizer)            │
│  Memecah kode menjadi token     │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│    PARSER (AST Generator)       │
│  Konversi token ke AST          │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│    TRANSPILER (Code Generator)  │
│  Konversi AST ke Python         │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│   Output: Kode Python Valid     │
└─────────────────────────────────┘
```

## 🐛 Troubleshooting

### Import Error

Jika mendapat error `ModuleNotFoundError: No module named 'pitonx'`, pastikan PitonX sudah diinstal:

```bash
pip install --upgrade pitonx
```

### File Not Found

Pastikan file .px berada di direktori yang benar:

```bash
ls -la program.px
pitonx program.px
```

### Syntax Error

Periksa kamus kata kunci dengan:

```bash
pitonx --kamusx
```

## 📚 Dokumentasi Lengkap

Untuk dokumentasi lebih lengkap, kunjungi:
- GitHub: https://github.com/Fathirthe-founder1/PitonX
- Issues: https://github.com/Fathirthe-founder1/PitonX/issues

## 📄 Lisensi

PitonX dirilis di bawah lisensi MIT. Silakan lihat file `LICENSE` untuk detail lebih lanjut.

## 👤 Penulis

**Jameson AlFathir Void (Fathirthe-founder1)**

- GitHub: [@Fathirthe-founder1](https://github.com/Fathirthe-founder1)

---

## 💡 Berkontribusi

Kontribusi sangat dipersilakan! Untuk berkontribusi:

1. Fork repository ini
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 🙏 Terima Kasih

Terima kasih telah menggunakan PitonX! Semoga bahasa pemrograman ini membuat pembelajaran dan pengembangan lebih mudah.

---

## DISCLAIMER💡

> **Proyek ini hanya Hobi,Eksperimen,Iseng saja,jika ada yang mau mengembangkan,maka silahkan**

# CREDIT🤝

**Author**: Fathirthe-founder1 
**Assistant**: Deepseek
