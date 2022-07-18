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
    cursor2 = conn.cursor()
    query = "INSERT INTO mat_d_purchasematerial(id,nama,purchaserName,purchaseDate)VALUES(%s,%s,%s,%s)"
    query2 = "INSERT INTO mat_d_purchaseitem(id_item,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,purchaseId)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    try:
        data = request.json
        
        id = data["id"]
        nama = data["nama"]
        purchaserName = data["purchaserName"]
        now = datetime.datetime.now()
       
        values = (id,nama,purchaserName,now)
        cursor.execute(query,values)
        conn.commit()

        id_item = data["id_item"]
        supplierCode = data["supplierCode"]
        materialTypeCode = data["materialTypeCode"]
        quantity = data["quantity"]
        unit = data["unit"]
        purchaseId = data["purchaseId"]
        schedulledArrival = now + datetime.timedelta(days=7)

        values2 = (id_item,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,purchaseId)    
        cursor2.execute(query2,values2)
        conn.commit()
        
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil