import db.db_handler as db
from flask import request,make_response,jsonify

def GetMaterialType():
    conn = db.connector()
    cursor = conn.cursor()
    #query = "SELECT a.code,a.nama, a.isAvailable,a.isAssy, b.descriptions AS 'descriptionClassification', c.descriptions AS 'descriptionGroup' FROM mat_r_materialtype a JOIN mat_r_classification b ON b.code = a.classificationCode JOIN mat_r_group c ON c.code = a.groupCode"
    query = "SELECT a.code,a.nama, a.isAvailable,a.isAssy FROM mat_r_materialtype a"
    cursor.execute(query)
    records = cursor.fetchall()

    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)

def GetMaterialTypeDescription():
    conn = db.connector()
    cursor = conn.cursor()
    query = "SELECT a.code,a.nama FROM mat_r_materialtype a"
    cursor.execute(query)
    records = cursor.fetchall()

    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)




def AddMaterialType():
    conn = db.connector()
    cursor = conn.cursor()
    query = "INSERT INTO mat_r_materialtype(code,nama)VALUES(%s,%s)"

    try:
        data = request.json
        code = data["code"]
        nama = data["nama"]
       
        values = (code,nama)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil



def UpdateMaterialType(code):
    conn = db.connector()
    cursor = conn.cursor()
    query = "UPDATE mat_r_materialtype SET code = %s,nama = %s,isAvailable = %s,isAssy = %s,classificationCode = %s,groupCode = %s WHERE code = '"+code+"'"
    try:
        data = request.json
        code = data["code"]
        nama = data["nama"]
        isAvailable = data["isAvailable"]
        isAssy = data["isAssy"]
        classificationCode = data["classificationCode"]
        groupCode = data["groupCode"]
        values = (code,nama,isAvailable,isAssy,classificationCode,groupCode)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def SearchMaterialType(nama):
    conn = db.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM mat_r_materialtype WHERE nama LIKE '%"+nama+"%'"
    cursor.execute(query)

    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)




