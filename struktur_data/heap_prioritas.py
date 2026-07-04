class BinaryHeap:
    def __init__(self):
        self._heap = []

    def is_empty(self):
        return len(self._heap) == 0

    def size(self):
        return len(self._heap)

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def insert(self, prioritas, data):
        """Menambahkan pasien baru ke heap sesuai prioritas. O(log n)."""
        self._heap.append((prioritas, data))
        self._heapify_up(len(self._heap) - 1)
        return True

    def _heapify_up(self, i):
        while i > 0 and self._heap[i][0] < self._heap[self._parent(i)][0]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def delete_root(self):
        """Mengeluarkan pasien dengan prioritas tertinggi. O(log n)."""
        if self.is_empty():
            print("[Heap] Tidak ada pasien dalam antrean prioritas.")
            return None
        root = self._heap[0]
        elemen_terakhir = self._heap.pop()
        if not self.is_empty():
            self._heap[0] = elemen_terakhir
            self._heapify_down(0)
        return root

    def _heapify_down(self, i):
        n = len(self._heap)
        while True:
            kiri = self._left(i)
            kanan = self._right(i)
            terkecil = i
            if kiri < n and self._heap[kiri][0] < self._heap[terkecil][0]:
                terkecil = kiri
            if kanan < n and self._heap[kanan][0] < self._heap[terkecil][0]:
                terkecil = kanan
            if terkecil == i:
                break
            self._swap(i, terkecil)
            i = terkecil

    def peek(self):
        """Melihat pasien prioritas tertinggi tanpa mengeluarkannya."""
        if self.is_empty():
            print("[Heap] Antrean prioritas kosong.")
            return None
        return self._heap[0]

    def display(self):
        if self.is_empty():
            print("[Heap] Belum ada pasien dalam antrean prioritas.")
            return
        label_prioritas = {
            1: "Gawat Darurat", 2: "Mendesak", 3: "Sedang",
            4: "Ringan", 5: "Tidak Mendesak",
        }
        print("\n=== ANTREAN PRIORITAS PENANGANAN (Min-Heap) ===")
        for i, (prioritas, data) in enumerate(self._heap):
            label = label_prioritas.get(prioritas, "Tidak diketahui")
            print(f"[{i}] Prioritas {prioritas} ({label}) - {data}")
        print("=" * 50)
