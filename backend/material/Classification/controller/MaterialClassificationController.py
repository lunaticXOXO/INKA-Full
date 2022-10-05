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

    query = "INSERT INTO mat_r_classification(CODE,DESCRIPTION)VALUES(%s,%s)"
    try:
        data = request.json
        code = data["CODE"]
        descriptions = data["DESCRIPTION"]
        values = (code,descriptions)
        cursor.execute(query,values)
        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def UpdateClassification(code):
    conn = db.connector()
    cursor = conn.cursor()

    query = "UPDATE mat_r_classification SET CODE = %s,DESCRIPTION = %s WHERE CODE = '"+code+"'"
    try:
        data = request.json
        code = data["CODE"]
        descriptions = data["DESCRIPTION"]
        values = (code,descriptions)
        cursor.execute(query,values)
        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}
    
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil