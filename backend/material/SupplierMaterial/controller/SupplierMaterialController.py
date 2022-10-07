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


def AddMaterialTypeSupplierbySupplier(code):
    conn = db.connector()
    cursor = conn.cursor()
    query_select = "SELECT code FROM gen_r_supplier WHERE code = '"+code+"'"
    cursor.execute(query_select)
    records = cursor.fetchall()
    code_supplier = ""

    for data in records:
        code_supplier = data[0]
    
    query_insert = "INSERT INTO mat_r_materialtypesupplier(materialTypeCode,supplierCode)VALUES(%s,%s)"
    try:
        data = request.json
        materialTypeCode = data["materialTypeCode"]
        values = (materialTypeCode,code_supplier)
        cursor.execute(query_insert,values)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil



def ShowMaterialTypeSupplierBySupplier(code):
    conn = db.connector()
    cursor = conn.cursor()
    query = "SELECT a.code,a.nama AS 'namaSupplier',b.materialTypeCode,c.nama AS 'namaMaterialType' FROM gen_r_supplier a JOIN mat_r_materialtypesupplier b ON b.supplierCode = a.code JOIN mat_r_materialtype c ON c.code = b.materialTypeCode WHERE a.code = '"+code+"'"
    cursor.execute(query)

    records = cursor.fetchall()
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)