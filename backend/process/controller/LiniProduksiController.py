from datetime import datetime
import db.db_handler as database
from flask import request,make_response,jsonify
#import process.entity.LiniProduksi as LP

def GetAllLiniProduksi():
  conn = database.connector()
  cursor = conn.cursor()

  query = "SELECT * FROM gen_r_liniproduksi"
  cursor.execute(query)

  records = cursor.fetchall()
  row_headers = [x[0] for x in cursor.description]
  json_data = []
  for data in records:
    json_data.append(dict(zip(row_headers,data)))

  conn.commit()
  return make_response(jsonify(json_data),200)


def AddLiniProduksi():
  conn = database.connector()
  cursor = conn.cursor()

  query = "INSERT INTO gen_r_liniproduksi (id, nama, dibuat) VALUES (%s,%s,%s)"
  try:
    data = request.json
    #LP.LiniProduksi().id   = data["id"]
    #LP.LiniProduksi().nama = data["nama"]
    #LP.LiniProduksi().dibuat = datetime.now()
    #LP.LiniProduksi().dibuat = data["dibuat"]
    #LP.LiniProduksi().berlaku = data["berlaku"]
    #values = (LP.LiniProduksi2().id,LP.LiniProduksi2().nama, LP.LiniProduksi().dibuat,LP.LiniProduksi().berlaku)

    id = data["id"]
    nama = data["nama"] 
    values = (id,nama,datetime.now())
    cursor.execute(query,values)
    conn.commit()
    hasil = {"status" : "berhasil"}
    print("Lini Produksi Baru Ditambahkan!")
  except Exception as e:
      print("Error" + str(e))
      hasil = {"status" : "gagal"}
  return hasil


def StopLiniProduksi(id):
  conn = database.connector()
  cursor = conn.cursor()
  now = datetime.now()
  query = "UPDATE gen_r_liniproduksi SET berlaku = '"+str(now)+"'WHERE id = '"+id+"'"
  try:
    cursor.execute(query)
    conn.commit()
    hasil = {"status" : "berhasil"}
  except Exception as e:
      print("Error" + str(e))
      hasil = {"status" : "gagal"}
  return hasil

#Update Lini Produksi