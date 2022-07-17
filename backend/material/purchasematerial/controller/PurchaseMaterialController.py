import datetime
import db.db_handler as database
from flask import request,make_response,jsonify

def PurchaseMaterial():
    conn = database.connector()
    cursor = conn.cursor()

    query = "INSERT INTO mat_d_purchasematerial(id,nama,purchaseName,purchaseDate)VALUES(%s,%s,%s,%s)"
    query2 = "INSERT INTO mat_d_purchaseitem(id,supplierCode,materialTypeCode,unit,schedulledArrival,purchaseId)VALUES(%s,%s,%s,%s,%s,%s)"
    try:
        data = request.json
        data2 = request.json
        id = data["id"]
        nama = data["nama"]
        purchaserName = data["purchaserName"]
        purchaseDate = datetime.now()
        id_item = data2["id"]
        supplierCode = data2["supplierCode"]
        materialTypeCode = data2["materialTypeCode"]
        unit = data2["unit"]
        schedulledArrival = datetime.now() + datetime.timedelta(days=7)
        purchaseId = data2["purchaseId"]

        values = (id,nama,purchaserName,purchaseDate)
        values2 = (id_item,supplierCode,materialTypeCode,unit,schedulledArrival,purchaseId)
        
        cursor.execute(query,values)
        cursor.execute(query2,values2)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil