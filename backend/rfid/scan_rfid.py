import db.db_handler as database
from flask import request,make_response,jsonify

def ScanRFID():
  conn = database.connector()
  cursor = conn.cursor()
  
  query = "INSERT INTO cpl_matlogin (stasiunKerja, idMat) VALUES (%s,%s)"
  try:
      data = request.json
      stasiunKerja = data["stasiunKerja"]
      idMat = data["idMat"]
      values = (stasiunKerja, idMat)
      cursor.execute(query,values)
      conn.commit()
      hasil = {"Status " : "berhasil"}
  except Exception as e:
      print("Error" + str(e))
      hasil = {"Status" : "gagal"}

  return hasil