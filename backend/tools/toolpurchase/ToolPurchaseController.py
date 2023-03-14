from datetime import date
import db.db_handler as database
from flask import request,make_response,jsonify
import datetime

def AddToolPurchase():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO eqp_d_toolpurchase(toolPurchaseId,orderName,purchaserName,PurchaseDate)VALUES(%s,%s,%s,%s)"
    try:
        data = request.json
        id_default = "PC"
        orderName = data["orderName"]
        purchaserName = data["purchaserName"]
        purchaserDate = datetime.datetime.now()

        query_countdata = "SELECT COUNT(*) FROM eqp_d_toolpurchase"
        cursor.execute(query_countdata)
        records_count = cursor.fetchall()
        count = ""
        for index in records_count:
            count = index[0]
            count = int(count)

        count = count + 1
        length = len(str(count))
        length = int(length)

        id_purchase = ""
        if count < 10 and length == 1 :
            id_purchase = id_default + "000" + str(count)
        
        if count % 10 > 0 and length == 2:
            id_purchase = id_default + "00" + str(count)
        
        if count % 100 > 0 and length == 3:
            id_purchase = id_default + "0" + str(count)

        if count % 1000 > 0 and length == 4:
            id_purchase = id_default + str(count)

        values = (id_purchase,orderName,purchaserName,purchaserDate)
        cursor.execute(query,values)
        print("id_purchase : ",id_purchase)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def ShowToolPurchase():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM eqp_d_toolpurchase"
    cursor.execute(query)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records :
        json_data.append(dict(zip(row_headers,data)))
  
    return make_response(jsonify(json_data),200)


