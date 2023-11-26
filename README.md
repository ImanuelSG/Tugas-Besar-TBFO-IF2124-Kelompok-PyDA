# Tugas Besar TBFO IF2124
<p align="center">
    <h1 align="center">HTML PARSER WITH PUSHDOWN AUTOMATA</h3>
</p>
Tugas Besar IF 2124 Institut Teknologi Bandung Teori Bahasa Formal dan Otomata - HTML Checker dengan Pushdown Automata (PDA)

## Daftar Isi
1. [Informasi Umum](#informasi-umum)
2. [Teknologi yang Digunakan](#teknologi-yang-digunakan)
3. [Fitur](#fitur)
4. [Cara Menjalankan](#cara-menjalankan)
   - [Prasyarat](#prasyarat)
   - [Klon Repository](#klon-repository)
   - [Run Dengan Format](#Run sesuai format (python PDA.py {namafiletxtpda} {path-ke-filehtml}))
   

## Informasi Umum
Dalam pengembangan program, tahap parsing merupakan hal yang krusial di mana sintaks dari bahasa pemrograman diperiksa untuk memastikan bahwa itu sesuai dengan aturan bahasa tersebut. Hal ini dilakukan oleh para programmer untuk memastikan bahwa instruksi-instruksi tersebut sesuai dengan sintaks yang telah ditentukan oleh bahasa pemrograman tersebut.

Baik dalam bahasa yang diinterpretas maupun dikompilasi, pemeriksaan sintaks adalah praktik standar. Perbedaannya terletak pada langkah-langkah selanjutnya setelah proses pemeriksaan. Dalam suatu kompiler, setelah parsing, program diubah menjadi bentuk yang dapat dieksekusi, sementara dalam suatu interpreter, pemeriksaan sintaks dan eksekusi terjadi secara langsung tanpa langkah kompilasi tambahan.

## Penulis:
| NIM      | Nama                           | Pembagian Tugas  |
| -------- | -------------------------------| ---------------- |
| 13522048 | Angelica Kierra Ninta Gurning  | Diagram state    |
| 13522058 | Imanuel Sebastian Girsang      | PDA              |
| 13522060 | Andhita Naura Hariyanto        | Tokenizer, Bonus |

## Teknologi yang Digunakan
- Python 3.10.8

## Fitur
**HTML PDA Parser:**
   Parser HTML PDA (Pushdown Automaton) merupakan komponen krusial dari proyek ini. Dirancang untuk menganalisis dan memproses dokumen HTML menggunakan model pushdown automaton. Parser ini efisien menangani struktur hierarkis tag HTML, memastikan parsing dan ekstraksi informasi yang akurat dari file HTML.

   - *Tokenisasi:* Program ini mampu membuat token-token dari sebuah file HTML dan membuatnya menjadi string yang akan dicek pada PDA

   - *Pushdown Automata(PDA):* Program ini memiliki sebuah PDA yang dapat memroses input token dari tokenizer dan menentukan apakah struktur dan syntax yang ada benar atau salah

   - *Penanganan Error:* Parser ini memunculkan SyntaxError dengan pesan rinci jika menemui kesalahan sintaks.

## Cara Menjalankan

### Prasyarat
Sebelum memulai proses pengembangan, pastikan Anda telah menginstal perangkat lunak berikut di mesin Anda:

- [Python](https://www.python.org/) (3.6 atau yang lebih baru)

### 1. Klon Repository

```bash
git clone https://github.com/ImanuelSG/Tugas-Besar-TBFO-IF2124-Kelompok-PyDA.git
```
### 2. Run sesuai format (python PDA.py {namafiletxtpda} {path-ke-filehtml})

```bash
python PDA.py PDA.txt Test/tc11.html
```

