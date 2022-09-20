from operasi.controller.OperasiController import EndOperation
from project.controller.RincianProyekController import *
from datetime import datetime
import db.db_handler as database
from flask import request,make_response,jsonify

def GetAllProyek():
  conn = database.connector()
  cursor = conn.cursor()

  query = "SELECT * FROM prd_r_proyek"
  cursor.execute(query)

  row_headers = [x[0] for x in cursor.description]
  records = cursor.fetchall()
  json_data = []

  for data in records:
      json_data.append(dict(zip(row_headers,data)))

  conn.commit()
  return make_response(jsonify(json_data),200)

def GetProyekByCustomer(id):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.id,a.nama,a.tglDibuat,a.customerid FROM prd_r_proyek a JOIN gen_r_customer b ON b.id = a.customerid WHERE a.customerid = '"+id+"'"
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    conn.commit()
    return make_response(jsonify(json_data),200)

### Ga kepake
def AddProyek():
  conn = database.connector()
  cursor = conn.cursor()
  
  query = "INSERT INTO prd_r_proyek (id, nama,tglDibuat,customerid) VALUES (%s,%s,%s,%s)"
  try:
      data = request.json
      id_proyek = data["id"]
      nama_proyek = data["nama"]
     
      customerid = data['customerid']
      values = (id_proyek,nama_proyek,datetime.now(),customerid)
      cursor.execute(query,values)
      conn.commit()
      hasil = {"Status " : "Berhasil"}
  except Exception as e:
      print("Error" + str(e))
      hasil = {"Status" : "Gagal"}

  return hasil
###################

def GetCustomerInProyek(idCustomer):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id AS 'IdCustomer',a.nama AS 'NamaCustomer' FROM gen_r_customer a WHERE a.id = '"+idCustomer+"'"
    cursor.execute(query)

    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)

def AddProyekbyCustomer(id_customer):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id FROM gen_r_customer a WHERE a.id = '"+id_customer+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    temp = ""
    for data in records:
        temp = data[0]
   
    query = "INSERT INTO prd_r_proyek(id,nama,tglDibuat,customerid)VALUES(%s,%s,%s,'"+temp+"')"
    try:
        data = request.json
        id = data["id"]
        nama = data["nama"]
        now = datetime.now()
        values = (id,nama,now)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "berhasil"}
    return hasil



def UpdateProyek(id):
    conn = database.connector()
    query = "UPDATE prd_r_proyek SET id = %s,nama = %s,customerid = %s WHERE id = '"+id+"'"
    try:
        data = request.json
        id = data["id"]
        nama_proyek = data["nama"]
        customerid = data["customerid"]
        cursor = conn.cursor()
        values = (id,nama_proyek,customerid)

        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}

    return hasil
  

def AccumulatePercentageProyek(idOperasi):

    #Memberhentikan operasi, tanda sudah beres & mengupdate status operasi menjadi 1.
    EndOperation(idOperasi)

    conn = database.connector()
    cursor = conn.cursor()
    #meng GET data id proyek dari id operasi yang di klik
    query_get_idproyek = "SELECT d.id,a.selesai FROM prd_d_operasi a JOIN prd_d_produk b ON a.produk = b.id JOIN prd_r_rincianproyek c ON b.rincianproyek = c.id JOIN prd_r_proyek d ON c.proyek = d.id WHERE a.id = '"+idOperasi+"'"
    cursor.execute(query_get_idproyek)
    records = cursor.fetchall()
    id_proyek = ''
    tanggalSelesai = ''
    for data in records:
        id_proyek = data[0]
        tanggalSelesai = data[1]

    #print("Id Proyek       : ",id_proyek)
    #print("Tanggal Selesai : ",tanggalSelesai)

    #Get jumlah pesanan / jumlah item proyek
    query_count_nrincian = "SELECT a.jumlah FROM prd_r_rincianproyek a JOIN prd_r_proyek b ON b.id = a.proyek WHERE b.id = '"+id_proyek+"'"
    cursor.execute(query_count_nrincian)
    records_jumlah = cursor.fetchall()
    jumlah_itemproyek_str = ''
    for index in records_jumlah:
        jumlah_itemproyek_str = index[0]

    jumlah_itemproyek_int = int(jumlah_itemproyek_str)
    #Menghitung jumlah operasi dari suatu proyek
    query_count_operasi = "SELECT COUNT(a.id) AS 'jumlahOperasi' FROM prd_d_operasi a JOIN prd_d_produk b ON a.produk = b.id JOIN prd_r_rincianproyek c ON b.rincianproyek = c.id JOIN prd_r_proyek d ON c.proyek = d.id WHERE d.id = '"+id_proyek+"'"
    cursor.execute(query_count_operasi)
    records2 = cursor.fetchall()
    jml = ''
    jml_totalop_int = 0
    for data in records2:
        jml = data[0]
    jml_totalop_int = int(jml)

    nilai_percentage = 0
    counter = 0
    query_all = "SELECT a.id,a.rencanaMulai,a.rencanaSelesai,a.produk,a.status FROM prd_d_operasi a JOIN prd_d_produk b ON a.produk = b.id JOIN prd_r_rincianproyek c ON b.rincianproyek = c.id JOIN prd_r_proyek d ON c.proyek = d.id WHERE d.id = '"+id_proyek+"'"
    cursor.execute(query_all)
    records_operasi = cursor.fetchall()
    nstatus = 0
   
    for index in records_operasi:
        nstatus = index[4]
        if nstatus == 1:
            counter = counter + nstatus


    nilai_percentage = (counter / jml_totalop_int / jumlah_itemproyek_int) * 100
    print(nilai_percentage)
    tanggalStr = tanggalSelesai.strftime("%m/%d/%Y, %H:%M")
    print('tangal str : ',tanggalStr)
    query_update_percentage = "UPDATE prd_r_proyek SET percentage = %s WHERE id = %s"
    query_insert_cpl = "INSERT INTO cpl_progress(proyek,selesai,selesai_str,percentage)VALUES(%s,%s,%s,%s)"
    try:
        
        values3 = (nilai_percentage,id_proyek)
        cursor.execute(query_update_percentage,values3)
        values4 = (id_proyek,tanggalSelesai,tanggalStr,nilai_percentage)
        print("Idproyek : ",id_proyek,"date : ",tanggalSelesai,"date_str : ",tanggalStr,"percentage : ",nilai_percentage)
        cursor.execute(query_insert_cpl,values4)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil
    

def showpercentageProgressProyek():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM cpl_progress GROUP BY selesai_str"
    cursor.execute(query)

    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)


def showPercentageAllProyek():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id,a.nama,a.percentage FROM prd_r_proyek a"
    cursor.execute(query)
    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)
