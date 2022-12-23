from numpy import record
import db.db_handler as database
from flask import request,make_response,jsonify
import random
import string
from datetime import datetime
import time

def ShowOperasiFromProduct(idProduct):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.id AS 'idOperasi',a.rencanaMulai,a.rencanaSelesai, b.id AS 'idProses',b.nama AS 'namaProses', a.produk,a.stasiunKerja,a.output,a.mulai,a.selesai FROM prd_d_operasi a JOIN prd_r_proses b ON b.id = a.proses JOIN prd_d_produk i ON i.id = a.produk WHERE i.id = '"+idProduct+"' ORDER BY a.rencanaMulai ASC"
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

    query_min = "SELECT MIN(a.SCHEDULLEDSTARTOPERATION) FROM prd_d_operation a"
    cursor.execute(query_min)
    records = cursor.fetchall()
    for data in records:
        rencana_mulai_min = data[0]
        rencana_mulai_min = str(rencana_mulai_min)
    print(rencana_mulai_min)

    #query = "SELECT a.id,a.rencanaMulai, b.id AS 'idProduk',b.dueDate AS 'dueDateProduk', c.id AS 'idRincian',c.jumlah,c.dueDate AS 'dueDateRincian', d.id AS 'idProyek', d.nama AS 'namaProyek', e.id AS 'idCustomer', e.nama AS 'namaCustomer' FROM prd_d_operasi a JOIN prd_d_produk b ON b.id = a.produk JOIN prd_d_rincianproyek c ON c.id = b.rincianProyek JOIN prd_d_proyek d ON d.id = c.proyek JOIN gen_r_customer e ON e.id = d.customerid WHERE a.produk = '"+id_product+"' AND a.rencanaMulai = '"+rencana_mulai_min+"'"
    query = "SELECT a.ID AS 'idOperasi',a.SCHEDULLEDSTARTOPERATION,a.SCHEDULLEDFINISHOPERATION, b.id AS 'idProses',b.nama AS 'namaProses',a.produk, i.operatorid,j.nama AS 'namaOperator' FROM prd_d_operation a JOIN prd_r_process b ON b.id = a.proses JOIN prd_r_strukturjnsprd d ON d.idNodal = b.nodalOutput JOIN prd_r_jenisproduk e ON e.id = d.jnsProduk JOIN prd_d_rincianproyek f ON f.jenisProduk = e.id JOIN prd_d_proyek g ON g.id = f.proyek JOIN prd_d_produk h ON h.rincianProyek = f.id JOIN opr_d_operatorneed i ON i.operationid = a.id JOIN opd_r_operator j ON j.code = i.operatorid WHERE h.id = '"+id_product+"' ORDER BY a.proses,a.rencanaMulai ASC"
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

    query = "SELECT a.id AS 'idOperasi',a.rencanaMulai,a.rencanaSelesai, b.id AS 'idProses',b.nama AS 'namaProses', a.produk FROM prd_d_operasi a JOIN prd_r_proses b ON b.id = a.proses JOIN prd_r_strukturjnsprd d ON d.idNodal = b.nodalOutput JOIN prd_r_jenisproduk e ON e.id = d.jnsProduk JOIN prd_d_rincianproyek f ON f.jenisProduk = e.id JOIN prd_d_proyek g ON g.id = f.proyek JOIN prd_d_produk h ON h.rincianProyek = f.id WHERE h.id = '"+idProduct+"' ORDER BY a.rencanaMulai ASC"
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
    query2 = "SELECT a.id FROM prd_r_proses a JOIN prd_r_strukturjnsprd b ON b.idNodal = a.nodalOutput JOIN prd_r_jenisproduk c ON c.id = b.jnsProduk JOIN prd_d_rincianproyek d ON d.jenisProduk = c.id JOIN prd_d_proyek e ON e.id = d.proyek JOIN prd_d_produk f ON f.rincianProyek = d.id WHERE f.id = '"+idProduk+"'"
    cursor.execute(query2)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records:
        json_data.append(dict(zip(row_headers,data)))    
    
    return make_response(jsonify(json_data),200)



def ConvertDateOperation():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT rencanaMulai,rencanaSelesai,rencanaMulai_str,rencanaSelesai_str FROM prd_d_operasi"
    cursor.execute(query)
    records = []
    records = cursor.fetchall()
    date_tanggal_mulai = ""
    date_tanggal_selesai = ""
    date_tanggal_mulai_str = ""
    date_tanggal_selesai_str = ""
    print(records)
    try:
    #UPDATE `prd_d_operasi` SET `rencanaMulai_str`= NULL ,`rencanaSelesai_str`= NULL  WHERE produk = '221028000'
        for data in records:
            date_tanggal_mulai = data[0]
            date_tanggal_selesai = data[1]
            query_insert = "UPDATE prd_d_operasi SET rencanaMulai_str = %s, rencanaSelesai_str = %s WHERE rencanaMulai = %s AND rencanaSelesai = %s"
            temp1 = ""
            temp2 = ""
            date_tanggal_mulai_str = date_tanggal_mulai.strftime("%Y-%m-%d %H:%M")
            date_tanggal_selesai_str = date_tanggal_selesai.strftime("%Y-%m-%d %H:%M")
            temp1 = date_tanggal_mulai_str
            temp2 = date_tanggal_selesai_str
            values = (temp1,temp2,date_tanggal_mulai,date_tanggal_selesai)
            cursor.execute(query_insert,values)
            conn.commit()
        hasil = {"status" : "berhasil"} 
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}

    cursor.close()
    conn.close()     
    return hasil  

def GetOperasiGanttChart(stasiunKerja):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id AS 'idOperasi', b.nama AS 'namaProses', c.keterangan AS 'namaStasiunKerja' , a.rencanaMulai_str AS 'rencanaMulai',a.rencanaSelesai_str AS 'rencanaSelesai' FROM prd_d_operasi a JOIN prd_r_proses b ON b.id = a.proses JOIN gen_r_stasiunkerja c ON c.id = a.stasiunKerja WHERE c.id = '"+stasiunKerja+"'"
    cursor.execute(query)
    records = cursor.fetchall()

    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)
        

def ShowProductInPantauOperasi():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id , b.id AS 'IdRincian', b.jumlah, c.nama AS 'NamaProyek', d.nama AS 'NamaCustomer' FROM prd_d_produk a JOIN prd_d_rincianproyek b ON a.rincianProyek = b.id JOIN prd_d_proyek c ON c.id = b.proyek JOIN gen_r_customer d ON d.id = c.customerid"
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
    dates = ''
    dates = datetime.datetime.now()
    query = "UPDATE prd_d_operasi SET mulai = %s,status = 0 WHERE id = %s"
    values = (dates,idOperasi)
    cursor.execute(query,values)
    conn.commit()
    conn.close()
    hasil = {"status" : "berhasil"}
    return hasil


def EndOperation(idOperasi):
    conn = database.connector()
    cursor = conn.cursor()

    #update kolom selesai
    dates = ''
    dates = datetime.datetime.now()
    query = "UPDATE prd_d_operasi SET selesai = %s WHERE id = %s"
    values = (dates,idOperasi)
    cursor.execute(query,values)

    #status menjadi 1 atau selesai
    query2 = "UPDATE prd_d_operasi SET status = %s WHERE id = %s"
    values2 = (1,idOperasi)
    cursor.execute(query2,values2)
    conn.commit()
    conn.close()
    hasil = {"status" : "berhasil"}
    return hasil


def StartResponseOperasi(nomorWS):
    conn = database.connector()
    cursor = conn.cursor()
    query_get_ws = "SELECT stasiunKerja FROM cpl_oprsiap WHERE stasiunKerja = '"+nomorWS+"'"
    cursor.execute(query_get_ws)
    records = cursor.fetchall()
    ws = ""
    for index in records:
        ws = index[0]
    query_insert = "INSERT INTO cpl_responoperasi(stasiunKerja,jenis,mulai)VALUES(%s,%s,%s)"
    
    try:
        jenis = "on"
        mulai = datetime.now()
        values_insert = (ws,jenis,mulai)
        cursor.execute(query_insert,values_insert)
        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        hasil = {"status" : "gagal"}
        print("Error",str(e))
    return hasil


def GetResponseStartOperasi(username):
    conn = database.connector()
    cursor = conn.cursor()
  
    query_cek = "SELECT username FROM opd_r_operator WHERE username = '"+username+"'"
    cursor.execute(query_cek)
    records_cek = cursor.fetchall()

    for data in records_cek:
        username = data[0]

    query_select = "SELECT a.mulai FROM cpl_oprsiap a WHERE a.stasiunKerja = '"+username+"'"
    cursor.execute(query_select)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)

