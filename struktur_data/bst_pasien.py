class NodePasien:
    def __init__(self, no_rm, data):
        self.no_rm = no_rm      # key/kunci BST
        self.data = data        # payload: dict data pasien
        self.left = None
        self.right = None
class BSTRekamMedis:  
    def __init__(self):
        self.root = None  # tree kosong di awal
    def insert(self, no_rm, data):
        if self.root is None:
            self.root = NodePasien(no_rm, data)
            return
        self.root = self._insert_rec(self.root, no_rm, data)
    def _insert_rec(self, node, no_rm, data):
        if node is None:
            return NodePasien(no_rm, data)

        if no_rm < node.no_rm:
            node.left = self._insert_rec(node.left, no_rm, data)
        elif no_rm > node.no_rm:
            node.right = self._insert_rec(node.right, no_rm, data)
        else:
            node.data = data
        return node
    def search(self, no_rm):
        node = self._search_rec(self.root, no_rm)
        return node.data if node else None
    def _search_rec(self, node, no_rm):
        if node is None or node.no_rm == no_rm:
            return node
        if no_rm < node.no_rm:
            return self._search_rec(node.left, no_rm)
        return self._search_rec(node.right, no_rm)
    def delete(self, no_rm):
        self.root = self._delete_rec(self.root, no_rm)
    def _delete_rec(self, node, no_rm):
        if node is None:
            return None
        if no_rm < node.no_rm:
            node.left = self._delete_rec(node.left, no_rm)
        elif no_rm > node.no_rm:
            node.right = self._delete_rec(node.right, no_rm)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = self._cari_terkecil(node.right)
            node.no_rm = successor.no_rm
            node.data = successor.data
            node.right = self._delete_rec(node.right, successor.no_rm)
        return node
    def _cari_terkecil(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def inorder_traversal(self):
        hasil = []
        self._inorder_rec(self.root, hasil)
        return hasil
    def _inorder_rec(self, node, hasil):
        if node is not None:
            self._inorder_rec(node.left, hasil)       # kunjungi kiri
            hasil.append((node.no_rm, node.data))      # kunjungi root
            self._inorder_rec(node.right, hasil)       # kunjungi kanan
    def get_height(self):
        return self._height_rec(self.root)
    def _height_rec(self, node):
        if node is None:
            return -1
        tinggi_kiri = self._height_rec(node.left)
        tinggi_kanan = self._height_rec(node.right)
        return 1 + max(tinggi_kiri, tinggi_kanan)
    def count_nodes(self):
        return self._count_rec(self.root)
    def _count_rec(self, node):
        if node is None:
            return 0
        return 1 + self._count_rec(node.left) + self._count_rec(node.right)
    
# if __name__ == "__main__":
#     bst = BSTRekamMedis()
#     bst.insert(1050, {"nama": "Andi", "umur": 30, "diagnosa": "Flu"})
#     bst.insert(1020, {"nama": "Budi", "umur": 25, "diagnosa": "Demam"})
#     bst.insert(1080, {"nama": "Citra", "umur": 40, "diagnosa": "Batuk"})
#     bst.insert(1010, {"nama": "Dewi", "umur": 22, "diagnosa": "Migrain"})
#     print("In-order (terurut No. RM):")
#     for no_rm, data in bst.inorder_traversal():
#         print(f"  RM {no_rm}: {data}")
#     print("Tinggi tree :", bst.get_height())
#     print("Jumlah node :", bst.count_nodes())
#     print("Cari RM 1020:", bst.search(1020))
#     bst.delete(1020)
#     print("Setelah hapus RM 1020:")
#     for no_rm, data in bst.inorder_traversal():
#         print(f"  RM {no_rm}: {data}")