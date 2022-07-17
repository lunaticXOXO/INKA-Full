import datetime
import db.db_handler as database
from flask import request,make_response,jsonify


def PurchaseMaterialItem():
    conn = database.connector()
    cursor = conn.cursor()

    query = "INSERT INTO mat_d_purchaseitem(id,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,purchaseId)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    try:
       data = request.json 
       id_item = data["id"]
       supplierCode = data["supplierCode"]
       materialTypeCode = data["materialTypeCode"]
       quantity = data["quantity"]
       unit = data["unit"]
       schedulledArrival = datetime.now() + datetime.timedelta(days=7)
       purchaseId = data["purchaseId"]
       values = (id_item,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,purchaseId)
       cursor.execute(query,values)
       conn.commit()
       hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil