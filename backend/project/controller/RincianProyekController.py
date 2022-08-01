from math import ceil
from process.controller.ProsesController import HitungDurasiProses
import db.db_handler as db
import numpy as np
from datetime import timedelta
from flask import request,make_response,jsonify

def GetAllRincianProyek():
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM prd_r_rincianproyek"
   
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    data_json = []

    for data in records:
        data_json.append(dict(zip(row_headers,data)))
    return make_response(jsonify(data_json),200)


def ShowRincianProyekByProyek(id_proyek):
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT a.id,a.jumlah,a.dueDate,a.proyek,a.jenisProduk FROM prd_r_rincianproyek a JOIN prd_r_proyek b ON a.proyek = b.id WHERE b.id = '"+id_proyek+"'"
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)


def ShowProyekInRProyek(id_proyek):
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT a.id AS 'IdProyek', a.nama AS 'NamaProyek', b.id AS 'IdCustomer', b.nama AS 'NamaCustomer' FROM prd_r_proyek a JOIN gen_r_customer b ON b.id = a.customerid WHERE a.id =  '"+id_proyek+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)

def AddRincianProyek():
    conn = db.connector()
    cursor = conn.cursor()

    query = "INSERT INTO prd_r_rincianproyek(id,jumlah,dueDate,jenisProduk,proyek)VALUES(%s,%s,%s,%s,%s)"
    try:
        data = request.json
        id = data["id"]
        jumlah = data["jumlah"]
        dueDate = data["dueDate"]
        jenisProduk = data["jenisProduk"]
        proyek = data["proyek"]
        values = (id,jumlah,dueDate,jenisProduk,proyek)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"Status" : "Berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"Status" : "Gagal"}

    return hasil


def AddRincianProyekByProyek(id_proyek):
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT a.id FROM prd_r_proyek a WHERE a.id = '"+id_proyek+"' LIMIT 1"

    cursor.execute(query)
    records = cursor.fetchall()
    temp = ""
    for index in records:
        temp = index[0]
    
    print(temp)
    print(type(temp))
    cursor = conn.cursor()
    query = "INSERT INTO prd_r_rincianproyek (id, jumlah,jenisProduk, proyek) VALUES (%s,%s,%s,'"+temp+"')"
    try:
        data = request.json
        id_rproyek = data["id"]
        jumlah = data["jumlah"]
        jenisProduk = data["jenisProduk"]
    
        values = (id_rproyek,jumlah,jenisProduk)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
        print("Rincian Proyek Baru Ditambahkan!")

    except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}
    
    return hasil


def UpdateRProyek(id_rproyek):
    conn = db.connector()
    cursor = conn.cursor()
    query = "UPDATE prd_r_rincianproyek SET jumlah = %s,proyek = %s,jenisProduk = %s WHERE id = '"+id_rproyek+"'"
    try:
        data = request.json
        jumlah = data["jumlah"]
        proyek = data["proyek"]
        jenisProduk = data["jenisProduk"]
        values = (jumlah,proyek,jenisProduk)

        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}
    
    return hasil



def HitungDueDateRProyek(id_produk):
    hasil1 = HitungDurasiProses(id_produk)

    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT a.jumlah, b.tglDibuat, b.dueDate FROM prd_r_rincianproyek a "
    query = query + "JOIN prd_r_proyek b ON "
    query = query + "b.id = a.proyek"
    query = query + "JOIN prd_d_produk c ON"
    query = query + "c.rincianProyek = a.id"
    query = query + "WHERE c.id = '"+id_produk+"'"
    
    cursor.execute(query)

    records = cursor.fetchall()
    hasilPerkalian = 1        
    
    for data in records:
        print("Jumlah Pesanan :",data[0], "Produk")
        data[1]
        data[2]
       
        hasilPerkalian = data[0]
        tanggalDibuat  =  data[1]
        tanggalDueDate = data[2]
   
    hasilPerkalian = hasilPerkalian * hasil1
    durasiHari = hasilPerkalian / 8
    sabtuMingguDalamSebulan = (16 * 4)
    durasiBaru = hasilPerkalian + sabtuMingguDalamSebulan
    durasiBaru2 = durasiBaru / 8

    hitungHariBisnis = np.busday_count(tanggalDibuat,tanggalDueDate)

    print("Tanggal Proyek Dipesan :", tanggalDibuat.strftime("%A"), tanggalDibuat)
    print("Due Date Proyek :", tanggalDueDate.strftime("%A"), tanggalDueDate)
    print("Banyak Hari Kerja Antara Dipesan dan Due Date :", hitungHariBisnis)
    print("Durasi Rincian Proyek :", ceil(hasilPerkalian), "Jam Atau", ceil(durasiHari), "Hari (Sabtu dan Minggu Kerja)")
    newdays = ceil(durasiBaru2)
    print("Durasi Rincian Proyek :",ceil(durasiBaru), "Jam Atau",newdays, "Hari (Sabtu dan Minggu Libur)")
    duedateproyek = tanggalDibuat + timedelta(days = newdays)
    print(type(duedateproyek))
    print("Due Date Rincian Proyek :",duedateproyek)
    return duedateproyek
    #return make_response(jsonify(duedateproyek),200)


def UpdateDueDateRProyek(id_proyek):
    tanggal = HitungDueDateRProyek(id_proyek)
    conn = db.connector()
    try:
        cursor = conn.cursor()
        query = "UPDATE prd_r_rincianproyek SET dueDate = '"+str(tanggal)+"' WHERE proyek = '"+id_proyek+"'"
        cursor.execute(query)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}
    
    return hasil
    

