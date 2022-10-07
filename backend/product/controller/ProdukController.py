import db.db_handler as database
from flask import request,make_response,jsonify
import numpy as np
from datetime import datetime, timedelta, date
from math import ceil
import random
import string
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


def GetProdukbyRProyekDSP(id_rproyek):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.id,c.nama AS 'jenisProduk',a.dueDate,d.percentage FROM prd_d_produk a JOIN prd_d_rincianproyek b ON b.id = a.rincianproyek JOIN prd_r_jenisproduk c ON c.id = b.jenisProduk JOIN prd_d_proyek d ON d.id = b.proyek WHERE b.id = '"+id_rproyek+"'"
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

  query = "SELECT a.id,a.rincianProyek FROM prd_d_produk a JOIN prd_d_rincianproyek b ON b.id = a.rincianProyek WHERE a.rincianProyek = '"+id_rproyek+"'"
  cursor.execute(query)
  records = cursor.fetchall()

  row_headers = [x[0] for x in cursor.description]
  json_data = []

  for data in records:
    json_data.append(dict(zip(row_headers,data)))

  return make_response(jsonify(json_data),200)
  
def GetRProyekInProduk(id_rproyek):
  conn = database.connector()
  cursor = conn.cursor()

  query = "SELECT a.id AS 'IdRincian', a.jumlah AS 'jumlah', a.dueDate, b.id AS 'IdProyek', b.nama AS 'NamaProyek', c.id AS 'IdCustomer', c.nama AS 'NamaCustomer' FROM prd_d_rincianproyek a JOIN prd_d_proyek b ON b.id = a.proyek JOIN gen_r_customer c ON c.id = b.customerid WHERE a.id = '"+id_rproyek+"'"
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
  query = "SELECT a.id FROM prd_d_rincianproyek a WHERE a.id = '"+id_rincian+"'"
  cursor.execute(query)
  records = cursor.fetchall()
  temp = ""
  for data in records:
    temp = data[0]
    print(temp)
  
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

    query = "SELECT a.jumlah, b.tglDibuat,a.dueDate FROM prd_d_rincianproyek a JOIN prd_d_proyek b ON b.id = a.proyek JOIN prd_d_produk c ON c.rincianProyek = a.id WHERE c.id = '"+id_produk+"'"
    
    cursor.execute(query)
    records = cursor.fetchall()
    hasilPerkalian = 1        
    tanggalDibuat = ""
    tanggalDueDate = ""
    
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
    
    print(tanggalDibuat)
    tanggalDibuatNew = datetime.strptime(tanggalDibuat,'%Y/%m/%d')

    #tanggalDueDateNew = datetime. strftime(tanggalDueDate)
    
    #hitungHariBisnis = np.busday_count(tanggalDibuatNew.date(),tanggalDueDateNew.date())
    
    #print("Tanggal Proyek Dipesan :", tanggalDibuatNew.strftime("%A"), tanggalDibuatNew)
    #print("Due Date Proyek :", tanggalDueDateNew.strftime("%A"), tanggalDueDateNew)
    #print("Banyak Hari Kerja Antara Dipesan dan Due Date :", hitungHariBisnis)
    #print("Durasi Rincian Proyek :", ceil(hasilPerkalian), "Jam Atau", ceil(durasiHari), "Hari (Sabtu dan Minggu Kerja)")
    newdays = ceil(durasiBaru2)
    print("Durasi Rincian Proyek :",ceil(durasiBaru), "Jam Atau",newdays, "Hari (Sabtu dan Minggu Libur)")
    duedateproduk = tanggalDibuatNew + timedelta(days = newdays)
    print("Due Date Rincian Proyek :",duedateproduk)
    return duedateproduk
