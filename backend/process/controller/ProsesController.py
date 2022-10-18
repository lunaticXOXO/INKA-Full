from math import ceil
from signal import valid_signals
from tkinter.messagebox import QUESTION
import pandas as pd
import product.controller.JenisProdukController as jpcont
import product.controller.StrukturJenisProdukController as sjpcont
from flask import request,make_response,jsonify
import db.db_handler as database

def ShowProses():
    conn = database.connector()
    cursor = conn.cursor()
    #data = request.json
    query = "SELECT a.id,a.jenisProses,a.prosesSesudahnya,a.nama,a.durasi,a.satuanDurasi," 
    query += "c.idNodal FROM prd_r_proses a "
    query += "JOIN prd_r_strukturjnsprd c ON c.idNodal = a.nodalOutput"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []
    for data in records:
       json_data.append(dict(zip(row_headers,data)))
    #conn.commit()

    return make_response(jsonify(json_data),200)

def ShowJenisProses():
    conn = database.connector()
    cursor = conn.cursor()
    #data = request.json
    query = "SELECT * FROM prd_r_jenisproses"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []
    for data in records:
       json_data.append(dict(zip(row_headers,data)))
  
    return make_response(jsonify(json_data),200)


def AddRequirementByProcess(id):
    conn = database.connector()
    cursor = conn.cursor()
    query_select = "SELECT id FROM prd_r_proses WHERE id = '"+id+"'"
    cursor.execute(query_select)
    records = cursor.fetchall()
    id_proses = ""
    for data in records:
        id_proses = data[0]

    query_insert = "INSERT INTO prd_r_operatorrequirement(qualificationCode,processCode)VALUES(%s,%s)"
    try:
        data = request.json
        qualificationCode = data["qualificationCode"]
        values = (qualificationCode,id_proses)
        cursor.execute(query_insert,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def ShowRequirementProcess():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.processCode AS 'IdProses',b.nama AS 'NamaProses',c.codes AS 'RequirementCode',c.descriptions FROM prd_r_operatorrequirement a JOIN prd_r_proses b ON b.id = a.processCode JOIN opr_r_operatorqualification c ON c.codes = a.qualificationCode"
    cursor.execute(query)
    records = cursor.fetchall()

    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)



def ShowRequirmentByIdProcess(idProcess):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.processCode AS 'IdProses', b.nama AS 'NamaProses', c.codes AS 'RequirementCode', c.descriptions FROM prd_r_operatorrequirement a JOIN prd_r_proses b ON b.id = a.processCode JOIN opr_r_operatorqualification c ON c.codes = a.qualificationCode WHERE a.processCode = '"+idProcess+"'"
    cursor.execute(query)
    records = cursor.fetchall()

    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)



def InsertJenisProses():
    conn = database.connector()
    cursor = conn.cursor()
    try:
        data = request.json
        query = "INSERT INTO prd_r_jenisproses(id,namajenisproses)VALUES(%s,%s)"
        id = data["id"]
        namajenisproses = data["namajenisproses"]
        values = (id,namajenisproses)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def ShowGroupProses():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM prd_r_prosesgroup"

    cursor.execute(query)
    records = cursor.fetchall()

    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data))


def InsertGroupProses():
    conn = database.connector()
    cursor = conn.cursor()

    query = "INSERT prd_r_prosesgroup(id,nama)VALUES(%s,%s)"
    try:
        data = request.json
        id = data["id"]
        nama = data["nama"]
        values = (id,nama)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil



def ShowSJProdukInProcess(id_sjproduk):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.idNodal,a.nama,a.indukNodal, c.id AS 'IdJenisProduk', c.nama AS 'NamaJenisProduk', d.id AS 'IdRincian',d.jumlah,d.dueDate AS 'dueDateRincian', e.id AS 'IdProduk',e.dueDate AS 'dueDateProduk', f.id AS 'IdProyek',f.nama AS 'namaProyek', g.id AS 'IdCustomer',g.nama AS 'namaCustomer' FROM prd_r_strukturjnsprd a JOIN prd_r_jenisproduk c ON c.id = a.jnsProduk JOIN prd_d_rincianproyek d ON d.jenisProduk = c.id JOIN prd_d_produk e ON e.rincianProyek = d.id JOIN prd_d_proyek f ON f.id = d.proyek JOIN gen_r_customer g ON g.id = f.customerid WHERE a.idNodal = '"+id_sjproduk+"'"

    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    
    records = cursor.fetchall()
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)



