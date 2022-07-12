import db.db_handler as db
from flask import request,make_response,jsonify

def GetMaterialType():
    conn = db.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM mat_r_materialtype"

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
    query = "INSERT INTO mat_r_materialtype(code,nama,isAvailable,isAssy,classificationCode,groupCode)VALUES(%s,%s,%s,%s,%s,%s)"

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




