import db.db_handler as database
from flask import request,make_response,jsonify
import datetime

def ShowBoxChoosedByToolStock(toolstock):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.toolTypeCode FROM eqp_d_toolstock a WHERE a.id = '"+toolstock+"'"
    cursor.execute(query)
    data = cursor.fetchone()
    tooltype = data[0]

    #query untuk mencari stasiunkerja berdasarkan tooltypecode
    query = "SELECT stasiunKerja FROM cpl_kirimtool02 WHERE toolTypeCode = '"+tooltype+"'"
    cursor.execute(query)
    data = cursor.fetchone()
    pilihanws = data[0]

    query = "SELECT b.id,b.nama,a.stasiunKerja FROM eqp_d_boxonws a JOIN eqp_r_toolbox b ON b.id = a.boxId WHERE a.stasiunKerja = 'wsgd' UNION SELECT b.id,b.nama,a.stasiunKerja FROM eqp_d_boxonws a JOIN eqp_r_toolbox b ON b.id = a.boxId WHERE a.stasiunKerja = '"+pilihanws+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return  make_response(jsonify(json_data),200)

def ShowWorkstationByToolBox(idbox):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT b.id AS 'idWS', b.nama AS 'namaWS' FROM eqp_d_boxonws a JOIN gen_r_stasiunkerja b ON b.id = a.stasiunKerja WHERE a.boxId = '"+idbox+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return  make_response(jsonify(json_data),200)


def ShowWorkstationToolsByToolBox(idbox):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT b.id,b.nama,c.toolStockId FROM eqp_d_boxonws a JOIN gen_r_stasiunkerja b on b.id = a.stasiunKerja JOIN eqp_d_toolonws c on c.stasiunKerja = b.id WHERE a.boxId = '"+idbox+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return  make_response(jsonify(json_data),200)


def PengemasanToolStockToBox(toolstock,idbox):
    conn =  database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO eqp_d_boxitem(toolStockId,boxId,startDate)VALUES(%s,%s,%s)"
    
    try:    
        startdate = datetime.datetime.now()
        values = (toolstock,idbox,startdate)
        cursor.execute(query,values)
        query = "DELETE FROM eqp_d_boxonws WHERE boxid = '"+idbox+"' AND stasiunKerja = 'WSGD'"
        cursor.execute(query)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def ShowInsertedToolStockInBox(idbox):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.boxId,a.toolStockId,c.nama AS 'namaTool' FROM eqp_d_boxitem a JOIN eqp_d_toolstock b ON b.id = a.toolStockId JOIN eqp_r_tooltype c ON c.codes = b.toolTypeCode WHERE a.boxId = '"+idbox+"' AND startDate != '0000-00-00 00:00:00'"
    cursor.execute(query)
    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return  make_response(jsonify(json_data),200)