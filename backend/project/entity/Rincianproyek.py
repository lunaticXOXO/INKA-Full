import project.entity.Proyek as proj
import product.entity.StrukturJenisProduk as sjprod
import product.entity.JenisProduk as jprod
class Rincianproyek():
    def __init__(self,id,quantity,dueDate):
        self.id = id
        self.quantity = quantity
        self.dueDate = dueDate           
        self.proyek = proj.Proyek()
        self.strukturJenisProduk = sjprod.StrukturJenisProduk()
        self.jenisProduk = jprod.JenisProduk()