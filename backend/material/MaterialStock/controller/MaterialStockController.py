import db.db_handler as database
import datetime
from flask import request,make_response,jsonify

def GetMaterialStock():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM mat_d_materialstock"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def AddNewMaterialStock():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO mat_d_materialstock(id,purchaseId,purchaseItem,materialTypeCode,merk,quantity,unit,arrivalDate,supplierCode)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        data = request.json
        id = data["id"]
        purchaseId = data["purchaseId"]
        orders = data["purchaseItem"]
        materialTypeCode = data["materialTypeCode"]
        merk = data["merk"]
        quantity = data["quantity"]
        unit = data["unit"]
        arrivalDate = data["arrivalDate"]
        supplierCode = data["supplierCode"]
        values = (id,purchaseId,orders,materialTypeCode,merk,quantity,unit,arrivalDate,supplierCode)
        cursor.execute(query,values)
        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def GetMaterialStockbyOrder(order):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id,a.purchaseItem,a.merk,a.quantity,a.unit,a.arrivalDate FROM mat_d_materialstock a JOIN mat_d_purchaseitem b ON b.id_item = a.purchaseItem WHERE a.purchaseItem = '"+order+"'"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)

def AddMaterialStockbyOrders(orders):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT id_item FROM mat_d_purchaseitem WHERE id_item = '"+orders+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    for index in records:
        orders = index[0]
    print("ID Item : ",orders)
    query_insert = "INSERT INTO mat_d_materialstock(id,purchaseItem,merk,quantity,unit,arrivalDate)VALUES(%s,%s,%s,%s,%s,%s)"
    query_insert2 = "INSERT INTO mat_d_materialonws01(workstationCode,materialStock,login)VALUES(%s,%s,%s)"
    query_insert3 = "INSERT INTO mat_d_statusbarcode(id,workstation)VALUES(%s,%s)"
    query_insert4 = "INSERT INTO mat_d_materialstock01(id,purchaseID)VALUES(%s,%s)"
    try:
        data = request.json
        id = data["id"]
        merk = data["merk"]
        quantity = data["quantity"]
        unit = data["unit"]
        arrivalDate = data["arrivalDate"]
        workstationCode = "WSGD"
        login = datetime.datetime.now()
        values = (id,orders,merk,quantity,unit,arrivalDate)
    
        cursor.execute(query_insert,values)
        conn.commit()
        query_get_idstock = "SELECT id FROM mat_d_materialstock WHERE id = '"+id+"'"
        cursor.execute(query_get_idstock)

        record_idstock = cursor.fetchall()
        for index in record_idstock:
            new_idstock = index[0]
        print(new_idstock)

        values2 = (workstationCode,new_idstock,login)
        values3 = (new_idstock,workstationCode)
        values4 = (new_idstock,orders)

        cursor.execute(query_insert2,values2)
        cursor.execute(query_insert3,values3)
        cursor.execute(query_insert4,values4)
        
        conn.commit()
        
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        hasil = {"status" : "gagal"}
        print("Error",str(e))
    return hasil




def GetPurchaseItemInMatStock(orders):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id_item,c.nama AS 'namaSupplier', d.nama AS 'namaMatType' ,a.quantity,a.unit,e.id,e.nama,e.purchaserName FROM mat_d_purchaseitem a JOIN gen_r_supplier c ON c.code = a.supplierCode JOIN mat_r_materialtype d ON d.code = a.materialTypeCode JOIN mat_d_purchasematerial e ON e.id = a.purchaseId WHERE a.id_item = '"+orders+"'"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)



