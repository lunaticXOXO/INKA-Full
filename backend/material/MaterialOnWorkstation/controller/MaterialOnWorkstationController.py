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
    

def AddMaterialStockOnWSByIdStock(idStock):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT id FROM mat_d_materialstock WHERE id = '"+idStock+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    for index in records:
        idStock = index[0]
    
    query_insert = "INSERT INTO mat_d_materialonws(workstationCode,materialStock,login)VALUES(%s,%s,%s)"
    try:
        data = request.json
      
        workstationCode = data["workstationCode"]
        login = datetime.datetime.now()
        values = (workstationCode,idStock,login)
        cursor.execute(query_insert,values)
        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil