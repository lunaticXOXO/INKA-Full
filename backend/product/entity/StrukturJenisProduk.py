import product.entity.JenisProduk as jnsProd
class StrukturJenisProduk():
    def __init__(self,idNodal,indukNodal,nama,jumlah,satuan):
        self.idNodal = idNodal
        self.indukNodal = indukNodal
        self.nama = nama
        self.jumlah = jumlah
        self.satuan = satuan
        self.jenisProduct = jnsProd.JenisProduk()
       
