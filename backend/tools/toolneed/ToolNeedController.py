import db.db_handler as database
from flask import request,make_response,jsonify

def ShowToolNeedByProcess(idProcess):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.toolTypeCode,c.nama AS 'namaTool',a.processCode,b.nama AS 'namaProses',a.quantity FROM eqp_r_toolneed a JOIN prd_r_proses b ON b.id = a.processCode JOIN eqp_r_tooltype c ON c.codes = a.toolTypeCode WHERE b.id = '"+idProcess+"'"
    cursor.execute(query)

    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return  make_response(jsonify(json_data),200)


