import db.db_handler as db
from flask import request,make_response,jsonify


def GetToolButuhOpr(username):
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM cpl_toolbutuhopr02 a WHERE a.stasiunKerja = '"+username+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)
