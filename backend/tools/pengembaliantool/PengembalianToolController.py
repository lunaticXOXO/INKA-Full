import db.db_handler as database
from flask import request,make_response,jsonify

def ShowToolOnWorkstation(ws):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT b.id AS 'idToolStock',c.codes AS 'idToolType',c.nama,b.quantity,b.unit FROM eqp_d_toolonws a JOIN eqp_d_toolstock b ON b.id = a.toolStockId JOIN eqp_r_tooltype c ON c.codes = b.toolTypeCode JOIN eqp_d_boxonws d ON d.stasiunKerja = a.stasiunKerja WHERE a.stasiunKerja = '"+ws+"' AND c.codes LIKE 'TS%'"
    cursor.execute(query)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records :
        json_data.append(dict(zip(row_headers,data)))
  
    return make_response(jsonify(json_data),200)



