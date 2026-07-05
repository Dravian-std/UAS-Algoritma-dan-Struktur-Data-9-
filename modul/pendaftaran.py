import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from struktur_data.bst_pasien import BSTRekamMedis

class QueueAntrean:
    def __init__(self):
        self.antrean = []  # list kosong sebagai penyimpan antrean
    def enqueue(self, item):
        self.antrean.append(item)
    def dequeue(self):
        if self.is_empty():
            return None
        return self.antrean.pop(0)
    def is_empty(self):
        return len(self.antrean) == 0
    def size(self):
        return len(self.antrean)

class SistemPendaftaranKlinik:
    def __init__(self):
        self.antrean = QueueAntrean()      # antrean pasien yang baru datang
        self.rekam_medis = BSTRekamMedis()  # arsip permanen (BST)
    def daftarkan_ke_antrean(self, no_rm, nama, umur, keluhan):
        data_pasien = {
            "no_rm": no_rm,
            "nama": nama,
            "umur": umur,
            "keluhan": keluhan,
        }
        self.antrean.enqueue(data_pasien)
        print(f"[ANTREAN] Pasien '{nama}' (RM {no_rm}) masuk antrean. "
              f"Total mengantre: {self.antrean.size()}")
    def proses_pendaftaran(self):
        data_pasien = self.antrean.dequeue()
        if data_pasien is None:
            print("[INFO] Tidak ada pasien dalam antrean untuk diproses.")
            return None
        self.rekam_medis.insert(data_pasien["no_rm"], data_pasien)
        print(f"[REKAM MEDIS] Pasien '{data_pasien['nama']}' "
              f"(RM {data_pasien['no_rm']}) telah disimpan permanen ke BST.")
        return data_pasien
    def proses_semua_antrean(self):
        while not self.antrean.is_empty():
            self.proses_pendaftaran()
    def cari_pasien(self, no_rm):
        return self.rekam_medis.search(no_rm)
    def hapus_pasien(self, no_rm):
        self.rekam_medis.delete(no_rm)
    def tampilkan_semua_rekam_medis(self):
        return self.rekam_medis.inorder_traversal()
    def tinggi_tree(self):
        return self.rekam_medis.get_height()
    def jumlah_pasien_tersimpan(self):
        return self.rekam_medis.count_nodes()