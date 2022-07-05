from process.controller.ProsesController import *
from process.controller.LiniProduksiController import *
from product.controller.JenisProdukController import *
from product.controller.ProdukController import *
from product.controller.StrukturJenisProdukController import *
from project.controller.ProyekController import *
from workstation.controller.WorkstationController import *
from product.controller.JenisProdukController import *

def terminal():
    print("--------------")
    print("Fitur Aplikasi")
    print("--------------")
    print("1. Get List Proyek")
    print("2. Insert Proyek")
    print("3. Get List Produk")
    print("4. Insert Produk")
    print("5. Get List Rincian Proyek")
    print("6. Get List Jenis Produk")
    print("7. Insert Jenis Produk")
    print("8. Show Struktur Jenis Produk")
    print("9. Insert Struktur Jenis Produk")
    print("10. Get List Lini Produksi")
    print("11. Insert Lini Produksi")
    print("12. Stop Lini Produksi")
    print("13. Get List Workstation")
    print("14. Insert New Workstation")
    print("15. Show Proses")
    print("16. Insert New Proses")
    print("17. Hitung Durasi Proses")
    print("18. Hitung Durasi Rincian Proyek")
    print("19. Tampilkan Proses Terakhir")
    print("20. Tampilkan ID Jenis Produk")
 
    masukan = input("Input Pilihan : ")
    if masukan == "1":
        GetAllProyek()
    elif masukan == "2":
        AddProyek()
    elif masukan == "3":
        GetAllProduk()
    elif masukan == "4":
        AddProduk()
    elif masukan == "5":
        GetAllRincianProyek()
    elif masukan == "6":
        GetAllJenisProduk()
    elif masukan == "7":
        AddJenisProduct()
    elif masukan == "8":
        ShowStrukturJenisProduk()
    elif masukan == "9":
        AddStrukturJenisProduk()
    elif masukan == "10":
        GetAllLiniProduksi()
    elif masukan == "11":
        AddLiniProduksi()
    elif masukan == "12":
        StopLiniProduksi()
    elif masukan == "13":
        GetAllWorkstation()
    elif masukan == "14":
        AddWorkstation()
    elif masukan == "15":
        ShowProses()
    elif masukan == "16":
        AddProses()
    elif masukan == "17":
        HitungDurasiProses()
    elif masukan == "18":
        UpdateDueDateRProyek()
    elif masukan == "19":
        ShowLastProcessofProduct()
    elif masukan == "20":
        Get_ID_Jproduk()
    else:
        print("Input Tidak Sesuai!")

terminal()