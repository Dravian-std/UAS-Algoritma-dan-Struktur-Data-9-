class _NodeAntrian:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._jumlah = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        node_baru = _NodeAntrian(data)
        if self.is_empty():
            self.front = node_baru
            self.rear = node_baru
        else:
            self.rear.next = node_baru
            self.rear = node_baru
        self._jumlah += 1

    def dequeue(self):
        if self.is_empty():
            print("Antrean kosong, tidak ada pasien yang bisa diproses.")
            return None
        data_diambil = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._jumlah -= 1
        return data_diambil

    def peek(self):
        if self.is_empty():
            print("Antrean kosong.")
            return None
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Antrean kosong.")
            return
        print("=== Isi Antrean (depan -> belakang) ===")
        node_sekarang = self.front
        posisi = 1
        while node_sekarang is not None:
            print(f"{posisi}. {node_sekarang.data}")
            node_sekarang = node_sekarang.next
            posisi += 1

    def __len__(self):
        return self._jumlah