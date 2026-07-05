class _NodeRiwayat:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._jumlah = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        node_baru = _NodeRiwayat(data)
        node_baru.next = self.top
        self.top = node_baru
        self._jumlah += 1

    def pop(self):
        if self.is_empty():
            print("Riwayat kosong, tidak ada tindakan yang bisa dibatalkan.")
            return None
        data_diambil = self.top.data
        self.top = self.top.next
        self._jumlah -= 1
        return data_diambil

    def peek(self):
        if self.is_empty():
            print("Riwayat kosong.")
            return None
        return self.top.data

    def display(self):
        if self.is_empty():
            print("Riwayat kosong.")
            return
        print("=== Riwayat Tindakan (terbaru -> terlama) ===")
        node_sekarang = self.top
        posisi = 1
        while node_sekarang is not None:
            print(f"{posisi}. {node_sekarang.data}")
            node_sekarang = node_sekarang.next
            posisi += 1

    def __len__(self):
        return self._jumlah