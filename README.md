# UJIAN AKHIR SEMESTER (UAS)
## Algoritma dan Struktur Data

---

**Program Studi**: S1 Pendidikan Teknik Informatika dan Komputer
**Fakultas**: Keguruan dan Ilmu Pendidikan
**Universitas**: Sebelas Maret

---

### Kelompok 9

| No | Nama | NIM |
|----|------|-----|
| 1  | Dafa Syahrul Syah | [NIM] |
| 2  | Danang Rafli  | K3525054  |
| 3  | Faris Rafiuddin Hannan  | K3525058 |

---

### Judul Proyek
Implementasi Struktur Data pada Studi Kasus Klinik

### Studi Kasus
Sistem Antrean dan Rekam Medis Klinik

### Struktur Data yang Digunakan
- Queue
- Stack
- Binary Search Tree (BST)
- Binary Heap

### Cara Menjalankan
Program dijalankan melalui Google Colab (.ipynb) dan berbasis Command Line Interface (CLI).

1. Buka file notebook pada folder `notebook/`
2. Jalankan seluruh cell secara berurutan

## 📂 Struktur Folder

```
siklinik/
├── 📄 README.md
├── 📄 main.py                      # Entry point aplikasi 
│
├── 📁 struktur_data/               # Implementasi murni struktur data
│   ├── __init__.py
│   ├── queue_antrian.py            # Class Queue
│   ├── stack_riwayat.py            # Class Stack
│   ├── bst_pasien.py               # Class BST + Node
│   └── heap_prioritas.py           # Class BinaryHeap
│
├── 📁 modul/                       # Logika proses bisnis
│   ├── pendaftaran.py              # Modul pendaftaran (Queue + BST)
│   ├── triase.py                   # Modul prioritas (Heap)
│   └── riwayat.py                  # Modul riwayat/undo (Stack)
│
├── 📁 notebook/
│   └── UAS_AlgStruk_Kelompok3.ipynb   
│
├── 📁 laporan/
│   └── Laporan_UAS_Kelompok3.pdf
│
├── 📁 docs/
│   └── diagram_alur_bisnis.png
│
└── 📄 .gitignore

**Mata Kuliah Algoritma dan Struktur Data — 2026**