def ShowProsesbySJProduk(idNodal):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id, a.nama, a.durasi, a.satuanDurasi,a.jenisProses,a.prosesSesudahnya, c.idNodal FROM prd_r_proses a JOIN prd_r_strukturjnsprd c ON c.idNodal = a.nodalOutput WHERE a.nodalOutput = '"+idNodal+"'"
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    records = cursor.fetchall()
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)


def OffForeign():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SET GLOBAL FOREIGN_KEY_CHECKS = 0;"
    cursor.execute(query)




def OnForeign(): 
    conn = database.connector()
    cursor = conn.cursor()
    query = "SET GLOBAL FOREIGN_KEY_CHECKS = 1;"
    cursor.execute(query)

     


def AddProses():
    OffForeign()
    conn = database.connector()
    cursor = conn.cursor()

   
    query  = "INSERT INTO prd_r_proses(id,prosesSesudahnya,nodalOutput,nama,durasi,satuanDurasi,jenisProses)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    
    try:
        data = request.json
        idProses = data["id"]
        prosesSesudahnya = data["prosesSesudahnya"]
        nodalOutput = data["nodalOutput"]
        nama = data["nama"]
        durasi = data["durasi"]
        satuanDurasi = data["satuanDurasi"]
        jenisProses = data["jenisProses"]

        values = (idProses, prosesSesudahnya, nodalOutput, nama,durasi, satuanDurasi,jenisProses)

        cursor.execute(query,values)
        conn.commit()
        print("Proses Baru Ditambahkan!")
        hasil = {"status" : "berhasil"}
        
        cursor2 = conn.cursor()
        query2 = "SET GLOBAL FOREIGN_KEY_CHECKS = 1;"
        cursor2.execute(query2)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}
        
    return hasil


def AddProcessBySJProduk(id_sjproduk):
    OffForeign()
    conn = database.connector()
    cursor1 = conn.cursor()
    
    query = "SELECT a.idNodal FROM prd_r_strukturjnsprd a WHERE a.idNodal = '"+id_sjproduk+"' LIMIT 1"
    cursor1.execute(query)

    temp = ""
    records_sjproduk = cursor1.fetchall()
    for index in records_sjproduk:
       temp = index[0]
       print(temp)

  
    query = "INSERT INTO prd_r_proses(id,prosesSesudahnya,nodalOutput,nama,durasi,satuanDurasi,jenisProses)VALUES(%s,%s,'"+temp+"',%s,%s,%s,%s);"
    #query = query + "SET FOREIGN_KEY_CHECKS = 1;"

    try:
        data = request.json
        idProses = data["id"]
        prosesSesudah = data["prosesSesudahnya"]
        nama = data["nama"]
        durasi = data["durasi"]
        satuanDurasi = data["satuanDurasi"]
        jenisProses = data["jenisProses"]
        values = (idProses,prosesSesudah,nama,durasi,satuanDurasi,jenisProses)        
        cursor1.execute(query,values)
        #conn.commit()
       
        #conn2 = database.connector()
        cursor2 = conn.cursor()
        query2 = "SET GLOBAL FOREIGN_KEY_CHECKS = 1;"
        cursor2.execute(query2)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error" + str(e))
        hasil = {"status" : "gagal"}

    return hasil


def HitungDurasiProsesbyProduk(id_produk):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.id, a.nama, b.idNodal, b.nama, b.jumlah, c.id, c.nama, c.durasi, c.satuandurasi, d.id, d.jumlah, e.id, e.nama, e.tglDibuat, f.id AS 'ID Produk' FROM prd_r_jenisproduk a JOIN prd_r_strukturjnsprd b ON b.jnsProduk = a.id JOIN prd_r_proses c ON c.nodalOutput = b.idNodal JOIN prd_d_rincianproyek d ON d.jenisProduk = a.id JOIN prd_d_proyek e ON e.id = d.proyek JOIN prd_d_produk f ON f.rincianProyek = d.id WHERE f.id = '"+id_produk+"'"
    cursor.execute(query)
    records = cursor.fetchall()

    hitungDurasi = 0
    
    for data in records:
        hitungDurasi = hitungDurasi + data[7]
    
    hitungJam = hitungDurasi/60
    print("Durasi :", ceil(hitungJam), "Jam Per Produk")

    return ceil(hitungJam)


