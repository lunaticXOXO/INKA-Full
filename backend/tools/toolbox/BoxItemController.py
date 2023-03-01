from datetime import date
import db.db_handler as database
from flask import request,make_response,jsonify
import tools.toolstock.ToolStockController as toolstockcontroller
import datetime

def AddToolBox():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO eqp_r_toolbox(id,nama)VALUES(%s,%s)"
    try:
        data = request.json
        id_default = "TB"
        nama = data["nama"]

        query_countbaris = "SELECT COUNT(*) FROM eqp_r_toolbox WHERE id LIKE 'TB%'"
        cursor.execute(query_countbaris)
        records = cursor.fetchall()
        for index in records:
            count = index[0]

        count = int(count)
        count += 1
        
        length = len(str(count))
        length = int(length)
        id_box = ""
        if count < 10 and length == 1 :
            id_box = id_default + "000" + str(count)
        
        if count % 10 > 0 and length == 2:
            id_box = id_default + "00" + str(count)
        
        if count % 100 > 0 and length == 3:
            id_box = id_default + "0" + str(count)

        if count % 1000 > 0 and length == 4:
            id_box = id_default + str(count)
        
        values = (id_box,nama)
        cursor.execute(query,values)
        print("ID Box : ",id_box)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def ShowToolBox():
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM eqp_r_toolbox"
    cursor.execute(query)

    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return  make_response(jsonify(json_data),200)




def AddToolStockToBox(boxId):
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO eqp_d_boxitem(toolStockId,boxId,startDate)VALUES(%s,%s,%s)"
    try:
        data = request.json
      
        toolStockId = data["toolStockId"]
        startDate   = datetime.datetime.now()
       
        values = (toolStockId,boxId,startDate)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil
  