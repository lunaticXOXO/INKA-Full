from cgi import print_directory
from math import ceil
from process.controller.ProsesController import HitungDurasiProses
import db.db_handler as db
import numpy as np
from datetime import timedelta
from flask import request,make_response,jsonify
import random
import string
import datetime
import time

def GetAllRincianProyek():
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM prd_d_rincianproyek"
   
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    data_json = []

    for data in records:
        data_json.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(data_json),200)


def ShowRincianProyekByProyek(id_proyek):
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT a.id,a.jumlah,a.dueDate,a.proyek,c.nama FROM prd_d_rincianproyek a JOIN prd_d_proyek b ON a.proyek = b.id JOIN prd_r_jenisproduk c ON c.id = a.jenisProduk WHERE b.id = '"+id_proyek+"' ORDER BY a.id DESC"
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def ShowProyekInRProyek(id_proyek):
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT a.id AS 'IdProyek', a.nama AS 'NamaProyek', b.id AS 'IdCustomer', b.nama AS 'NamaCustomer' FROM prd_d_proyek a JOIN gen_r_customer b ON b.id = a.customerid WHERE a.id =  '"+id_proyek+"'"
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

    query = "INSERT INTO prd_d_rincianproyek(id,jumlah,dueDate,jenisProduk,proyek)VALUES(%s,%s,%s,%s,%s)"
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
        cursor.close()
        conn.close()
        hasil = {"Status" : "Berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"Status" : "Gagal"}

    return hasil


def AddRincianProyekByProyek(id_proyek):
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT a.id FROM prd_d_proyek a WHERE a.id = '"+id_proyek+"' LIMIT 1"

    cursor.execute(query)
    records = cursor.fetchall()
    temp = ""
    for index in records:
        temp = index[0]
    
    print("ID Proyek : ",temp)
    print(type(temp))
    #P00000
    angka_awal = '00'
    
    id_rproyek_new = ""
    
    query_get_rproyekbyproyek = "SELECT a.id FROM prd_d_rincianproyek a JOIN prd_d_proyek b ON b.id = a.proyek WHERE b.id = '"+id_proyek+"'"
    cursor.execute(query_get_rproyekbyproyek)
    records_rinci = cursor.fetchall()
    angka_akhir = 0

    temp2 = ""
    for index2 in records_rinci:
        temp2 = index2[0]

    print(temp2)
    if temp2 == '':
        print("test")
        id_rproyek_new = temp + "000"
    else:
        angka_akhir_str = ""
        for index in records_rinci:
            print("Angka : ",angka_akhir)

            if angka_akhir >= 9:
                angka_awal = '0'
                angka_akhir = angka_akhir + 1
                angka_akhir_str = str(angka_akhir)
                id_rproyek_new = temp + angka_awal + angka_akhir_str
                print("test")

            else:
                angka_akhir = angka_akhir + 1
                angka_akhir_str = str(angka_akhir)
                id_rproyek_new = temp + angka_awal + angka_akhir_str
       

    cursor = conn.cursor()
    query = "INSERT INTO prd_d_rincianproyek (id, jumlah,dueDate,jenisProduk, proyek) VALUES (%s,%s,%s,%s,'"+temp+"')"
    try:
        data = request.json
        #id_rproyek = data["id"]
        jumlah = data["jumlah"]
        dueDate = data["gabunganTanggal"]
        jenisProduk = data["jenisProduk"]
    
        values = (id_rproyek_new,jumlah,str(dueDate),jenisProduk)
        cursor.execute(query,values)
       
        conn.commit()
         
        cursor.close()
        conn.close()

        boolean = True
        counter = 1
        counter2 = 0

        while boolean :
            f = open("C:\\Users\Rispro LPDP\operasi04\demofile3.txt", "r")
            read = f.read()
            print("nilai : ",read)
            if read == '0':
                boolean = True

            if read == '1' and counter == 1 :
                counter  = 1
                counter2 = counter2 + 1
            
            if read == '1' and counter2 > counter:    
                boolean = False
                break
            print("counter1 : ",counter)
            print("counter2 : ", counter2)
            time.sleep(5)
        hasil = {"status" : "berhasil"}

        print("Rincian Proyek Baru Ditambahkan!")

    except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}
    
    return hasil


def GetFirstOperation():
    conn = db.connector()
    cursor = conn.cursor()
    query = "SELECT a.id,a.rencanaMulai FROM prd_d_operasi a WHERE confirm IS NULL ORDER BY a.rencanaMulai ASC LIMIT 1"
    cursor.execute(query)
    records = cursor.fetchall()
    keterangan2 = ""
    headers = "keterangan"
   
    for index in records:
        renmul = index[1]
        if renmul < datetime.datetime.now():
            keterangan2 = "Terlambat"
        elif renmul > datetime.datetime.now():
            keterangan2 = "Tepat"

    row_headers = [x[0] for x in cursor.description]

    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200) 


