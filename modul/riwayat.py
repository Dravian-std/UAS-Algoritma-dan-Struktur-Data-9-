from struktur_data.stack_riwayat import Stack

def catat_tindakan(stack_riwayat: Stack, deskripsi: str):
    stack_riwayat.push(deskripsi)

def tampilkan_riwayat(stack_riwayat: Stack):
    print("\n--- RIWAYAT TINDAKAN SISTEM ---")
    stack_riwayat.display()

def batalkan_tindakan_terakhir(stack_riwayat: Stack):
    tindakan_dibatalkan = stack_riwayat.pop()

    if tindakan_dibatalkan is None:
        # Stack.pop() sudah mencetak pesan "riwayat kosong",
        # jadi di sini cukup dikembalikan None.
        return None

    print(f"Tindakan berhasil dibatalkan (undo): {tindakan_dibatalkan}")
    return tindakan_dibatalkan