def HitungDurasiProses(id_proyek):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT "
    query = query + "a.id, a.nama,"
    query = query + "b.idNodal, b.nama, b.jumlah,"
    query = query + "c.id, c.nama, c.durasi, c.satuandurasi,"
    query = query + "d.id, d.jumlah,"
    query = query + "e.id, e.nama, e.tglDibuat "
    query = query + "FROM prd_r_jenisproduk a "
    query = query + "JOIN prd_r_strukturjnsprd b ON b.jnsProduk = a.id "
    query = query + "JOIN prd_r_proses c ON c.nodalOutput = b.idNodal "
    query = query + "JOIN prd_d_rincianproyek d ON d.jenisProduk = a.id "
    query = query + "JOIN prd_d_proyek e ON e.id = d.proyek "
    query = query + "WHERE e.id =  '"+id_proyek+"'"

    cursor.execute(query)
    records = cursor.fetchall()

    hitungDurasi = 0
    
    for data in records:
        hitungDurasi = hitungDurasi + data[7]
    
    hitungJam = hitungDurasi/60
    print("Durasi :", ceil(hitungJam), "Jam Per Produk")

    return hitungJam


def UpdateProcess(id):
    conn = database.connector()
    cursor = conn.cursor()
    query = "UPDATE prd_r_proses SET prosesSesudahnya = %s,nodalOutput = %s, nama = %s,durasi = %s,satuanDurasi = %s,jenisProses = %s WHERE id = '"+id+"'"
    try:
        data = request.json
        prosesSesudah = data["prosesSesudahnya"]
        nodalOutput = data["nodalOutput"]
        nama = data["nama"]
        durasi = data["durasi"]
        satuanDurasi = data["satuanDurasi"]
        jenisProses = data["jenisProses"]

        values = (prosesSesudah,nodalOutput,nama,durasi,satuanDurasi,jenisProses)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def ShowLastProcessofProduct():
    conn = database.connector()
    cursor = conn.cursor()

    idProduk = input("Input ID Produk : ")

    query = "SELECT c.id, c.nama, c.durasi, c.satuanDurasi, c.nodalOutput, "
    query = query + "d.stasiunkerja, "
    query = query + "e.id, e.namajenisproses "
    query = query + "FROM prd_r_jenisproduk a, prd_r_strukturjnsprd b, prd_r_proses c, "
    query = query + "gen_r_mampuproses d, prd_r_jenisproses e, prd_d_rincianproyek f, prd_d_produk g "
    query = query + "WHERE a.id = b.jnsProduk AND b.idNodal = c.nodalOutput "
    query = query + "AND c.id = d.proses AND c.jenisProses = e.id AND g.id = '"+idProduk+"'" 
    query = query + "AND f.id = g.rincianProyek ORDER BY c.nodalOutput ASC"

    cursor.execute(query)

    records = cursor.fetchall()

    print("=======================================================================================================================")
    col_names = ["ID Proses","Nama Proses","Durasi","Satuan Durasi","ID Nodal Output","Stasiun Kerja","ID Jenis Proses","Nama jenis proses"]
    df = pd.DataFrame(records, columns = col_names)
    print(df)
    print("=======================================================================================================================")

    id_nodal = df["ID Nodal Output"].iloc[0]

    df_filter = df[df["ID Nodal Output"] == id_nodal]
    print(df_filter)
    print("=======================================================================================================================")
    
    #jika data index ws setelah nya tidak sama,langsung print proses terakhir
    #df_new = pd.DataFrame(columns = col_names)
    #for i in df_filter.index:
    #    if df["Stasiun Kerja"].iloc[i] != df["Stasiun Kerja"].iloc[i+1]:
    #        #df_new.iloc[i] = df_filter.iloc[i]
    #        print(df_filter.iloc[i])
    #        print()
    #        break
    #    elif df_filter['Stasiun Kerja'].iloc[i] == df_filter['Stasiun Kerja'].iloc[i-1] and i == df_filter.index-1:
    #        print(df_filter.iloc[i])
    #        print()
    #        break
    #    elif df_filter['Stasiun Kerja'].iloc[i] == df_filter['Stasiun Kerja'].iloc[i+1]:
    #        print(df_filter.iloc[i])
    ##        print()
            #break
     #   elif df_filter['Stasiun Kerja'].iloc[i] != df_filter['Stasiun Kerja'].iloc[i+1] and df_filter['Stasiun Kerja'].iloc[i] == df_filter['Stasiun Kerja'].iloc[i-1] :
     #       print(df_filter.iloc[i])
      #      print()
     #       break




