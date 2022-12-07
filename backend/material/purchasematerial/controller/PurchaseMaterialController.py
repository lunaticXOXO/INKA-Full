import datetime
from turtle import pu
import db.db_handler as database
from flask import request,make_response,jsonify

def PurchaseMaterial():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO mat_d_purchasematerial(id,nama,purchaserName,purchaseDate)VALUES(%s,%s,%s,%s)"
    try:
        data = request.json
        
        id = data["id"]
        nama = data["nama"]
        purchaserName = data["purchaserName"]
        purchaseDate = data["purchaseDate"]
       
        values = (id,nama,purchaserName,purchaseDate)
        cursor.execute(query,values)
        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def GetPurchaseMaterial():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM mat_d_purchasematerial"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def ShowRequirementPurchaseMaterial(rencanaMulai):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT f.code AS 'codeMaterial',f.nama AS 'namaMaterial' ,SUM(e.jumlah) AS 'jumlah' FROM prd_d_operasi a JOIN prd_d_produk b ON a.produk = b.id JOIN prd_d_rincianproyek c ON c.id = b.rincianproyek JOIN prd_r_jenisproduk d ON d.id = c.jenisProduk JOIN prd_r_strukturjnsprd e ON e.jnsProduk = d.id JOIN mat_r_materialtype f ON f.code = e.materialTypeCode WHERE a.mulai IS NULL AND e.idNodal != e.materialTypeCode AND rencanaMulai < '"+rencanaMulai+"' GROUP BY f.nama,f.code"

    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)