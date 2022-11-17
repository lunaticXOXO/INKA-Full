import db.db_handler as database
from datetime import datetime
from flask import request,make_response,jsonify

def ScanBarcodeRFID():
  conn = database.connector()
  cursor = conn.cursor()
  
  query = "INSERT INTO cpl_matlogin (stasiunKerja, idMat, waktu) VALUES (%s,%s,%s)"
  try:
      data = request.json
      stasiunKerja = data["stasiunKerja"]
      idMat = data["idMat"]
      waktu = datetime.now()
      values = (stasiunKerja, idMat, waktu)
      cursor.execute(query,values)
      conn.commit()
      hasil = {"status" : "berhasil"}
  except Exception as e:
      print("Error" + str(e))
      hasil = {"status" : "gagal"}

  return hasil