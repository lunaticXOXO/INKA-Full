import process.entity.LiniProduksi as proc
class Workstation():
    def __init__(self, id, nama, dibuat, berlaku):
        self.id = id
        self.nama = nama
        self.dibuat = dibuat
        self.berlaku = berlaku
        self.liniProduksi = proc.LiniProduksi()