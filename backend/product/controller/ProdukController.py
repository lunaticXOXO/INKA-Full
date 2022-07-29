import db.db_handler as database
from flask import request,make_response,jsonify
import numpy as np
from datetime import datetime, timedelta
from math import ceil
from process.controller.ProsesController import *


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
  

def HitungDueDateProduk(id_produk):
    hasil1 = HitungDurasiProsesbyProduk(id_produk)
    print(hasil1)
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.jumlah, b.tglDibuat,a.dueDate FROM prd_r_rincianproyek a JOIN prd_r_proyek b ON b.id = a.proyek JOIN prd_d_produk c ON c.rincianProyek = a.id WHERE c.id = '"+id_produk+"'"
    
    cursor.execute(query)
    records = cursor.fetchall()
    hasilPerkalian = 1        

    
    print("test")
    for data in records:
        print("Jumlah Pesanan :",data[0], "Produk")
        print(data[1])
        print(data[2])
        hasilPerkalian =  data[0]
        tanggalDibuat  =  data[1]
        tanggalDueDate = data[2]
   
    hasilPerkalian = hasilPerkalian * hasil1
    #print(hasilPerkalian)
    durasiHari = hasilPerkalian / 8
    sabtuMingguDalamSebulan = (16 * 4)
    durasiBaru = hasilPerkalian + sabtuMingguDalamSebulan
    durasiBaru2 = durasiBaru / 8
    tanggalDibuatNew = tanggalDibuat.date()
    tanggalDueDateNew = tanggalDueDate.date()
    
    hitungHariBisnis = np.busday_count(tanggalDibuatNew,tanggalDueDateNew)
    
    print("Tanggal Proyek Dipesan :", tanggalDibuatNew.strftime("%A"), tanggalDibuatNew)
    print("Due Date Proyek :", tanggalDueDateNew.strftime("%A"), tanggalDueDateNew)
    print("Banyak Hari Kerja Antara Dipesan dan Due Date :", hitungHariBisnis)
    print("Durasi Rincian Proyek :", ceil(hasilPerkalian), "Jam Atau", ceil(durasiHari), "Hari (Sabtu dan Minggu Kerja)")
    newdays = ceil(durasiBaru2)
    print("Durasi Rincian Proyek :",ceil(durasiBaru), "Jam Atau",newdays, "Hari (Sabtu dan Minggu Libur)")
    duedateproduk = tanggalDibuatNew + timedelta(days = newdays)
    print("Due Date Rincian Proyek :",duedateproduk)
    return duedateproduk

  
  
