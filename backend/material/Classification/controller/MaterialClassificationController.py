import db.db_handler as db
from flask import request,make_response,jsonify

def GetClassification():
    conn = db.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM mat_r_classification"
    cursor.execute(query)

    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))

    return make_response(jsonify(json_data),200)


def AddClassification():
    conn = db.connector()
    cursor = conn.cursor()

    query = "INSERT INTO mat_r_classification(code,descriptions)VALUES(%s,%s)"
    try:
        data = request.json
        code = data["code"]
        descriptions = data["descriptions"]
        values = (code,descriptions)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def UpdateClassification(code):
    conn = db.connector()
    cursor = conn.cursor()

    query = "UPDATE mat_r_classification SET code = %s,descriptions = %s WHERE code = '"+code+"'"
    try:
        data = request.json
        code = data["code"]
        descriptions = data["descriptions"]
        values = (code,descriptions)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil