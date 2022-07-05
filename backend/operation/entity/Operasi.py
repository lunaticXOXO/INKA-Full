import process.entity.Proses as proc
import workstation.entity.Workstation as ws
import product.entity.Produk as prod
class Operasi:
    def __init__(self, id, rencanaMulai, rencanaSelesai, mulai, selesai):
        self.id = id
        self.rencanaMulai = rencanaMulai
        self.rencanaSelesai = rencanaSelesai 
        self.mulai = mulai
        self.selesai = selesai
        self.process = proc.Proses()
        self.workstation = ws.Workstation()
        self.product = prod.Produk()
       