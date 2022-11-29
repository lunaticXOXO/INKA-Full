import datetime
import db.db_handler as database
from flask import request,make_response,jsonify
import random
import string

def GetMaterialItem():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * from mat_d_purchaseitem"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


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

    query_select = "SELECT id FROM mat_d_purchasematerial WHERE id = '"+idPurchase+"'"
    cursor.execute(query_select)
    records = cursor.fetchall()
    for index in records:
        idPurchase = index[0]

    print("ID Purchase : ",idPurchase)
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


def GetPurchaseMaterialinPurchaseItem(idPurchase):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM  mat_d_purchasematerial WHERE id = '"+idPurchase+"'"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def GetPurchaseMaterialItemComparedMatStock(idPurchase):
    conn = database.connector()
    cursor = conn.cursor()
    qty_purchaseitem = ""
    qty_stock = ""
    
    query = "SELECT quantity FROM mat_d_purchaseitem WHERE purchaseId = '"+idPurchase+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    for index in records:
        qty_purchaseitem = index[0]
    
    
    #print("qty_purchaseitem : ",qty_purchaseitem)
    
    
    query_matstock = "SELECT a.quantity FROM mat_d_materialstock a JOIN mat_d_purchaseitem b ON b.id_item = a.purchaseItem JOIN mat_d_purchasematerial c ON c.id = b.purchaseId WHERE c.id = '"+idPurchase+"' GROUP BY a.quantity"
    cursor.execute(query_matstock)
    records_item = cursor.fetchall()
    for index2 in records_item:
        qty_stock = index2[0]
    #print("qty_stock : ",qty_stock)
    #qty_stock_int = int(qty_stock)
    
    records_purch_item = []
    #if qty_stock == qty_purchaseitem:
    #    query_show = "SELECT * FROM mat_d_purchaseitem WHERE id_item = NULL"
    #elif qty_stock == '':
    #    query_show = "SELECT a.id_item,a.materialTypeCode,a.purchaseId,a.quantity,a.schedulledArrival,a.supplierCode,a.unit FROM mat_d_purchaseitem a WHERE a.purchaseId = '"+idPurchase+"'"
   # elif qty_purchaseitem < qty_stock:
    #    query_show = "SELECT a.id_item,a.materialTypeCode,a.purchaseId,a.quantity,a.schedulledArrival,a.supplierCode,a.unit FROM mat_d_purchaseitem a WHERE a.purchaseId = '"+idPurchase+"'"
    #else:
    query_show = "SELECT * FROM mat_d_purchaseitem WHERE purchaseId = '"+idPurchase+"'"
       
    cursor.execute(query_show)
    records_purch_item = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    for data in records_purch_item:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


