import product.entity.Produk as prod
import process.entity.Proses as proc
class Proses():
    def __init__(self,id,nama,durasi,satuanDurasi):
        self.id = id
        self.nama = nama
        self.durasi = durasi
        self.satuanDurasi = satuanDurasi
        self.nodalOutput = prod.Produk() 
        self.prosesSebelumnya = proc.Proses()
        