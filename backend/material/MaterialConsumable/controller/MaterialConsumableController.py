from concurrent.futures import process
import datetime
import db.db_handler as database
from flask import request,make_response,jsonify



def GetMaterialConsumablebyProcess(idProcess):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.processCode,a.materialStock,a.materialTypeCode,a.idNodal,a.quantity,a.unit FROM mat_r_consumable a JOIN prd_r_proses b ON b.id = a.processCode WHERE b.id = '"+idProcess+"'"
    cursor.execute(query)
    records = cursor.fetchall()

    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)



def addMaterialConsumable():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO mat_r_consumable(processCode,materialStock,materialTypeCode,idNodal,quantity,unit)VALUES(%s,%s,%s,%s,%s,%s)"
   
    try:
        data = request.json
        processCode = data["processCode"]
        materialStock = data["materialStock"]
        quantity = data["quantity"]
      
        query2 = "SELECT nodalOutput FROM prd_r_proses a JOIN prd_r_strukturjnsprd b ON b.idNodal = a.nodalOutput WHERE a.id = '"+processCode+"'"
        cursor.execute(query2)
        idNodal = ""
        records = cursor.fetchall()
        for data in records:
            idNodal = data[0]
        print("ID Nodal : ", idNodal)

        query3 = "SELECT materialTypeCode,unit FROM mat_d_materialstock a WHERE a.id = '"+materialStock+"' "
        cursor.execute(query3)
        records2 = cursor.fetchall()
        unit = ""
        materialTypeCode = ""
        for data in records2:
            materialTypeCode = data[0]
            unit = data[1]
        
        values = (processCode,materialStock,materialTypeCode,idNodal,quantity,unit)
        cursor.execute(query,values)

        query4 = "UPDATE mat_d_materialstock SET quantity = quantity - '"+quantity+"' WHERE id = '"+materialStock+"'"
        cursor.execute(query4)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil



