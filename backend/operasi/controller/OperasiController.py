from numpy import record
import db.db_handler as database
from flask import request,make_response,jsonify
import random
import string
from product.controller.ProdukController import *
import datetime

def ShowOperasiFromProduct(idProduct):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.id,a.proses,b.nama,a.stasiunKerja,a.rencanaMulai,a.rencanaSelesai FROM prd_d_operasi a JOIN prd_r_proses b ON b.id = a.proses WHERE produk = '"+idProduct+"' ORDER BY proses,rencanaMulai ASC"
    cursor.execute(query)

    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)


def ShowProductInOperasi(id_product):
    conn = database.connector()
    cursor = conn.cursor()
    rencana_mulai_min = ""

    query_min = "SELECT MIN(a.rencanaMulai) FROM prd_d_operasi a"
    cursor.execute(query_min)
    records = cursor.fetchall()
    for data in records:
        rencana_mulai_min = data[0]
        rencana_mulai_min = str(rencana_mulai_min)
    print(rencana_mulai_min)

    query = "SELECT a.id,a.rencanaMulai, b.id AS 'idProduk',b.dueDate AS 'dueDateProduk', c.id AS 'idRincian',c.jumlah,c.dueDate AS 'dueDateRincian', d.id AS 'idProyek', d.nama AS 'namaProyek', e.id AS 'idCustomer', e.nama AS 'namaCustomer' FROM prd_d_operasi a JOIN prd_d_produk b ON b.id = a.produk JOIN prd_r_rincianproyek c ON c.id = b.rincianProyek JOIN prd_r_proyek d ON d.id = c.proyek JOIN gen_r_customer e ON e.id = d.customerid WHERE a.produk = '"+id_product+"' AND a.rencanaMulai = '"+rencana_mulai_min+"'"
    cursor.execute(query)
    records_query = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records_query:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)

def PantauOperasi(idProduct):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.id AS 'idOperasi',a.rencanaMulai,a.rencanaSelesai,b.id AS 'idProses',b.nama AS 'namaProses',a.produk FROM prd_d_operasi a JOIN prd_r_proses b ON b.id = a.proses JOIN prd_r_strukturjnsprd d ON d.idNodal = b.nodalOutput JOIN prd_r_jenisproduk e ON e.id = d.jnsProduk JOIN prd_r_rincianproyek f ON f.jenisProduk = e.id JOIN prd_r_proyek g ON g.id = f.proyek JOIN prd_d_produk h ON h.rincianProyek = f.id WHERE h.id = '"+idProduct+"' ORDER BY a.proses,a.rencanaMulai ASC"
    cursor.execute(query)

    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)

def GetProcessofProduct(idProduk):
    conn = database.connector()
    cursor = conn.cursor()
    query2 = "SELECT a.id FROM prd_r_proses a JOIN prd_r_strukturjnsprd b ON b.idNodal = a.nodalOutput JOIN prd_r_jenisproduk c ON c.id = b.jnsProduk JOIN prd_r_rincianproyek d ON d.jenisProduk = c.id JOIN prd_r_proyek e ON e.id = d.proyek JOIN prd_d_produk f ON f.rincianProyek = d.id WHERE f.id = '"+idProduk+"'"
    cursor.execute(query2)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records:
        json_data.append(dict(zip(row_headers,data)))    
    
    return make_response(jsonify(json_data),200)


def GenerateOperation(idProduk):
    conn = database.connector()
    cursor = conn.cursor()

    #query INSERT ke Operasi
    query = "INSERT INTO prd_d_operasi(id,rencanaMulai,rencanaSelesai,proses,stasiunKerja,produk)VALUES(%s,%s,%s,%s,%s,%s)"     
    try:
      
        query3 = "SELECT c.id AS 'IdProses',a.stasiunKerja,c.durasi FROM gen_r_mampuproses a JOIN prd_r_proses c ON c.id = a.proses JOIN prd_r_strukturjnsprd d ON d.idNodal = c.nodalOutput JOIN prd_r_jenisproduk e ON e.id = d.jnsProduk JOIN prd_r_rincianproyek f ON f.jenisProduk = e.id JOIN prd_r_proyek g ON g.id = f.proyek JOIN prd_d_produk h ON h.rincianProyek = f.id WHERE h.id = '"+idProduk+"'"
        cursor.execute(query3)
        recordsFetch = cursor.fetchall()

        N = 9
        counter=1
        proses = ""   
        stasiunKerja = ""

        print("test")
        query5 = "SELECT a.tglDibuat FROM prd_r_proyek a JOIN prd_r_rincianproyek b ON b.proyek = a.id JOIN prd_d_produk c ON c.rincianProyek = b.id WHERE c.id = '"+idProduk+"'"
        cursor.execute(query5)
       
        recorddate = cursor.fetchall()
        schedulledstartWorkDate = ""
        scehdulledFinishWorkDate = ""
     
        for data in recorddate:
           schedulledstartWorkDate = data[0]
           scehdulledFinishWorkDate = data[0]

       
        for index in recordsFetch:
            id_operation = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
            proses = index[0]
            stasiunKerja = index[1]
            durasi = index[2]
            counter = 1
            cek = False
            while cek == False:
                if counter %2 != 0 and cek == False:
                    scehdulledFinishWorkDate = scehdulledFinishWorkDate + datetime.timedelta(minutes = durasi)
                    values1 = (id_operation,schedulledstartWorkDate,scehdulledFinishWorkDate,proses,stasiunKerja,idProduk)
                    cursor.execute(query,values1)
                    schedulledstartWorkDate = scehdulledFinishWorkDate
                    cek = True
                if counter %2 == 0 and cek == False:
                    scehdulledFinishWorkDate = scehdulledFinishWorkDate + datetime.timedelta(minutes = durasi)
                    cursor.execute(query,values1)
                    schedulledstartWorkDate = scehdulledFinishWorkDate
                    cek = True
            print("")
        counter = counter + 1
                    
        dueDateproduk = HitungDueDateProduk(idProduk)
        query4 = "UPDATE prd_d_produk SET dueDate = %s WHERE id = %s"
        print("test")
        values2 = (dueDateproduk,idProduk)
        cursor.execute(query4,values2) 
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def ShowProductInPantauOperasi():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id , b.id AS 'IdRincian', b.jumlah, c.nama AS 'NamaProyek', d.nama AS 'NamaCustomer' FROM prd_d_produk a JOIN prd_r_rincianproyek b ON a.rincianProyek = b.id JOIN prd_r_proyek c ON c.id = b.proyek JOIN gen_r_customer d ON d.id = c.customerid"
    cursor.execute(query)
    records = cursor.fetchall()

    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)

def StartOperation(idOperasi):
    conn = database.connector()
    cursor = conn.cursor()
    query = "UPDATE prd_d_operasi SET mulai = '"+datetime.datetime.now()+"' WHERE id = '"+idOperasi+"'"
    cursor.execute(query)
    conn.commit()
    hasil = {"status" : "berhasil"}
    return hasil


def EndOperation(idOperasi):
    conn = database.connector()
    cursor = conn.cursor()
    query = "UPDATE prd_d_operasi SET selesai = '"+datetime.datetime.now()+"' WHERE id = '"+idOperasi+"'"
    cursor.execute(query)
    conn.commit()
    hasil = {"status" : "berhasil"}
    return hasil