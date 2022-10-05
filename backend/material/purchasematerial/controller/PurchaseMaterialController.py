import datetime
from turtle import pu
import db.db_handler as database
from flask import request,make_response,jsonify


def OffForeign():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SET GLOBAL FOREIGN_KEY_CHECKS = 0;"
    cursor.execute(query)

def PurchaseMaterial():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO mat_d_purchasematerial(id,nama,purchaserName,purchaseDate)VALUES(%s,%s,%s,%s)"
   
    try:
        data = request.json
        id = data["id"]
        nama = data["nama"]
        purchaserName = data["purchaserName"]
        date = data["purchaseDate"]
       
        values = (id,nama,purchaserName,date)
        cursor.execute(query,values)
        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil