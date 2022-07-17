import datetime
from turtle import pu
import db.db_handler as database
from flask import request,make_response,jsonify

def PurchaseMaterial():
    conn = database.connector()
    cursor = conn.cursor()
    cursor2 = conn.cursor()
    query = "INSERT INTO mat_d_purchasematerial(id,nama,purchaserName,purchaseDate)VALUES(%s,%s,%s,%s)"
    query2 = "INSERT INTO mat_d_purchaseitem(id_item,supplierCode,materialTypeCode,unit,schedulledArrival,purchaseId)VALUES(%s,%s,%s,%s,%s,%s)"
    try:
        ##
        data = request.json
        
        id = data["id"]
        nama = data["nama"]
        purchaserName = data["purchaserName"]
        now = datetime.datetime.now()
       
      
        values = (id,nama,purchaserName,now)
        cursor.execute(query,values)
        conn.commit()

        query3 = "SELECT id FROM mat_d_purchasematerial WHERE id = '"+id+"'"
        cursor.execute(query3)
        purchaseId = ""
        record = cursor.fetchall()
        for index in record:
            purchaseId = index[0]

        print("purchase Id : ",purchaseId)

        data2 = request.json
        id_item = data2["id_item"]
        supplierCode = data2["supplierCode"]
        materialTypeCode = data2["materialTypeCode"]
        unit = data2["unit"]
        schedulledArrival = now + datetime.timedelta(days=7)
        
        values2 = (id_item,supplierCode,materialTypeCode,unit,purchaseId,schedulledArrival)    

        cursor2.execute(query2,values2)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil