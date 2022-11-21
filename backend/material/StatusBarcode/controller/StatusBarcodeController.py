import db.db_handler as database
from flask import request,make_response,jsonify

def ShowStatusBarcode():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM mat_d_statusbarcode"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)
