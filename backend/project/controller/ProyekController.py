from project.controller.RincianProyekController import *
from datetime import datetime
import db.db_handler as database
from flask import request,make_response,jsonify

def GetAllProyek():
  conn = database.connector()
  cursor = conn.cursor()

  query = "SELECT * FROM prd_r_proyek"
  cursor.execute(query)

  row_headers = [x[0] for x in cursor.description]
  records = cursor.fetchall()
  json_data = []

  for data in records:
      json_data.append(dict(zip(row_headers,data)))

  conn.commit()
  return make_response(jsonify(json_data),200)

def GetProyekByCustomer(id):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.id,a.nama,a.tglDibuat,a.customerid FROM prd_r_proyek a JOIN gen_r_customer b ON b.id = a.customerid WHERE a.customerid = '"+id+"'"
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    conn.commit()
    return make_response(jsonify(json_data),200)

### Ga kepake
def AddProyek():
  conn = database.connector()
  cursor = conn.cursor()
  
  query = "INSERT INTO prd_r_proyek (id, nama,tglDibuat,customerid) VALUES (%s,%s,%s,%s)"
  try:
      data = request.json
      id_proyek = data["id"]
      nama_proyek = data["nama"]
     
      customerid = data['customerid']
      values = (id_proyek,nama_proyek,datetime.now(),customerid)
      cursor.execute(query,values)
      conn.commit()
      hasil = {"Status " : "Berhasil"}
  except Exception as e:
      print("Error" + str(e))
      hasil = {"Status" : "Gagal"}

  return hasil
###################

def GetCustomerInProyek(idCustomer):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id AS 'IdCustomer',a.nama AS 'NamaCustomer' FROM gen_r_customer a WHERE a.id = '"+idCustomer+"'"
    cursor.execute(query)

    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)

def AddProyekbyCustomer(id_customer):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id FROM gen_r_customer a WHERE a.id = '"+id_customer+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    temp = ""
    for data in records:
        temp = data[0]
   
    query = "INSERT INTO prd_r_proyek(id,nama,tglDibuat,customerid)VALUES(%s,%s,%s,'"+temp+"')"
    try:
        data = request.json
        id = data["id"]
        nama = data["nama"]
        now = datetime.now()
        values = (id,nama,now)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "berhasil"}
    return hasil



def UpdateProyek(id):
    conn = database.connector()
    query = "UPDATE prd_r_proyek SET id = %s,nama = %s,customerid = %s WHERE id = '"+id+"'"
    try:
        data = request.json
        id = data["id"]
        nama_proyek = data["nama"]
        customerid = data["customerid"]
        cursor = conn.cursor()
        values = (id,nama_proyek,customerid)

        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}

    return hasil
  