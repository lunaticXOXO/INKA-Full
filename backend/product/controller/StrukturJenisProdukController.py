import db.db_handler as database
from flask import request,make_response,jsonify

def ShowStrukturJenisProduk():
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.idNodal, a.nama, a.jumlah, a.satuan, b.indukNodal, c.id FROM prd_r_strukturjnsprd a "
    query = query + "JOIN prd_r_strukturjnsprd b ON b.indukNodal = a.idNodal "
    query = query + "JOIN prd_r_jenisproduk c ON c.id = a.jnsProduk"

    records = cursor.fetchall(query)
    row_headers = [x[0] for x in cursor.description]

    
    for data in records:
        print("ID Nodal         : ",data[0],)
        print("Nama             : ",data[1],)
        print("Jumlah           : ",data[2],)
        print("Satuan           : ",data[3],)
        print("Induk Nodal      : ",data[4],)
        print("ID Jenis Produk  : ",data[5],)

    return records

def ShowAllSJProduk():
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM prd_r_strukturjnsprd"
    cursor.execute(query)
    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    conn.commit()
    return make_response(jsonify(json_data),200)


def ShowSJProdukbyIDJenisProduk(id):
    conn = database.connector()
    cursor = conn.cursor()
    
    query = "SELECT a.id,b.idNodal,b.nama,b.indukNodal,b.jumlah,b.satuan FROM prd_r_jenisproduk a JOIN prd_r_strukturjnsprd b ON b.jnsProduk = a.id WHERE a.id = '"+id+"' "
   
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()

    json_data = []
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    conn.commit()

    return make_response(jsonify(json_data),200)


def AddSJProdukByJenisProduk(id_jproduk):
    conn = database.connector()
    cursor = conn.cursor()
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id FROM prd_r_jenisproduk a JOIN prd_r_strukturjnsprd b ON b.jnsProduk = a.id WHERE a.id = '"+id_jproduk+"' LIMIT 1"

    cursor.execute(query)
    records = cursor.fetchall()
   
    for index in records:
        temp = index[0]
    

    print(temp)
    print(type(temp))
    query = "INSERT INTO prd_r_strukturjnsprd(idNodal,indukNodal,jnsProduk,nama,jumlah,satuan)VALUES(%s,%s,'"+temp+"',%s,%s,%s)"
    try :
        data = request.json
        idNodal = data["idNodal"]
        indukNodal = data["indukNodal"]
        nama = data["nama"]
        jumlah = data["jumlah"]
        satuan = data["satuan"]
        values = (idNodal,indukNodal,nama,jumlah,satuan)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status":"berhasil"}
    except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}
    return hasil

def AddStrukturJenisProduk():
    conn = database.connector()
    cursor = conn.cursor()

    idNodal, indukNodal, jnsProduk, nama, jumlah, satuan = input("Input ID Nodal : "), input("Input Induk Nodal : "), input("Input Jenis Produk : "), input("Input Nama : "), input("Input Jumlah : "), input("Input Satuan : ")

    query = "INSERT INTO prd_r_strukturjnsprd (idNodal, indukNodal, jnsProduk, nama, jumlah, satuan) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (idNodal, indukNodal, jnsProduk, nama, jumlah, satuan)
    cursor.execute(query,values)
    
    conn.commit()
    print("Struktur Jenis Produk Baru Ditambahkan!")


def ShowSJProdJoinProses():
    conn = database.connector()
    cursor = conn.cursor()
    
    query = "SELECT a.idNodal,a.nama,a.jumlah,a.satuan,"
    query = query + "b.id,b.nama,b.durasi,b.satuanDurasi,b.jenisProses "
    query = query + "FROM prd_r_strukturjnsprd a "
    query = query + "JOIN prd_r_proses b ON b.nodalOutput = a.idNodal"

    cursor.execute(query)
    records = cursor.fetchall()

    return records