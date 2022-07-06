import db.db_handler as database
from flask import request,make_response,jsonify

def GetAllProduk():
  conn = database.connector()
  cursor = conn.cursor()

  query = "SELECT * FROM prd_d_produk"
  cursor.execute(query)

  records = cursor.fetchall()
  row_headers = [x[0] for x in cursor.description]
  json_data = []
 
  for data in records:
    json_data.append(dict(zip(row_headers,data)))
  
  return  make_response(jsonify(json_data),200)


def GetProdukbyRProyek(id_rproyek):
  conn = database.connector()
  cursor = conn.cursor()

  query = "SELECT a.id,a.rincianProyek FROM prd_d_produk a JOIN prd_r_rincianproyek b ON b.id = a.rincianProyek WHERE a.rincianProyek = '"+id_rproyek+"'"
  cursor.execute(query)
  records = cursor.fetchall()

  row_headers = [x[0] for x in cursor.description]
  json_data = []

  for data in records:
    json_data.append(dict(zip(row_headers,data)))

  return make_response(jsonify(json_data),200)
  


def AddProduk():
  conn = database.connector()
  cursor = conn.cursor()

  query = "INSERT INTO prd_d_produk(id,rincianProyek)VALUES(%s,%s)"
  try:
    data = request.json
    id = data["id"]
    rincianProyek = data["rincianProyek"]
    values = (id,rincianProyek)
    cursor.execute(query,values)
    conn.commit()
    hasil = {"Status" : "Berhasil"}

  except Exception as e:
    print("Error",str(e))
    hasil = {"Status" : "Gagal"}
  return hasil


def AddProdukbyRincian(id_rincian):
  conn = database.connector()
  cursor = conn.cursor()
  query = "SELECT a.rincianProyek FROM prd_d_produk a JOIN prd_r_rincianproyek b ON a.rincianProyek = b.id WHERE a.rincianProyek = '"+id_rincian+"' LIMIT 1"
  cursor.execute(query)
  records = cursor.fetchall()
  temp = ""
  for data in records:
    temp = data[0]
  
  query = "INSERT INTO prd_d_produk(id,rincianProyek)VALUES(%s,%s)"
  try:
    data = request.json
    id = data["id"]
    values = (id,temp)
    cursor.execute(query,values)
    conn.commit()
    hasil = {"Status" : "Berhasil"}
    
  except Exception as e:
    print("Error",str(e))
    hasil = {"Status" : "Gagal"}
  return hasil
  

def ShowDueDateProduct():
  conn = database.connector()
  cursor = conn.cursor()
  


  
