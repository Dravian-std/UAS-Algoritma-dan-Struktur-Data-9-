def daftarkan_ke_antrean(queue, nama, keluhan):
    data_pasien = {"nama": nama, "keluhan": keluhan}
    queue.enqueue(data_pasien)
    print(f"[ANTREAN] Pasien '{nama}' masuk antrean. Total mengantre: {len(queue)}")


def proses_pendaftaran(queue, bst, no_rm, stack_riwayat):
    data_pasien = queue.dequeue()
    if data_pasien is None:
        print("[INFO] Tidak ada pasien dalam antrean untuk diproses.")
        return None

    data_pasien["no_rm"] = no_rm
    bst.insert(no_rm, data_pasien)
    stack_riwayat.push(("daftar", no_rm, data_pasien))

    print(f"[REKAM MEDIS] Pasien '{data_pasien['nama']}' (RM {no_rm}) disimpan ke BST.")
    return data_pasien


def cari_pasien(bst, no_rm):
    return bst.search(no_rm)


def hapus_pasien(bst, no_rm, stack_riwayat):
    data_lama = bst.search(no_rm)
    if data_lama is None:
        print(f"[INFO] RM {no_rm} tidak ditemukan.")
        return
    bst.delete(no_rm)
    stack_riwayat.push(("hapus", no_rm, data_lama))
    print(f"[HAPUS] Data RM {no_rm} berhasil dihapus.")