import datetime
import db.db_handler as database
from flask import request,make_response,jsonify


def GetMaterialOnWS():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM mat_d_materialonws"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]

    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)



def AddMaterialOnWS():
    conn = database.connector()
    cursor = conn.cursor()

    query = "INSERT INTO mat_d_materialonws(id,workstationCode,materialStock,login)VALUES(%s,%s,%s,%s)"
  
    try:
        data = request.json
        id = data["id"]
        workstationCode = data["workstationCode"]
        materialStock = data["materialStock"]
        login = datetime.datetime.now()
        values = (id,workstationCode,materialStock,login)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil

def UpdateMaterialOnWS(id):
    conn = database.connector()
    cursor = conn.cursor()

    query = "UPDATE mat_d_materialonws SET id = %s, workstationCode = %s, materialStock = %s WHERE id = '"+id+"'"

    try:
        data = request.json
        id = data["id"]
        workstationCode = data["workstationCode"]
        materialStock = data["materialStock"]
        values = (id,workstationCode,materialStock)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))       
        hasil = {"status" : "gagal"}
    return hasil