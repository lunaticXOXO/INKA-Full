from datetime import datetime
import db.db_handler as database
from flask import request,make_response,jsonify

def GetAllWorkstation():
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.id, a.nama, a.dibuat, a.berlaku, a.liniproduksi FROM gen_r_stasiunkerja a "
    query = query + "JOIN gen_r_liniproduksi b WHERE a.liniproduksi = b.id"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []
    for data in records:
       json_data.append(dict(zip(row_headers,data)))

    return make_response(jsonify(json_data),200)


def ShowWorkStationbyProcess(id_process):
      conn = database.connector()
      cursor = conn.cursor()

      query = "SELECT a.proses,a.stasiunKerja,c.nama,c.dibuat,c.berlaku,c.liniproduksi FROM gen_r_mampuproses a JOIN prd_r_proses b ON b.id = a.proses JOIN gen_r_stasiunkerja c ON c.id = a.stasiunKerja WHERE a.proses = '"+id_process+"'"
      cursor.execute(query)

      row_headers = [x[0] for x in cursor.description]
      records = cursor.fetchall()
      json_data = []

      for data in records:
            json_data.append(dict(zip(row_headers,data)))
      
      return make_response(jsonify(json_data),200)




def UpdateWorkstation(id):
      conn = database.connector()
      cursor = conn.cursor()

      query = "UPDATE gen_r_stasiunkerja SET id = %s,nama = %s,liniproduksi = %s WHERE id = '"+id+"'"
      try:
            data = request.json
            id = data["id"]
            nama = data["nama"]
            liniproduksi = data["liniproduksi"]

            values = (id,nama,liniproduksi)
            cursor.execute(query,values)
            conn.commit()
            hasil = {"status" : "berhasil"}
      except Exception as e:
            print("Error",str(e))
            hasil = {"status" : "gagal"}
      return hasil

def AddWorkstation():
  conn = database.connector()
  cursor = conn.cursor()

  #id, nama, liniProduksi = input("Input ID : "), input("Input Nama : "), input("Input ID Lini Produksi  : ")

  query = "INSERT INTO gen_r_stasiunkerja (id, nama,dibuat,liniproduksi) VALUES (%s,%s,%s,%s)"
  try:
        data = request.json
        id = data["id"]
        nama = data["nama"]
        dibuat = datetime.now()
        liniproduksi = data["liniproduksi"]
        values = (id, nama,dibuat,liniproduksi)

        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
        print("Workstation Baru Ditambahkan!")
  except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}
  return hasil




def AddWorkStationbyProcess(id_process):
      conn = database.connector()
      cursor = conn.cursor()
      query = "SELECT a.id FROM prd_r_proses a WHERE a.id = '"+id_process+"' LIMIT 1"
      cursor.execute(query)
      records = cursor.fetchall()
      temp = ""
      for data in records:
       temp = data[0]

      query = "INSERT INTO gen_r_mampuproses(proses,stasiunKerja)VALUES(%s,%s)"
      try:
            data = request.json
            stasiunKerja = data["stasiunKerja"]
            values = (temp,stasiunKerja)
            cursor.execute(query,values)
            conn.commit()
            hasil = {"Status" : "Berhasil"}

      except Exception as e:
            print("Error",str(e))
            hasil = {"Status" : "Gagal"}
      return hasil
      

def UpdateWorkstation(id):
  conn = database.connector()
  cursor = conn.cursor()
  query = "UPDATE gen_r_stasiunkerja SET id = %s,nama = %s,berlaku = %s,liniproduksi = %s WHERE id = '"+id+"'"
  try:
      data = request.json
      id = data["id"]
      nama = data["nama"]
      berlaku = data["berlaku"]
      liniproduksi = data["liniproduksi"]
      values = (id,nama,berlaku,liniproduksi)
      cursor.execute(query,values)
      conn.commit()
      hasil = {"Status" : "Berhasil"}
  except Exception as e:
      print("Error",str(e))
      hasil = {"Status" : "Gagal"}
  return hasil
