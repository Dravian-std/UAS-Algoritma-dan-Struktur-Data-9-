def triase_pasien(bst_pasien, heap_prioritas, no_rm, prioritas, stack_riwayat):
    data_pasien = bst_pasien.search(no_rm)
    if data_pasien is None:
        print(f"[Triase] Pasien RM {no_rm} tidak ditemukan di data BST.")
        return False

    data_untuk_heap = {
        "no_rm": no_rm,
        "nama": data_pasien["nama"],
        "keluhan": data_pasien["keluhan"],
    }
    heap_prioritas.insert(prioritas, data_untuk_heap)
    stack_riwayat.push(f"TRIASE - RM {no_rm} - Prioritas {prioritas}")
    print(f"[Triase] {data_pasien['nama']} (RM {no_rm}) masuk antrean prioritas {prioritas}.")
    return True


def tangani_pasien_prioritas(heap_prioritas, stack_riwayat):
    pasien_ditangani = heap_prioritas.delete_root()
    if pasien_ditangani is None:
        return None

    prioritas, data = pasien_ditangani
    stack_riwayat.push(f"TANGANI - RM {data['no_rm']} - {data['nama']}")
    print(f"[Triase] Menangani pasien: {data['nama']} (Prioritas {prioritas}).")
    return pasien_ditangani
