import db.db_handler as db
from flask import request,make_response,jsonify

def GetGroups():
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM mat_r_group"
    cursor.execute(query)
    records = cursor.fetchall()

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)


def AddGroups():
    conn = db.connector()
    cursor = conn.cursor()

    query = "INSERT INTO mat_r_group(code,descriptions,remark)VALUES(%s,%s,%s)"
    try:
        data = request.json
        code = data["code"]
        descriptions = data["descriptions"]
        remark = data["remark"]
        values = (code,descriptions,remark)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def UpdateGroups(code):
    conn = db.connector()
    cursor = conn.cursor()

    query = "UPDATE mat_r_group SET code = %s, descriptions = %s, remark = %s WHERE code = '"+code+"'"
    try:
        data = request.json
        code = data["code"]
        descriptions = data["descriptions"]
        remark = data["remark"]
        values = (code,descriptions,remark)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil