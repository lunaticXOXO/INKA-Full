from math import ceil
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
    query = "SELECT a.id, a.nama, a.durasi, a.satuanDurasi,a.jenisProses,a.prosesSesudahnya, c.idNodal FROM prd_r_proses a JOIN prd_r_strukturjnsprd c ON c.idNodal = a.nodalOutput"
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
    #conn.commit()

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

    query = "SELECT "
    query = query + "a.id, a.nama,"
    query = query + "b.idNodal, b.nama, b.jumlah,"
    query = query + "c.id, c.nama, c.durasi, c.satuandurasi,"
    query = query + "d.id, d.jumlah,"
    query = query + "e.id, e.nama, e.tglDibuat,"
    query = query + "f.id AS 'ID Produk'"
    query = query + "FROM prd_r_jenisproduk a"
    query = query + "JOIN prd_r_strukturjnsprd b ON b.jnsProduk = a.id "
    query = query + "JOIN prd_r_proses c ON c.nodalOutput = b.idNodal "
    query = query + "JOIN prd_r_rincianproyek d ON d.jenisProduk = a.id "
    query = query + "JOIN prd_r_proyek e ON e.id = d.proyek"
    query = query + "JOIN prd_d_produk f ON f.rincianProyek = d.id"
    query = query + "WHERE f.id =  '"+id_produk+"'"

    cursor.execute(query)
    records = cursor.fetchall()

    hitungDurasi = 0
    
    for data in records:
        hitungDurasi = hitungDurasi + data[7]
    
    hitungJam = hitungDurasi/60
    print("Durasi :", ceil(hitungJam), "Jam Per Produk")

    return hitungJam


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
    query = query + "JOIN prd_r_rincianproyek d ON d.jenisProduk = a.id "
    query = query + "JOIN prd_r_proyek e ON e.id = d.proyek "
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
    query = query + "gen_r_mampuproses d, prd_r_jenisproses e, prd_r_rincianproyek f, prd_d_produk g "
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
    query = query + "gen_r_mampuproses d, prd_r_jenisproses e, prd_r_rincianproyek f, prd_d_produk g, gen_r_stasiunkerja h "
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
