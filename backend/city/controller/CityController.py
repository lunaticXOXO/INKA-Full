import db.db_handler as database
from flask import request,make_response,jsonify

def GetAllCities():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM gen_r_city"
    cursor.execute(query)
    records = cursor.fetchall()

    row_headers = [x[0] for x in cursor.description]
    json_data = []
   
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)


def AddCity():
    conn = database.connector()
    cursor = conn.cursor()

    query = "INSERT INTO gen_r_city(code,nama,country)VALUES(%s,%s,%s)"
    try:
        data = request.json
        code = data["code"]
        nama = data["nama"]
        country = data["country"]

        values = (code,nama,country)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil

def UpdateCity(code):
    conn = database.connector()
    cursor = conn.cursor()

    query = "UPDATE gen_r_city SET code = %s,nama = %s, country = %s WHERE code = '"+code+"'"
    try:
        data = request.json
        code = data["code"]
        nama = data["nama"]
        country = data["country"]

        values = (code,nama,country)
        cursor.execute(query,values)
        hasil = {"status" : "berhasil"}
        conn.commit()
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}

    return hasil


def DeleteCity(code):
    conn = database.connector()
    cursor = conn.cursor()

    query = "DELTE FROM gen_r_city WHERE city = '"+code+"'"
    try:
        cursor.execute(query)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil
