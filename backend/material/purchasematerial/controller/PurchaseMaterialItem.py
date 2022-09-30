import datetime
import db.db_handler as database
from flask import request,make_response,jsonify
import random
import string

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


def PurchaseMaterialSederhana():
    conn = database.connector()
    cursor = conn.cursor()

    query = "INSERT INTO mat_d_purchasematerial(id,nama,purchaserName,purchaseDate)VALUES(%s,%s,%s,%s)"
    try:
        data = request.json
        id = data["id"]
        nama = data["nama"]
        purchaserName = data["purchaserName"]
        purchaserDate = datetime.datetime.now()
        values = (id,nama,purchaserName,purchaserDate)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil

def PurchaseMaterialAndGetId():
    conn = database.connector()
    cursor = conn.cursor()

    query = "INSERT INTO mat_d_purchasematerial(id,nama,purchaserName,purchaseDate)VALUES(%s,%s,%s,%s)"
    try:
        data = request.json
        id = data["id"]
        nama = data["nama"]
        purchaserName = data["purchaserName"]
        purchaserDate = datetime.datetime.now()
        values = (id,nama,purchaserName,purchaserDate)
        cursor.execute(query,values)
        conn.commit()
        
    except Exception as e:
        print("Error",str(e))
    
    query2 = "SELECT id FROM mat_d_purchasematerial WHERE id = '"+id+"'"
    cursor.execute(query2)
    records = cursor.fetchall()
    id_pemesan = ""
    for data in records:
        id_pemesan = data[0]
    return id_pemesan

def GetMaterialFromStock():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM mat_d_materialstock"

    cursor.execute(query)
    records = cursor.fetchall()

    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)


def AddMaterialtoStock():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO mat_d_materialstock(id,merk,quantity,unit,arrivalDate)VALUES(%s,%s,%s,%s,%s)"
  
    try:
        data = request.json

        id_material = data["id"]
        merk = data["merk"]
        quantity = data["quantity"]
        unit = data["unit"]
        arrivalDate = data["arrivalDate"]

        values = (id_material,merk,quantity,unit,arrivalDate)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def MinimalQuantity(id):
    conn = database.connector()
    cursor = conn.cursor()
    query_cek = "SELECT a.jumlah FROM prd_r_strukturjnsprd a JOIN mat_r_materialtype b ON b.code = a.materialTypeCode JOIN mat_r_materialtypesupplier c ON c.materialTypeCode = a.materialTypeCode JOIN mat_d_purchaseitem d ON d.materialTypeCode = a.materialTypeCode JOIN mat_d_materialstock e ON e.materialTypeCode = a.materialTypeCode WHERE e.id = '"+id+"'"

    cursor.execute(query_cek)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)
    

def PurchaseMaterialFromStock(id):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM mat_d_materialstock WHERE id = '"+id+"'" #memilih material yang tersedia di list
    cursor.execute(query)
    id_item = ""
    materialTypeCode = ""
    supplierCode = ""
    unit = ""
    records = cursor.fetchall()
    for data in records:
        materialTypeCode = data[3] #untuk insert otomatis materialtypecode di purchase item
        supplierCode = data[4] #untuk insert otomatis suppliercode di purchase item
        unit = data[7] # untuk insert otomatis unit di purchaseitem

    print("Material Type Code : ",materialTypeCode)
    print("supplierCode : ",supplierCode)
    print("unit : ",unit)

    query2 = "INSERT INTO mat_d_purchaseMaterial(id,nama,purchaserName,purchaseDate)VALUES(%s,%s,%s,%s)"
    query3 = "INSERT INTO mat_d_purchaseitem(id_item,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,purchaseid)VALUES(%s,%s,%s,%s,%s,%s,%s)"

    try:
        data = request.json
        data2 = request.json
        
        N = 5
        N2 = 3
        id_purchase = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N)) #Men Generate otomatis untuk id purchase material
        print("ID Purchase : ",id_purchase)

        id_item = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N2)) #Men Generate Otomatis untuk id purchase item 
        id_item_fix = id_item

        nama = data["nama"]
        purchaserName = data["purchaserName"]
        purchaserDate = datetime.datetime.now()
        values = (id_purchase,nama,purchaserName,purchaserDate)
        cursor.execute(query2,values)
        
        N2 = 3
        id_item = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N2)) #Men Generate Otomatis untuk id purchase item
        id_item_fix = id_item
        quantity = data2["quantity"]
        schedulledArrival = data2["schedulledArrival"]
        values2 = (id_item_fix,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,id_purchase)
        cursor.execute(query3,values2)
        
        ###Setelah Data di insert kan semua maka, bisa update data purchaseid dan orders di material stock
        query4 = "SELECT quantity FROM mat_d_purchaseitem WHERE id_item = '"+id_item_fix+"'"
        cursor.execute(query4)
        records2 = cursor.fetchall()
        qty = ""
        for data2 in records2:
            qty = data2[0]

        query5 = "UPDATE mat_d_materialstock SET purchaseId = %s, orders = %s, quantity = quantity + %s WHERE id = '"+id+"'"
        values3 = (id_purchase,id_item_fix,qty)
        cursor.execute(query5,values3)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def PurchaseNewMaterial():
    conn = database.connector()
    cursor = conn.cursor()
    N = 5
    query = "INSERT INTO mat_d_purchasematerial(id,nama,purchaserName,purchaseDate)VALUES(%s,%s,%s,%s)"
    query2 = "INSERT INTO mat_d_purchaseitem(id_item,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,purchaseId)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    query3 = "INSERT INTO mat_d_materialstock(id,purchaseId,orders,materialTypeCode,supplierCode,merk,quantity,unit,arrivalDate)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = request.json
    data2 = request.json
    data3 = request.json
    try:
        id_purchase = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
        #id_fix_purchase = id_purchase
        nama = data["nama"]
        purchaserName = data["purchaserName"]
        purchaseDate = data["purchaseDate"]
        
        id_item = data2["id_item"]
        supplierCode = data2["supplierCode"]
        materialTypeCode = data2["materialTypeCode"]
        quantity = data2["quantity"]
        unit = data2["unit"]
        schedulledArrival = data2["schedulledArrival"]
        
        id_stock = data3["id"]
        
        
        supplierCodeMat = supplierCode
      
        merk = data3["merk"]
        matquantity = quantity
        matunit = unit
        arrivalDate = datetime.datetime.now() + datetime.timedelta(days=7)

        values  = (id_purchase,nama,purchaserName,purchaseDate)
        values2 = (id_item,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,id_purchase)
        values3 = (id_stock,id_purchase,id_item,materialTypeCode,supplierCodeMat,merk,matquantity,matunit,arrivalDate)

        cursor.execute(query,values)
        #conn.commit()
        cursor.execute(query2,values2)
        #conn.commit()
        cursor.execute(query3,values3)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil

