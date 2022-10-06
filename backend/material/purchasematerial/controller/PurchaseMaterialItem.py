import datetime
import db.db_handler as database
from flask import request,make_response,jsonify
import random
import string

def PurchaseMaterialItem():
    conn = database.connector()
    cursor = conn.cursor()

    query = "INSERT INTO mat_d_purchaseitem(id_item,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,purchaseId)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    try:
       data = request.json 
       id_item = data["id_item"]
       supplierCode = data["supplierCode"]
       materialTypeCode = data["materialTypeCode"]
       quantity = data["quantity"]
       unit = data["unit"]
       schedulledArrival = data["schedulledArrival"]
       purchaseId = data["purchaseId"]
       values = (id_item,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,purchaseId)
       cursor.execute(query,values)
       conn.commit()
       cursor.close()
       conn.close()
       hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil

def PurchaseMaterialItemByIDPurchase(idPurchase):
    conn = database.connector()
    cursor = conn.cursor()
    idPurchase = ""
    query_select = "SELECT id FROM mat_d_purchasematerial WHERE id = '"+idPurchase+"'"
    cursor.execute(query_select)
    records = cursor.fetchall()
    for index in records:
        idPurchase = index[0]

    query_insert = "INSERT INTO mat_d_purchaseitem(id_item,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,purchaseId)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    try:
        data = request.json
        id_item = data["id_item"]
        supplierCode = data["supplierCode"]
        materialTypeCode = data["materialTypeCode"]
        quantity = data["quantity"]
        unit = data["unit"]
        schedulledArrival = data["schedulledArrival"]
        values = (id_item,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,idPurchase)
        cursor.execute(query_insert,values)
        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil
    

def GetMaterialItemByPurchaseMaterial(idPurchase):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id_item,a.supplierCode,a.materialTypeCode,a.quantity,a.unit,a.schedulledArrival,a.purchaseId FROM mat_d_purchaseitem a "
    query += "JOIN mat_d_purchasematerial b ON b.id = a.purchaseId "
    query += "WHERE a.purchaseId = '"+idPurchase+"'"

    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)




