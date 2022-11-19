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



def GetMaterialStockOnWsByIdStock(idStock):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id,a.merk,b.workstationCode,b.login,b.logout FROM mat_d_materialstock a JOIN mat_d_materialonws01 b ON b.materialStock = a.id WHERE a.id = '"+idStock+"'"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def MaterialLogin():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO cpl_matlogin(stasiunKerja,idMat,waktu,keterangan,status01)VALUES(%s,%s,%s,%s)"
    try:
        data = request.json
        stasiunKerja = data["stasiunKerja"]
        idMat = data["idMat"]
        waktu = datetime.datetime.now()
        keterangan = "material berhasil login"
        status01 = waktu
        values = (stasiunKerja,idMat,waktu,keterangan,status01)
        cursor.execute(query,values)
        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        hasil = {"status" : "gagal"}
        print("Error",str(e))
    
    return hasil
