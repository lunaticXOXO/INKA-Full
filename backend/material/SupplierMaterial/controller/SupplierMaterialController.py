import db.db_handler as db
from flask import request,make_response,jsonify

def ShowSupplierWithMaterialType():
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM mat_r_materialtypesupplier"
    cursor.execute(query)

    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]

    json_data = []
    for data in records:
        json_data.append(jsonify(dict(zip(row_headers,data))))
    
    return make_response(jsonify(json_data),200)


def AddSupplierMaterialType():
    conn = db.connector()
    cursor = conn.cursor()

    query = "INSERT INTO mat_r_materialtypesupplier(materialTypeCode,supplierCode)VALUES(%s,%s)"
    try:
        data = request.json
        materialTypeCode = data["materialTypeCode"]
        supplierCode = data["supplierCode"]
        values = (materialTypeCode,supplierCode)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil