import db.db_handler as database
from flask import request,make_response,jsonify

def ShowAllCountry():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM gen_r_country"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def AddNewCountry():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO gen_r_country(code,nama)VALUES(%s,%s)"
    try:
        data = request.json
        code = data["code"]
        nama = data["nama"]
        values = (code,nama)
        cursor.execute(query,values)
        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}
    return hasil

def UpdateCountry(code):
    conn = database.connector()
    cursor = conn.cursor()
    query = "UPDATE gen_r_country SET code = %s,nama = %s WHERE code = '"+code+"'"
    try:
        data = request.json
        code = data["code"]
        nama = data["nama"]
        values = (code,nama)

        cursor.execute(query,values)
        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}

    return hasil