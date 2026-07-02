"""
SIKLINIK - Sistem Antrean & Rekam Medis Klinik
=================================================
Program Utama (Entry Point)

Integrasi struktur data:
    Queue        -> Antrean kedatangan pasien
    BST          -> Penyimpanan & pencarian data pasien (kunci: No. RM)
    Binary Heap  -> Penentuan prioritas penanganan pasien
    Stack        -> Riwayat tindakan / undo

Jalankan file ini langsung, atau salin seluruh isi project ke dalam
satu file Google Colab (.ipynb) sesuai ketentuan pengumpulan.
"""

from struktur_data.queue_antrian import Queue
from struktur_data.stack_riwayat import Stack
from struktur_data.bst_pasien import BST
from struktur_data.heap_prioritas import BinaryHeap

from modul.pendaftaran import (
    daftarkan_ke_antrean,
    proses_pendaftaran,
    cari_pasien,
    hapus_pasien,
)
from modul.triase import triase_pasien, tangani_pasien_prioritas
from modul.riwayat import tampilkan_riwayat, batalkan_tindakan_terakhir


# ---------------------- INISIALISASI STRUKTUR DATA ----------------------
queue_pendaftaran = Queue()
bst_pasien = BST()
heap_prioritas = BinaryHeap()
stack_riwayat = Stack()

no_rm_counter = 1000  # penomoran otomatis No. Rekam Medis


def cetak_menu():
    print("\n" + "=" * 55)
    print("     SIKLINIK - SISTEM ANTREAN & REKAM MEDIS KLINIK")
    print("=" * 55)
    print("1.  Tambah pasien ke antrean pendaftaran (Queue)")
    print("2.  Proses pendaftaran pasien terdepan (Queue -> BST)")
    print("3.  Tampilkan antrean pendaftaran")
    print("4.  Cari data pasien (BST)")
    print("5.  Hapus data pasien (BST)")
    print("6.  Tampilkan seluruh data pasien (BST - Inorder)")
    print("7.  Triase / atur prioritas pasien (BST -> Heap)")
    print("8.  Tangani pasien prioritas tertinggi (Heap)")
    print("9.  Tampilkan antrean prioritas (Heap)")
    print("10. Tampilkan riwayat tindakan (Stack)")
    print("11. Batalkan tindakan terakhir / Undo (Stack)")
    print("0.  Keluar")
    print("=" * 55)


def main():
    global no_rm_counter

    while True:
        cetak_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            nama = input("Nama pasien   : ").strip()
            keluhan = input("Keluhan       : ").strip()
            daftarkan_ke_antrean(queue_pendaftaran, nama, keluhan)

        elif pilihan == "2":
            no_rm_counter += 1
            hasil = proses_pendaftaran(
                queue_pendaftaran, bst_pasien, no_rm_counter, stack_riwayat
            )
            if hasil is None:
                no_rm_counter -= 1  # rollback nomor jika gagal/kosong

        elif pilihan == "3":
            queue_pendaftaran.display()

        elif pilihan == "4":
            try:
                rm = int(input("Masukkan No. RM: "))
                data = cari_pasien(bst_pasien, rm)
                if data:
                    print(f"[Ditemukan] RM {rm}: {data}")
            except ValueError:
                print("No. RM harus berupa angka.")

        elif pilihan == "5":
            try:
                rm = int(input("Masukkan No. RM yang akan dihapus: "))
                hapus_pasien(bst_pasien, rm, stack_riwayat)
            except ValueError:
                print("No. RM harus berupa angka.")

        elif pilihan == "6":
            bst_pasien.display()

        elif pilihan == "7":
            try:
                rm = int(input("No. RM pasien   : "))
                print("Skala Prioritas -> 1: Gawat Darurat, 2: Mendesak, "
                      "3: Sedang, 4: Ringan, 5: Tidak Mendesak")
                prioritas = int(input("Tingkat prioritas (1-5): "))
                triase_pasien(bst_pasien, heap_prioritas, rm, prioritas, stack_riwayat)
            except ValueError:
                print("Input harus berupa angka.")

        elif pilihan == "8":
            tangani_pasien_prioritas(heap_prioritas, stack_riwayat)

        elif pilihan == "9":
            heap_prioritas.display()

        elif pilihan == "10":
            tampilkan_riwayat(stack_riwayat)

        elif pilihan == "11":
            batalkan_tindakan_terakhir(stack_riwayat)

        elif pilihan == "0":
            print("Terima kasih telah menggunakan SIKLINIK.")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()
