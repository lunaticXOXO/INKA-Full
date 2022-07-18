from flask import request,make_response,jsonify
import db.db_handler as database


def GetUnit():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM gen_r_materialunit"
    cursor.execute(query)

    records = cursor.fetchall()
    json_data = []

    row_headers = [x[0] for x in cursor.description]
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)