def GetFirstOperationDsc():
    conn = db.connector()
    cursor = conn.cursor()
    query = "SELECT a.id,a.rencanaMulai FROM prd_d_operasi a WHERE confirm IS NULL ORDER BY a.rencanaMulai ASC LIMIT 1"
    cursor.execute(query)
    records = cursor.fetchall()
    keterangan2 = []
   
    for index in records:
        renmul = index[1]
        if renmul < datetime.datetime.now():
            keterangan2 = "Terlambat"
        elif renmul > datetime.datetime.now():
            keterangan2 = "Tepat"
    
    print(keterangan2)

    return make_response(jsonify(keterangan2),200) 


def GenerateSNProduct():
    N = 9
    id_product = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
    return id_product


def UpdateRProyek(id_rproyek):
    conn = db.connector()
    cursor = conn.cursor()
    query = "UPDATE prd_d_rincianproyek SET jumlah = %s,proyek = %s,jenisProduk = %s WHERE id = '"+id_rproyek+"'"
    try:
        data = request.json
        jumlah = data["jumlah"]
        proyek = data["proyek"]
        jenisProduk = data["jenisProduk"]
        values = (jumlah,proyek,jenisProduk)

        cursor.execute(query,values)
        conn.commit()

        cursor.close()
        conn.close()

        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}
    
    return hasil



def TerimaOperasi():
    conn = db.connector()
    cursor = conn.cursor()
    try:
        query_accept_rinci = "UPDATE prd_d_rincianproyek SET confirm = 1 WHERE confirm IS NULL"
        query_accept_product = "UPDATE prd_d_produk SET confirm = 1 WHERE confirm IS NULL"
        query_accept_operasi = "UPDATE prd_d_operasi SET confirm = 1 WHERE confirm IS NULL"
        query_accept_cpl_produk = "UPDATE cpl_produk SET confirm = 1 WHERE confirm IS NULL"
        query_accept_cplrinci = "UPDATE cpl_rinciproyek SET confirm = 1 WHERE confirm IS NULL"

        cursor.execute(query_accept_rinci)
        cursor.execute(query_accept_product)
        cursor.execute(query_accept_operasi)
        cursor.execute(query_accept_cpl_produk)
        cursor.execute(query_accept_cplrinci)
        conn.commit()
        hasil = {"status" : "berhasil"}
        
    except Exception as e:
        hasil = {"status" : "gagal"}
        print("Error",str(e))
    return hasil


def BatalOperasi():
    conn = db.connector()
    cursor = conn.cursor()
    try:
        query_delete_cplrinci = "DELETE FROM cpl_rinciproyek WHERE confirm IS NULL"
        query_delete_cplproduk = "DELETE FROM cpl_produk WHERE confirm IS NULL"
        query_delete_operasi  = "DELETE FROM prd_d_operasi WHERE confirm IS NULL"
        query_delete_produk = "DELETE FROM prd_d_produk WHERE confirm IS NULL"
        query_delete_rinci = "DELETE FROM prd_d_rincianproyek WHERE confirm IS NULL"
        query_delete_proyek = "DELETE FROM prd_d_proyek WHERE confirm != 1 OR customerid IS NULL"
        cursor.execute(query_delete_cplrinci)
        cursor.execute(query_delete_cplproduk)
        cursor.execute(query_delete_operasi)
        cursor.execute(query_delete_produk)
        cursor.execute(query_delete_rinci)
        cursor.execute(query_delete_proyek)
        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil

def fetchOperatorQualification():
    conn = db.connector()
    recordsqualification = []
    cursor = conn.cursor()
    query7 = "SELECT a.operatorid,a.qualificationCode,b.descriptions FROM opr_d_operatorlevel a JOIN opr_r_operatorqualification b ON b.codes = a.qualificationCode"
    cursor.execute(query7)
    recordsqualification = cursor.fetchall()
    print(recordsqualification)
    return recordsqualification




def fetchProcesstoOperation(idProduk):
   
    conn = db.connector()
    cursor = conn.cursor()
    query3 = "SELECT c.id AS 'IdProses',a.stasiunKerja,c.durasi,i.qualificationCode FROM gen_r_mampuproses a JOIN prd_r_proses c ON c.id = a.proses JOIN prd_r_strukturjnsprd d ON d.idNodal = c.nodalOutput JOIN prd_r_jenisproduk e ON e.id = d.jnsProduk JOIN prd_d_rincianproyek f ON f.jenisProduk = e.id JOIN prd_d_proyek g ON g.id = f.proyek JOIN prd_d_produk h ON h.rincianProyek = f.id JOIN prd_r_operatorrequirement i ON i.processCode = c.id WHERE h.id = '"+idProduk+"'ORDER BY c.id DESC"
    cursor.execute(query3)
   
    recordsFetch = cursor.fetchall()
  
    print("Records Fetch : ",recordsFetch)
    return recordsFetch


