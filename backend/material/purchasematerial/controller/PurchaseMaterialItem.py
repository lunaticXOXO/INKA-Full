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

    #GET Id Purchase yang di klik
    print("ID Purchase : ",idPurchase)

    #Angka awal dan angka akhir di set 00 & 0
    angka_awal = '00'
    angka_akhir = 0
    temp = ""
    id_item_new = ""    


    query_get_purchaseItem = "SELECT a.id_item FROM mat_d_purchaseitem a JOIN mat_d_purchasematerial b ON b.id = a.purchaseId WHERE b.id = '"+idPurchase+"'"
    cursor.execute(query_get_purchaseItem)
    records_matitem = cursor.fetchall()

    for index in records_matitem:
        temp = index[0]
    print("temp : ",temp)
    if temp == '':
        print("test2")
        id_item_new = idPurchase + "000"
    else:
        angka_akhir_str = ""
        for index in records_matitem:
            if angka_akhir >= 10:
                angka_awal = '0'
                angka_akhir = angka_akhir + 1
                angka_akhir_str = str(angka_akhir)
                id_item_new = idPurchase + angka_awal + angka_akhir_str
            else:
                angka_akhir = angka_akhir + 1
                angka_akhir_str = str(angka_akhir)
                id_item_new = idPurchase + angka_awal + angka_akhir_str

    print("ID Item : ",id_item_new)
    query_insert = "INSERT INTO mat_d_purchaseitem(id_item,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,purchaseId)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    try:
        data = request.json
        supplierCode = data["supplierCode"]
        materialTypeCode = data["materialTypeCode"]
        quantity = data["quantity"]
        unit = data["unit"]
        schedulledArrival = data["schedulledArrival"]
        values = (id_item_new,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,idPurchase)
        cursor.execute(query_insert,values)
        print("ID Item : ",id_item_new)
        conn.commit()
        #Query untuk menampilkan hasil multiplier dan quantity
        query_get_multiplie = "SELECT a.quantity,b.multiplier FROM mat_d_purchaseitem a JOIN gen_r_materialunit b ON b.id = a.unit WHERE a.id_item = '"+id_item_new+"'"
        cursor.execute(query_get_multiplie)
        records_unit = cursor.fetchall()
        mul_str = ""
        qty_str = ""
        for index in records_unit:
            qty_str = index[0]
            mul_str = index[1]
        
        print("qty_str : ",qty_str)
        qty_int = int(qty_str)
        mul_int = int(mul_str)
        
        
        #total kan qty int dengan multiplier
        total = qty_int * mul_int
        unit = "U01"
        query_update = "UPDATE mat_d_purchaseitem SET quantity = %s, unit = %s WHERE id_item = %s"
        values = (total,unit,id_item_new)
        cursor.execute(query_update,values)
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
    query = "SELECT a.id_item,a.supplierCode,a.materialTypeCode,a.quantity,c.nama AS 'namaUnit',a.schedulledArrival,a.purchaseId FROM mat_d_purchaseitem a "
    query += "JOIN mat_d_purchasematerial b ON b.id = a.purchaseId JOIN gen_r_materialunit c ON c.id = a.unit "
    query += "WHERE a.purchaseId = '"+idPurchase+"' AND a.quantity != 0 ORDER BY a.id_item DESC"

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
    query_show = "SELECT a.id_item,a.materialTypeCode,a.purchaseId,a.quantity,a.schedulledArrival,a.supplierCode,b.nama AS 'unit' FROM mat_d_purchaseitem a JOIN gen_r_materialunit b ON b.id = a.unit WHERE a.purchaseId = '"+idPurchase+"' AND a.quantity != 0 ORDER BY a.id_item DESC "
       
    cursor.execute(query_show)
    records_purch_item = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    for data in records_purch_item:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


