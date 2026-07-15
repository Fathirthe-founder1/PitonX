<p align="center">
  <img src="assets/pitonx.png" alt="PitonX Logo" width="120">
</p>

# Piton<font color="red">X</font> — Modifikasi Python

PitonX adalah bahasa pemrograman berbasis Python yang menggunakan sintaksis Bahasa Indonesia. Proyek ini dirancang khusus untuk mempermudah pemula, pelajar, dan developer di Indonesia dalam memahami logika pemrograman tanpa terkendala bahasa. PitonX juga mendukung **Dual Mode** yang memungkinkan Anda mencampur sintaks bahasa Indonesia dan Inggris secara fleksibel.

## 🚀 Instalasi

Pastikan Anda sudah menginstal Python dan `pip` di sistem Anda. Jalankan perintah berikut di terminal:

```bash
pip install PitonX
```

## 🛠️ Cara Pakai

Anda dapat menggunakan PitonX melalui CLI (Command Line Interface) atau mengisinya sebagai library di dalam kode Python.

### Melalui CLI
Jalankan file script PitonX (berekstensi `.px`) langsung dari terminal:
```bash
pitonx nama_file.px
```

### Melalui Library Python
Gunakan fungsi `run` dari modul `pitonx` untuk mengeksekusi string kode:
```python
import pitonx as px
px.run('ketik("Halo dari PitonX!")')
```

## 📖 Kamus PitonX → Python

Berikut adalah tabel padanan sintaksis lengkap dari PitonX ke Python standard:

| Kategori | PitonX | Python |
| :--- | :--- | :--- |
| **I/O** | ketik | print |
| | terima | input |
| | buka | open |
| | tutup | close |
| | baca | read |
| | tulis | write |
| | barisbaca | readline |
| | barisbacasemua | readlines |
| **Fungsi** | buat | def |
| | kembalikan | return |
| | wadah | class |
| | anon | lambda |
| | serahkan | yield |
| | inisial | init |
| | str | str |
| | repr | repr |
| **Logika** | jika | if |
| | jikalau | elif |
| | selain | else |
| | pasti | assert |
| **Loop** | selagi | while |
| | ulangi | for |
| | henti | break |
| | lanjut | continue |
| | lewat | pass |
| **Tipe Data** | teks | str |
| | bilangan | int |
| | desimal | float |
| | logika | bool |
| | daftar | list |
| | peta | dict |
| | panjang | len |
| | jenis | type |
| | rentang | range |
| **Boolean** | BENAR | True |
| | SALAH | False |
| | KOSONG | None |
| **Operator** | dan | and |
| | atau | or |
| | bukan | not |
| | dalam | in |
| | adalah | is |
| **Modul** | impor | import |
| | dari | from |
| | sbg | as |
| **Error** | coba | try |
| | tangkapi | except |
| | bersihkan | finally |
| | lontar | raise |
| **Math** | maks | max |
| | min | min |
| | total | sum |
| | urut | sorted |
| | abs | abs |
| | bulat | round |
| | pangkat | pow |
| **Khusus** | nama | name |
| | utama | main |

## 🧠 Mode Super Singkat

PitonX memiliki fitur **Mode Super Singkat** yang memungkinkan kamu menulis kode tanpa perlu mengetik `ketik()` setiap kali.

### Aturan:
1. Jika sebuah baris hanya berisi **string (teks dalam kutip)** atau **angka**, otomatis menjadi `ketik(...)`.
2. Jika baris mengandung `=`, `jika`, `selagi`, atau `buat`, baris tersebut **tidak akan diubah**.

### Contoh:

| Kamu ngetik ini | Sistem akan menjalankan ini |
|-----------------|------------------------------|
| `"Halo dunia"` | `ketik("Halo dunia")` |
| `'Halo'` | `ketik('Halo')` |
| `5 + 10` | `ketik(5 + 10)` |
| `nama = "Fathir"` | Tetap sebagai variabel |
| `jika x > 5:` | Tetap sebagai logika |
| `selagi benar:` | Tetap sebagai perulangan |

## ⚙️ Cara Kerja Sistem

Sistem penerjemahan PitonX bekerja melalui beberapa tahapan ringkas berikut:

1. **Input**: Pengguna menulis kode program menggunakan sintaksis PitonX.
2. **Translasi**: Sistem membaca kode tersebut dan menerjemahkannya ke kode Python standar menggunakan kamus pemetaan `PITON_MAP`.
3. **Eksekusi**: Kode Python hasil terjemahan dieksekusi secara real-time dan hasilnya dikembalikan sebagai output kepada pengguna.

## 📁 Struktur Folder

```text
PitonX/
├── pitonx/
│   ├── __init__.py
│   ├── core.py
│   ├── builtins.py
│   ├── cli.py
│   ├── repl.py
│   └── logo.py
├── setup.py
├── README.md
├── LICENSE
└── .gitignore
```

## 🙏 Kredit & Ucapan Terima Kasih

PitonX tidak akan terwujud tanpa peran dari pihak-pihak berikut:

| Peran | Kontribusi |
|------|------------|
| **Fathirthe-founder1**(gw)| Infrastruktur, cara kerja, sistem, logika penerjemahan, Mode Super Singkat, CLI, REPL, dan pengujian menyeluruh. |
| **DeepSeek AI** | Penyusunan folder, penulisan kode, debugging, optimasi, dan dokumentasi teknis. |
| **Komunitas Coding Indonesia** | Sumber inspirasi dan semangat untuk terus berkembang. |

---

> "Dreams will not be hindered by your weaknesses, dreams will only be hindered if you don't do it." — Fathir
