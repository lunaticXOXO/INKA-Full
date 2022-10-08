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
