from numpy import record
import db.db_handler as database
from flask import request,make_response,jsonify
import random
import string
from product.controller.ProdukController import *
import datetime

def ShowOperasiFromProduct(id):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM prd_d_operasi"
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
    query = "INSERT INTO prd_d_operasi(id,proses,stasiunKerja,produk)VALUES(%s,%s,%s,%s)"     
    try:
      
        query3 = "SELECT c.id AS 'IdProses',a.stasiunKerja,c.durasi FROM gen_r_mampuproses a JOIN prd_r_proses c ON c.id = a.proses JOIN prd_r_strukturjnsprd d ON d.idNodal = c.nodalOutput JOIN prd_r_jenisproduk e ON e.id = d.jnsProduk JOIN prd_r_rincianproyek f ON f.jenisProduk = e.id JOIN prd_r_proyek g ON g.id = f.proyek JOIN prd_d_produk h ON h.rincianProyek = f.id WHERE h.id = '"+idProduk+"'"
        cursor.execute(query3)
        recordsFetch = cursor.fetchall()

        N = 9
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
            values1 = (id_operation,proses,stasiunKerja,idProduk)
            cursor.execute(query,values1)
           
            print("idproses : ",index[0])
            print("stasiunkerja : ",index[1])
            print("start1 : ",schedulledstartWorkDate)
            durasi = index[2]
            
            query7 = "UPDATE prd_d_operasi SET rencanaMulai = %s, rencanaSelesai =  %s WHERE produk = '"+idProduk+"'"
            scehdulledFinishWorkDate = scehdulledFinishWorkDate + datetime.timedelta(minutes = durasi)
            print("end1 : ",scehdulledFinishWorkDate)
            values3 = (schedulledstartWorkDate,scehdulledFinishWorkDate)
            cursor.execute(query7,values3)
           
            schedulledstartWorkDate = scehdulledFinishWorkDate

            scehdulledFinishWorkDate = scehdulledFinishWorkDate + datetime.timedelta(minutes = durasi)
            print("start2 : ",schedulledstartWorkDate)
            print("end2 : ",scehdulledFinishWorkDate)
            values4 = (schedulledstartWorkDate,scehdulledFinishWorkDate)
            cursor.execute(query7,values4)
          
            schedulledstartWorkDate = scehdulledFinishWorkDate
            print("")
                    
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