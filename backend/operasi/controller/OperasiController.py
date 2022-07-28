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



def GenerateOperation(idProduk):
    conn = database.connector()
    cursor = conn.cursor()

    #query INSERT ke Operasi
    query = "INSERT INTO prd_d_operasi(id,rencanaMulai,rencanaSelesai,mulai,selesai,proses,stasiunKerja,produk,status)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        data = request.json
        #meng get data proses & ws untuk suatu produk
        query2 = "SELECT a.id FROM prd_r_proses a JOIN prd_r_strukturjnsprd b ON b.idNodal = a.nodalOutput JOIN prd_r_jenisproduk c ON c.id = b.jnsProduk JOIN prd_r_rincianproyek d ON d.jenisProduk = c.id JOIN prd_r_proyek e ON e.id = d.proyek JOIN prd_d_produk f ON f.rincianProyek = d.id WHERE f.id = '"+idProduk+"'"
        query3 = "SELECT a.stasiunKerja FROM gen_r_mampuproses a JOIN prd_r_proses c ON c.id = a.proses JOIN prd_r_strukturjnsprd d ON d.idNodal = c.nodalOutput JOIN prd_r_jenisproduk e ON e.id = d.jnsProduk JOIN prd_r_rincianproyek f ON f.jenisProduk = e.id JOIN prd_r_proyek g ON g.id = f.proyek JOIN prd_d_produk h ON h.rincianProyek = f.id WHERE h.id = '"+idProduk+"'"
        cursor.execute(query2)
        cursor.execute(query3)
        #fetch all 2 query
        recordsProses = cursor.fetchall()
        recordsWS = cursor.fetchall()
        #append record proses & recordws

        #gabungkan antar 2 tuples
        recordsFetch = ()
        recordsFetch = recordsProses + recordsWS
        N = 9
        proses = ""   
        ws = ""
        for data in recordsFetch:
            id_operation = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
            proses = data[0]
            ws = data[1]
            values = (id_operation,proses,ws,idProduk)
            cursor.execute(query,values)
            conn.commit()
        
        #mendapat start date work dari produk
        dueDateproduk = HitungDueDateProduk(idProduk)
        schedulledstartWorkDate = ""
        scehdulledFinishWorkDate = ""
        query4 = "SELECT a.tglDibuat FROM prd_r_proyek a JOIN prd_r_rincianproyek b ON b.proyek = a.id JOIN prd_d_produk c ON c.rincianProyek = b.id WHERE c.id = '"+idProduk+"'"
        cursor.execute(query4)
       
        recorddate = cursor.fetchall()
        for data in recorddate:
           schedulledstartWorkDate = data[0]
           scehdulledFinishWorkDate = data[0]

        ##Mendapatkan data durasi proses yang dikerjakan dari suatu product
        query5 = "SELECT a.durasi FROM prd_r_proses a JOIN prd_r_strukturjnsprd b ON a.nodalOutput = b.idNodal JOIN prd_r_jenisproduk c ON c.id = b.jnsProduk JOIN prd_r_rincianproyek d ON d.jenisProduk = c.id JOIN prd_r_proyek e ON e.id = d.proyek JOIN prd_d_produk f ON f.rincianProyek = d.id WHERE f.id = '"+idProduk+"'"
        cursor.execute(query5)
        duration = ""
        recordDuration =  cursor.fetchall()
        for data in recordDuration:
            #mengenerate mulai,selesai,rencana mulai,mulai,selesai,status
            duration = data[0]
            scehdulledFinishWorkDate = scehdulledFinishWorkDate + datetime.timedelta(minutes = duration)
            query6 = "UPDATE prd_d_operasi SET rencanaMulai = '"+schedulledstartWorkDate+"', rencanaSelesai = '"+scehdulledFinishWorkDate+"'"
            schedulledstartWorkDate = scehdulledFinishWorkDate
            cursor.execute(query6)
            conn.commit()
      
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil