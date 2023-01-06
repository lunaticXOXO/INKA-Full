import db.db_handler as database
from datetime import datetime
from flask import request,make_response,jsonify


#Menambahkan data jenis produk eksternal
def AddJenisProductEksternal():
    conn = database.connector()
    cursor = conn.cursor()

    query = "INSERT INTO prd_r_jenisproduk (id, nama, tglDibuat) VALUES (%s,%s,%s)"
    query2 = "INSERT INTO prd_r_strukturjnsprd(idNodal,indukNodal,jnsProduk,materialTypeCode,nama,jumlah,satuan)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    query3 = "INSERT INTO mat_r_materialtype(code,nama)VALUES(%s,%s)"

    try:
        data = request.json
        id = data["id"]
        nama = data["nama"]
        tglDibuat = datetime.now()
       
        values = (id,nama,tglDibuat)
        cursor.execute(query,values)
        #conn.commit()   
        
        id_jproduk = ""
        id_strjproduk = ""
        #SELECT id jenis produk yg baru saja di insert
        query_select = "SELECT id FROM prd_r_jenisproduk WHERE id = '"+id+"'"
        cursor.execute(query_select)
        records_jproduk = cursor.fetchall()
        for index in records_jproduk:
            id_jproduk = index[0]
        
        id_strjproduk = id_jproduk + "A00"
        values2 = (id_strjproduk,None,id,id_strjproduk,nama,1,"pcs")
        values3 = (id_strjproduk,nama)

        cursor.execute(query3,values3)
        cursor.execute(query2,values2)
        conn.commit()
        hasil = {"status"  : "berhasil"}
       
    except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}
    return hasil


def AddJenisProductInternal():
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
        hasil = {"status" : "berhasil"}
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

    query = "SELECT a.id,a.nama,a.tglDibuat,b.id AS 'idrincian' FROM prd_r_jenisproduk a JOIN prd_d_rincianproyek b ON b.jenisProduk = a.id WHERE b.id = '"+id_rproyek+"'"
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))

    conn.commit()
    cursor.close()
    conn.close()
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def GetRincianInJenisProduk(id_rincian):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.id AS 'IdRincian', a.jumlah AS 'jumlah', a.dueDate, b.id AS 'IdProyek', b.nama AS 'NamaProyek', c.id AS 'IdCustomer',c.nama AS 'NamaCustomer', d.id AS 'IdProduk',d.dueDate AS 'dueDateProduk' FROM prd_d_rincianproyek a JOIN prd_d_proyek b ON b.id = a.proyek JOIN gen_r_customer c ON c.id = b.customerid JOIN prd_d_produk d ON d.rincianProyek = a.id WHERE a.id = '"+id_rincian+"'"
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
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
    cursor.close()
    conn.close()
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
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def ShowJProdukInternal():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM prd_r_jenisproduk  WHERE id LIKE 'Z%' OR id LIKE 'Y%' OR id LIKE 'X%'"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []

    for data in records:
       json_data.append(dict(zip(row_headers,data)))
    conn.commit()
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def ShowJProdukEksternal():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM prd_r_jenisproduk  WHERE id NOT LIKE 'Z%' ORDER BY id DESC"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []

    for data in records:
       json_data.append(dict(zip(row_headers,data)))
    conn.commit()
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)
