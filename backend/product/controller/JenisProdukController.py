import db.db_handler as database
from datetime import datetime
from flask import request,make_response,jsonify

def AddJenisProduct():
    conn = database.connector()
    cursor = conn.cursor()

    query = "INSERT INTO prd_r_jenisproduk (id, nama, tglDibuat) VALUES (%s,%s,%s)"
    try:
        data = request.json
        id = data["id"]
        nama = data["nama"]
        tglDibuat = datetime.now()
       
        values = (id,nama,tglDibuat)
        cursor.execute(query,values)
        conn.commit()
        print("Jenis Produk Baru Ditambahkan!")
        hasil = {"status"  : "berhasil",
                 "message" : "Data berhasil ditambah"}
       
    except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}
    return hasil

def UpdateJenisProduk(id):
   conn = database.connector()
   try:
        data = request.json
    
        nama = data['nama']
        id = data['id']
        cursor = conn.cursor()
        query = "UPDATE prd_r_jenisproduk SET id = %s,nama = %s WHERE id = '"+id+"'"
        values = (id,nama)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
   except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}
   return hasil



def GetAllJenisProduk():
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM prd_r_jenisproduk"
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []

    for data in records :
        json_data.append(dict(zip(row_headers,data)))
    
    conn.commit()
    return make_response(jsonify(json_data),200)

def GetJenisProdukbyRincianProyek(id_rproyek):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.id,a.nama,a.tglDibuat,b.id AS 'idrincian' FROM prd_r_jenisproduk a JOIN prd_r_rincianproyek b ON b.jenisProduk = a.id WHERE b.id = '"+id_rproyek+"'"
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    conn.commit()
    return make_response(jsonify(json_data),200)


def GetRincianInJenisProduk(id_rincian):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.id AS 'IdRincian', a.jumlah AS 'jumlah', a.dueDate, b.id AS 'IdProyek', b.nama AS 'NamaProyek', c.id AS 'IdCustomer',c.nama AS 'NamaCustomer', d.id AS 'IdProduk',d.dueDate AS 'dueDateProduk' FROM prd_r_rincianproyek a JOIN prd_r_proyek b ON b.id = a.proyek JOIN gen_r_customer c ON c.id = b.customerid JOIN prd_d_produk d ON d.rincianProyek = a.id WHERE a.id = '"+id_rincian+"'"
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)

def GetJenisProductById(id_jproduk):
    conn = database.connector()
    cursor = conn.cursor()

    data = request.json
    #id_jproduk = data["id"]
    query = "SELECT * FROM prd_r_jenisproduk WHERE id ='"+id_jproduk+"'"
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    conn.commit()
    return make_response(jsonify(json_data),200)
   
    

def ShowJProdukJoinSJProduk():
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.id,a.nama,a.tglDibuat,"
    query = query + "b.idNodal,b.nama,b.jnsProduk "
    query = query + "FROM prd_r_jenisproduk a "
    query = query + "JOIN prd_r_strukturjnsprd b ON b.jnsProduk = a.id"

    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []

    for data in records:
       json_data.append(dict(zip(row_headers,data)))
    conn.commit()
    
    return make_response(jsonify(json_data),200)