def fetchRequirementsCode(idProduk):
    
    datafetch = []
    requirementsCode = ''
    datafetch = fetchProcesstoOperation(idProduk)
    for index in datafetch:
        requirementsCode = index[3]
    return requirementsCode


def fetchDateProyektoOperation(idProduk):
   
    conn = db.connector()
    recorddate = []
    cursor = conn.cursor()
    query5 = "SELECT a.tglDibuat FROM prd_d_proyek a JOIN prd_d_rincianproyek b ON b.proyek = a.id JOIN prd_d_produk c ON c.rincianProyek = b.id WHERE c.id = '"+idProduk+"'"
    cursor.execute(query5)
    recorddate = cursor.fetchall()
    return recorddate

def fetchSchedulledStart(idProduk):
    
    recordDate = []
    schedulledstartWorkDate = ""
    recordDate = fetchDateProyektoOperation(idProduk)
    for data in recordDate:
        schedulledstartWorkDate = data[0]
    return schedulledstartWorkDate


def fetchSchedulledFinish(idProduk):
    
    recordDate = []
    scehdulledFinishWorkDate = ""
    recordDate = fetchDateProyektoOperation(idProduk)
    for data in recordDate:
       scehdulledFinishWorkDate = data[0]
    return scehdulledFinishWorkDate

    

def GenerateOperation(idProduk):
    conn = db.connector()
    cursor = conn.cursor()
    N = 9
    counter=1
    print("ID Product : ",idProduk)
    proses = ""   
    stasiunKerja = ""
    recordsFetch = []
    records_oprqualification = []

    query = "INSERT INTO prd_d_operasi(id,rencanaMulai,rencanaSelesai,proses,stasiunKerja,produk)VALUES(%s,%s,%s,%s,%s,%s)"
    query_insert_operatorneed = "INSERT INTO opr_d_operatorneed(operationid,operatorid)VALUES(%s,%s)"     
    
    try:
        recordsFetch = fetchProcesstoOperation(idProduk)
        records_oprqualification = fetchOperatorQualification()
        schedulledstartWorkDate = fetchSchedulledStart(idProduk)
        schedulledFinishWorkDate = fetchSchedulledFinish(idProduk)
       
        print(recordsFetch)
      
        for index in recordsFetch:
            id_operation = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
            proses = index[0]
            stasiunKerja = index[1]
            durasi = index[2]
            requirementsCode = index[3]
            cek = False 
            while cek == False:
                if counter % 2 != 0 and cek == False:
                    schedulledFinishWorkDate = schedulledFinishWorkDate + datetime.timedelta(minutes = durasi)
                    values1 = (id_operation,schedulledstartWorkDate,schedulledFinishWorkDate,proses,stasiunKerja,idProduk)
                    cursor.execute(query,values1)
                    schedulledstartWorkDate = schedulledFinishWorkDate
                    for index2 in records_oprqualification:
                        operatorid = index2[0]
                        qualificationCode = index2[1]
                        if qualificationCode == requirementsCode:
                            values_oprneed = (id_operation,operatorid)
                            cursor.execute(query_insert_operatorneed,values_oprneed)
                   
                    cek = True 
                elif counter %2 == 0 and cek == False:
                    schedulledFinishWorkDate = schedulledFinishWorkDate + datetime.timedelta(minutes = durasi)
                    cursor.execute(query,values1)
                    schedulledstartWorkDate = schedulledFinishWorkDate
                    for index2 in records_oprqualification:
                        operatorid = index2[0]
                        qualificationCode = index2[1]
                        if qualificationCode == requirementsCode:
                            values_oprneed = (id_operation,operatorid)
                            cursor.execute(query_insert_operatorneed,values_oprneed)
                    cek = True
        counter = counter + 1
        conn.commit()
        conn.close()
        hasil = {"status" : "berhasil"}
        print(hasil)
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def HitungDueDateRProyek(id_produk):
    hasil1 = HitungDurasiProses(id_produk)

    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT a.jumlah, b.tglDibuat, b.dueDate FROM prd_d_rincianproyek a "
    query = query + "JOIN prd_d_proyek b ON "
    query = query + "b.id = a.proyek"
    query = query + "JOIN prd_d_produk c ON"
    query = query + "c.rincianProyek = a.id"
    query = query + "WHERE c.id = '"+id_produk+"'"
    
    cursor.execute(query)

    records = cursor.fetchall()
    hasilPerkalian = 1        
    tanggalDibuat = ""
    tanggalDueDate = ""

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

    cursor.close()
    conn.close()

    return duedateproyek

    #return make_response(jsonify(duedateproyek),200)


def UpdateDueDateRProyek(id_proyek):
    tanggal = HitungDueDateRProyek(id_proyek)
    conn = db.connector()
    try:
        cursor = conn.cursor()
        query = "UPDATE prd_d_rincianproyek SET dueDate = '"+str(tanggal)+"' WHERE proyek = '"+id_proyek+"'"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}
    
    return hasil
    