def EndResponseOperasi(nomorWS):
    conn = database.connector()
    cursor = conn.cursor()
    query_get_ws = "SELECT stasiunKerja FROM cpl_oprsiap WHERE stasiunKerja = '"+nomorWS+"'"
    cursor.execute(query_get_ws)
    records = cursor.fetchall()
    ws = ""
    for index in records:
        ws = index[0]
    
    query_insert = "INSERT INTO cpl_responoperasi(stasiunKerja,jenis,mulai)VALUES(%s,%s,%s)"
    
    try:
        jenis = "off"
        finish = datetime.now()
        values_insert = (ws,jenis,finish)

        #Execute Query Insert responseOperasi #
        cursor.execute(query_insert,values_insert)
        
        #program pak rahmat
        
        conn.commit()
        
        #BacaProgramPakRahmat()

        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def BacaProgramPakRahmat():
    time.sleep(20)
    conn = database.connector()
    cursor = conn.cursor()

    query_update_percentage = "UPDATE prd_d_proyek SET percentage = %s WHERE id = %s"
    query_insert_cplprogress = "INSERT INTO cpl_progress(proyek,selesai,selesai_str,percentage)VALUES(%s,%s,%s,%s)"

    try:
        #Meng GET id produk dari operasi yang di klik tombol selesai
        id_produk = ""

        #Meng GET id proyek dari id produk yang didapat.
        id_proyek = ""
        
        selesai = "0000-00-00 00:00:00"

        #Counter untuk menghitung jumlah yang memiliki output
        counter = 0

        #Untuk menghitung jumlah total operasi sautu produk
        total = 0

        hasil_percentage = 0

        query_select_operasiproduk = "SELECT id,mulai,selesai,produk FROM prd_d_operasi WHERE selesai is not null and mulai is not null ORDER BY selesai DESC LIMIT 1" 
        cursor.execute(query_select_operasiproduk)
        records_produk = cursor.fetchall()

        for index in records_produk:
            selesai - index[2]
            id_produk = index[3]

        print("selesai : ",selesai)
        selesaiSTR = selesai.strftime("%m/%D/%Y, %H:%M")
        print("Selesai : ",selesai, "Selesai STR : ", selesaiSTR)
        print("ID Produk : ",id_produk)

        
        query_operation = "SELECT a.id,a.output,a.produk FROM prd_d_operasi a WHERE a.produk = '"+id_produk+"'"
        cursor.execute(query_operation)
        records_operation = cursor.fetchall()

        for index in records_operation:
            if index[1] != None:
                counter = counter + 1
            total = total + 1
        
        hasil_percentage = (counter / total ) * 100

        query_get_proyek = "SELECT a.id AS 'idProduk',c.id AS 'idProyek' FROM prd_d_produk a JOIN prd_d_rincianproyek b ON b.id = a.rincianproyek JOIN prd_d_proyek c ON c.id = b.proyek WHERE a.id = '"+id_produk+"'"
        cursor.execute(query_get_proyek)

        records_proyek = cursor.fetchall()
        for index in records_proyek:
            id_proyek = index[1]
        

        values_update = (hasil_percentage,id_proyek)      
        values_insert2 = (id_proyek,selesai,selesaiSTR,hasil_percentage)
        cursor.execute(query_update_percentage,values_update)
        cursor.execute(query_insert_cplprogress,values_insert2)
        conn.commit()
        cursor.close()
        conn.close()

        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil



def GetResponseEndOperasi(idOperasi):
    conn = database.connector()
    cursor = conn.cursor()
  
    query_cek = "SELECT username FROM opd_r_operator WHERE username = '"+username+"'"
    cursor.execute(query_cek)
    records_cek = cursor.fetchall()

    for data in records_cek:
        username = data[0]

    query_select = "SELECT a.selesai FROM cpl_oprsiap a WHERE a.stasiunKerja = '"+username+"'"
    cursor.execute(query_select)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def ShowOperasiLayak(username):
    conn = database.connector()
    cursor = conn.cursor()
    query_cek = "SELECT username FROM opd_r_operator WHERE username = '"+username+"'"
    cursor.execute(query_cek)
    records_cek = cursor.fetchall()

    for data in records_cek:
        username = data[0]
    
    query_opr_layak = "SELECT * FROM cpl_oprlayak WHERE stasiunKerja = '"+username+"' ORDER BY selesai DESC, rencanaMulai ASC"
    cursor.execute(query_opr_layak)
    records = cursor.fetchall()

    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)



def IfOperasiSiap(username):
    conn = database.connector()
    cursor = conn.cursor()
    query_cek = "SELECT username FROM opd_r_operator WHERE username = '"+username+"'"
    cursor.execute(query_cek)
    records_cek = cursor.fetchall()

    for data in records_cek:
        username = data[0]
    
    query = "SELECT * FROM cpl_oprsiap WHERE stasiunKerja = '"+username+"' "
    cursor.execute(query)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)




def ShowOperasiByProduct(idProduct):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM prd_d_operasi WHERE produk = '"+idProduct+"' ORDER BY rencanaMulai ASC"
    cursor.execute(query)

    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)