def ShowLastProcessofProductAPI(idProduk):
    conn = database.connector()
    cursor = conn.cursor()

    #a : jenis produk
    #b : struktur jenis produk
    #c : table proses
    #d : mampu proses
    #e : jenis proses
    #f : rincian proyek
    #g : produk
    #h : stasiunkerja

    #proses(c) gabung jenisproses(e)
    #proses(c) gabung mampuproses(d)
    #stasiunkerja(h) gabung mampuproses(d)
    #proses(c) gabung strukturjenis produk(b)
    #strukturjenisproduk(b) gabung jenis produk(a)
    ##jenis produk(a) gabung rincianproyek(f)
    #rincianproyek(f) gabung produk(g)
    #produk = PR_01

    query = "SELECT c.id, c.nama, c.durasi, c.satuanDurasi, c.nodalOutput, "
    query = query + "d.stasiunkerja, "
    query = query + "e.id AS 'idjenisproses', e.namajenisproses "
    query = query + "FROM prd_r_jenisproduk a, prd_r_strukturjnsprd b, prd_r_proses c, "
    query = query + "gen_r_mampuproses d, prd_r_jenisproses e, prd_d_rincianproyek f, prd_d_produk g, gen_r_stasiunkerja h "
    query = query + "WHERE a.id = b.jnsProduk AND b.idNodal = c.nodalOutput "
    query = query + "AND c.id = d.proses AND d.stasiunKerja = h.id AND c.jenisProses = e.id AND g.id = '"+idProduk+"'" 
    query = query + "AND f.id = g.rincianProyek AND c.nodalOutput = 'A0000' GROUP BY idjenisproses ORDER BY c.nodalOutput ASC"

    cursor.execute(query)

    records = cursor.fetchall()

    print("=======================================================================================================================")
    col_names = ["ID Proses","Nama Proses","Durasi","Satuan Durasi","ID Nodal Output","Stasiun Kerja","Jenis Proses","Nama jenis proses"]
    df = pd.DataFrame(records, columns = col_names)
    print(df)
    print("=======================================================================================================================")

    id_nodal = df["ID Nodal Output"].iloc[0]

    df_filter = df[df["ID Nodal Output"] == id_nodal]
    print(df_filter)
    print("=======================================================================================================================")
    
    #Versi Papan Tulis
    #jika data index ws setelah nya tidak sama,langsung print proses terakhir
    #data_zero = []
    #df_new = pd.DataFrame(data_zero,columns = col_names)
    #for i in df_filter.index:
    #    if df["Stasiun Kerja"].iloc[i] != df["Stasiun Kerja"].iloc[i+1]:
    #        df_new = df_new.append(df_filter.iloc[i])
    #        print(df_filter.iloc[i])
    #        print()
    #        break
    #    elif df_filter['Stasiun Kerja'].iloc[i] == df_filter['Stasiun Kerja'].iloc[i-1] and i == df_filter.index-1:
    #        df_new = df_new.append(df_filter.iloc[i])
    #        print(df_filter.iloc[i])
    #        print()
    #        break
    #    elif df_filter['Stasiun Kerja'].iloc[i] == df_filter['Stasiun Kerja'].iloc[i+1]:
    #        df_new = df_new.append(df_filter.iloc[i])
    #        print(df_filter.iloc[i])
    #        print()
    #    elif df_filter['Stasiun Kerja'].iloc[i] != df_filter['Stasiun Kerja'].iloc[i+1] and df_filter['Stasiun Kerja'].iloc[i] == df_filter['Stasiun Kerja'].iloc[i-1]:
    #        df_new.iloc = df_new.append(df_filter.iloc[i])
    #        print(df_filter.iloc[i])
    #        print()
    #        break

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    
    new_records = df_filter.values.tolist()
    print(new_records)

    for data in new_records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)
