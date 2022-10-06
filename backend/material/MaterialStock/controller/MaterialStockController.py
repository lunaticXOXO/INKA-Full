import db.db_handler as database
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


def InsertNewMaterialStock():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO mat_d_materialstock(id,purchaseId,orders,materialTypeCode,merk,quantity,unit,arrivalDate,supplierCode)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        data = request.json
        id = data["id"]
        purchaseId = data["purchaseId"]
        orders = data["orders"]
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