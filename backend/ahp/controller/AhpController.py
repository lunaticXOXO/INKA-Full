import numpy as np
import math
import db.db_handler as database
from flask import request,make_response,jsonify


## AHP untuk Kriteria
def hitungSetengahMatrik():
    con00 = database.connector()
    cur00 = con00.cursor()
    q00="select * from gen_r_matrikskriteria WHERE konfirm IS NULL"
    cur00.execute(q00)
    tabel00=cur00.fetchall()
    for row00 in tabel00:
        K1=row00[0]
        K2=row00[1]
        nil=row00[2]
        if(K1!=K2):
            q01="insert into gen_r_matrikskriteria (IDKriteria, IDKriteria02, \
            nilai) values('"+K2+"', '"+K1+"', '"+str(1/nil)+"')"
            cur00.execute(q01)
            con00.commit()
            hasil = True
        else:
            hasil = False

    return hasil


def totalkolom():
    con00 = database.connector()
    cur00 = con00.cursor()
    q00="Select distinct idKriteria02 from gen_r_matrikskriteria WHERE konfirm IS NULL order by \
    idkriteria02"
    cur00.execute(q00)
    tabel00=cur00.fetchall()
    total=[]
    for row00 in tabel00:
        idKri00=row00[0]
        q01 = "select * from gen_r_matrikskriteria where idKriteria02= \
        '"+idKri00+"' AND konfirm IS NULL"
        cur00.execute(q01)
        tabel01=cur00.fetchall()
        jml=0
        for row01 in tabel01:
            nil01=row01[2]
            jml =jml+nil01
        total.append(jml)  
    return total


def normalisasi():
    con00 = database.connector()
    cur00 = con00.cursor()
    total= totalkolom ()
    q00="Select distinct idKriteria02 from gen_r_matrikskriteria WHERE konfirm IS NULL order by \
    idkriteria02"
    cur00.execute(q00)
    tabel00=cur00.fetchall()
    angka = 0
    try:
        for row00 in tabel00:
            idkri00=row00[0]
            q01="select * from gen_r_matrikskriteria WHERE konfirm IS NULL"
            cur00.execute(q01)
            tabel01=cur00.fetchall()
            for row01 in tabel01:
                K01 = row01[0]
                K02 = row01[1]
                nil01 = row01[2]
                jml01 = total[angka]
                if (idkri00 == K02):
                    normalisasi = nil01/jml01
                    q02 = "UPDATE gen_r_matrikskriteria SET nilai02 = \
                    '"+str(normalisasi)+"' where idKriteria02 = '"+idkri00+"' AND \
                    idKriteria = '"+K01+"' AND konfirm IS NULL"
                    cur00.execute(q02)
                    con00.commit()
            angka = angka + 1 
        hasil = True   
    except Exception:
        hasil = False
    return hasil

def totalbaris():
    con00 = database.connector()
    cur00 = con00.cursor()
    q00 = "select distinct idKriteria from gen_r_matrikskriteria WHERE konfirm IS NULL order by \
    idkriteria02"
    cur00.execute(q00)
    tabel00=cur00.fetchall()
    total=[]
    for row00 in tabel00:
        idkri00 = row00[0]
        q01 = "Select * from gen_r_matrikskriteria where idKriteria = \
        '"+idkri00+"' AND konfirm IS NULL"
        cur00.execute(q01)
        tabel01=cur00.fetchall()
        jml01 = 0
        for row01 in tabel01:
            nil02 = row01[3]
            jml01 = jml01 + nil02
        total.append(jml01)
    return total



def bobotKriteria():
    con00 = database.connector()
    cur00 = con00.cursor()
    total = totalbaris()
    jml=len(total)
    list01 = []
    for i in range(jml):
        total01 = total[i]
        bobot= total01/jml
        list01.append(bobot)
    return list01
        

def buatmatriks():
    con00 = database.connector()
    cur00 = con00.cursor()
    q00 = "select distinct IDKriteria FROM gen_r_matrikskriteria WHERE konfirm IS NULL\
    order by IDKriteria "
    cur00.execute(q00)
    tabel00 = cur00.fetchall()
    m = []
    angka = 0
    for row00 in tabel00:
        idkri00 = row00[0]
        q01 = "select * from gen_r_matrikskriteria where IDKriteria = \
        '"+idkri00+"' and konfirm IS NULL order by IDKriteria02"
        cur00.execute(q01)
        tabel01 = cur00.fetchall()
        n = []
        for row01 in tabel01:
            nil01 = row01[2]
            n.append(nil01)
        m.append(n)
        angka = angka +1
    return m, angka


def cariEigen(m00, uk):
    w, v = np.linalg.eig(m00)
    RI=0
    n00=len(m00)
    if(n00==1):
        RI=0.0
    if(n00==2):
        RI=0.0
    if(n00==3):
        RI=0.5799
    if(n00==4):
        RI=0.8921
    if(n00==5):
        RI=1.1159
    if(n00==6):
        RI=1.2358
    if(n00==7):
        RI=1.3322
    if(n00==8):
        RI=1.3952
    if(n00==9):
        RI=1.4537
    if(n00==10):
        RI=1.4882
    eigen = max(w)
    CI = (eigen - n00)/(n00 - 1)
    CR = CI/RI
    return eigen, RI, CI, CR

## Jika nilai eigen <= 0.1 maka insert data idKriteria dan bobot ke gen_r_kriteria bobot
#hasil akhir kriteria
def insertkriteria():
    con00 = database.connector()
    cur00 = con00.cursor()
    matriks=buatmatriks()
    print("test buat matriks")
    m00=matriks[0]
    uk=matriks[1]
    eigen=cariEigen(m00, uk)
    print("test test test")
    CR=eigen[3]
    angka01 = 0
    try:
        if (CR <= 0.1):
            print("Memenuhi Kriteria")
            bobot=bobotKriteria()
            q00="select distinct IDKriteria from gen_r_matrikskriteria WHERE konfirm IS NULL \
            order by IDKriteria"
            cur00.execute(q00)
            tabel00=cur00.fetchall()
            angka = 0
            q01="UPDATE gen_r_kriteriabobot SET selesai = current_timestamp"
            cur00.execute(q01)
            con00.commit()
            for row00 in tabel00:
                IDKri=row00[0]
                bobot01=bobot[angka]
                angka = angka+1
                angka01 = angka01+1
                q02="insert into gen_r_kriteriabobot (IDKriteria, Bobot,\
                mulai) values('"+IDKri+"', '"+str(bobot01)+"', current_timestamp)"
                cur00.execute(q02)
                con00.commit()
            angka01 = 0
            q03="select IDKriteria, Bobot from gen_r_kriteriabobot \
            WHERE selesai IS NULL order by Bobot DESC"
            cur00.execute(q03)
            tabel02=cur00.fetchall()
            for row01 in tabel02:
                bobot02=row01[1]
                IDKri00=row01[0]
                angka01 = angka01 +1
                q04="update gen_r_kriteriabobot set rangking =%s\
                where selesai is null and IDKriteria=%s"
                values = (angka01,IDKri00)
                cur00.execute(q04,values)
                con00.commit()
            hasil = {"status" : "berhasil"}
        else:
            hasil = {"status" : "perbaiki matriks"}
            print("Perbaiki Matriks")
            
    except Exception as e:
        hasil = {"status" : "gagal"}
        print("error",str(e))
    return hasil
    

def MergeCalculateKriteria(idPenghitung):
    con00 = database.connector()
    cur00 = con00.cursor()
    try:
        hitungSetengahMatrik()
        totalkolom() 
        normalisasi()
        totalbaris()
        bobotKriteria()
        hasil = buatmatriks()
        m=hasil[0]
        uk=hasil[1]
        hasil=cariEigen(m, uk)
        hasil2 = insertkriteria()
        if hasil2 == {"status" : "berhasil"}:
            query = "UPDATE gen_r_matrikskriteria SET konfirm = 1 WHERE idPenghitung = '"+idPenghitung+"'"
            cur00.execute(query)
            con00.commit()
            query2 = "UPDATE gen_r_matrikskriteria SET konfirm = 1, idPenghitung = '"+idPenghitung+"' WHERE konfirm IS NULL and idPenghitung IS NULL"
            query3 = "UPDATE gen_r_kriteriabobot SET idPenghitung = '"+idPenghitung+"' WHERE idPenghitung IS NULL"
            cur00.execute(query2)
            cur00.execute(query3)
            con00.commit()
            output = {"status" : "berhasill"}
        elif hasil2 == {"status" : "perbaiki matriks"}:
           output = {"status" : "perbaiki matriks"}
           query4= "DELETE FROM gen_r_matrikskriteria WHERE idPenghitung IS NULL AND konfirm IS NULL"
           cur00.execute(query4)
           con00.commit()
    except Exception as e:
        output = {"status" : "gagal"}
        print("error",str(e))
    return output



def HasilKriteriaByAdmin(idPenghitung):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM gen_r_matrikskriteria WHERE idPenghitung = '"+idPenghitung+"'"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def HasilKriteriaBobotByAdmin(idPenghitung):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM gen_r_kriteriabobot WHERE idPenghitung = '"+idPenghitung+"'"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


## AHP untuk supplier
#1
def hitungSetengahMatrik01():
    #Untuk menghitung nilai setengah matriks supplier setiap kriteria
    con00 = database.connector()
    cur00 = con00.cursor()
    q00="select distinct idKriteria from gen_r_perbandingan \
    where konfirm is null"
    cur00.execute(q00)
    tabel00=cur00.fetchall()
    for row00 in tabel00:
        idkri00=row00[0]
        q01="select * from gen_r_perbandingan where IDKriteria = \
        '"+idkri00+"' and konfirm is null "
        cur00.execute(q01)
        tabel01=cur00.fetchall()
        for row01 in tabel01:
            K1 = idkri00
            K2 = row01[1]
            K3 = row01[2]
            nil01 = row01[3]
            if(K2!=K3):
                q02 = "insert into gen_r_perbandingan (IDKriteria, IDSupplier01, \
                IDSupplier02, nilai) values('"+K1+"','"+K3+"', '"+K2+"', \
                '"+str(1/nil01)+"')"
                cur00.execute(q02)
                con00.commit()

#2
def totalkolom01():
    con00 = database.connector()
    cur00 = con00.cursor()
    q00="Select distinct IDKriteria from gen_r_perbandingan where konfirm is null \
    order by IDKriteria"
    cur00.execute(q00)
    tabel00=cur00.fetchall()
    total01=[]
    angka=0
    for row00 in tabel00:
        idKri00=row00[0]
        q01 = "select distinct IDSupplier02 from gen_r_perbandingan where IDKriteria = \
        '"+idKri00+"' and konfirm is null order by IDSupplier02"
        cur00.execute(q01)
        tabel01=cur00.fetchall()
        total=[]
        for row01 in tabel01:
            IDSup02 = row01[0]
            q02 = "select * from gen_r_perbandingan where IDSupplier02 ='"+IDSup02+"' \
            AND IDKriteria = '"+idKri00+"' and konfirm is null \
            order by IDKriteria, IDSupplier02"
            cur00.execute(q02)
            tabel02=cur00.fetchall()
            jml01 = 0
            for row02 in tabel02:
                K01=row02[0]
                K02=row02[1]
                K03=row02[2]
                nil02=row02[3] 
                jml01 = jml01+nil02
            total.append(jml01)
        total01.append(total)
    return total01
#3
def normalisasi01():
    con00 = database.connector()
    cur00 = con00.cursor()
    total01 = totalkolom01()
    q00="Select distinct IDKriteria from gen_r_perbandingan where konfirm is null \
    order by IDKriteria"
    cur00.execute(q00)
    tabel00=cur00.fetchall()
    angka01 = 0   
    for row00 in tabel00:
        idkri00 = row00[0]
        q01 = "select distinct IDSupplier02 from gen_r_perbandingan WHERE IDKriteria = \
        '"+idkri00+"' and konfirm is null order by IDSupplier02"
        cur00.execute(q01)
        tabel01=cur00.fetchall()
        angka02 = 0
        for row01 in tabel01:
            idSup02 = row01[0]
            q02 = "select * from gen_r_perbandingan WHERE IDKriteria = '"+idkri00+"' \
            AND IDSupplier02 = '"+idSup02+"' and konfirm is null \
            order by IDKriteria, IDSupplier02"
            cur00.execute(q02)
            tabel02=cur00.fetchall()
            for row02 in tabel02:
                K01 = row02[0]
                K02 = row02[1]
                K03 = row02[2]
                nil01 = row02[3]    
                jml01 = total01[angka01][angka02]
                if (idSup02 == K03):
                    normalisasi01 = nil01/jml01
                    q02 = "UPDATE gen_r_perbandingan SET nilai02 = \
                    '"+str(normalisasi01)+"' where idKriteria = '"+idkri00+"' AND \
                    IDSupplier01 = '"+K02+"' AND IDSupplier02 = '"+K03+"' "
                    cur00.execute(q02)
                    con00.commit()
            angka02 = angka02 + 1
        angka01 = angka01 +1


def totalbaris01():
    con00 = database.connector()
    cur00 = con00.cursor()
    q00 = "select distinct IDKriteria from gen_r_perbandingan where konfirm is null\
    order by IDKriteria "
    cur00.execute(q00)
    tabel00=cur00.fetchall()
    total01=[]
    angka=0
    for row00 in tabel00:
        idKri00=row00[0]
        q01 = "select distinct IDSupplier01 from gen_r_perbandingan where IDKriteria = \
        '"+idKri00+"' and konfirm is null order by IDSupplier01"
        cur00.execute(q01)
        tabel01=cur00.fetchall()
        total = []
        for row01 in tabel01:
            IDSup01 = row01[0]
            q02 = "select * from gen_r_perbandingan where IDSupplier01 ='"+IDSup01+"' \
            AND IDKriteria = '"+idKri00+"' and konfirm is null order by IDKriteria, IDSupplier01"
            cur00.execute(q02)
            tabel02=cur00.fetchall()
            jml02 = 0
            for row02 in tabel02:
                K01=row02[0]
                K02=row02[1]
                K03=row02[2]
                nil02=row02[4]
                jml02 = jml02 + nil02
            total.append(jml02)
        total01.append(total)
    return total01


def bobot01Supplier():
    total01 = totalbaris01()
    jml = len(total01)
    list01=[]
    for i in range(jml):
        L = total01[i]
        isiL = len(L)
        list02=[]
        for j in range(isiL):
            nilai = L[j]/isiL
            list02.append(nilai)
        list01.append(list02)
    return list01
        


def buatmatriks01():
    con00 = database.connector()
    cur00 = con00.cursor()
    q00= "select distinct IDKriteria from gen_r_perbandingan where konfirm is null \
    order by IDKriteria"
    cur00.execute(q00)
    tabel00=cur00.fetchall()
    k=[]
    for row00 in tabel00:
        IDKri00=row00[0]
        q01 = "select distinct IDSupplier01 from gen_r_perbandingan where \
        IDKriteria = '"+IDKri00+"' and konfirm is null order by IDKriteria, IDSupplier01"
        cur00.execute(q01)
        tabel01=cur00.fetchall()
        angka = 0
        m = []
        for row01 in tabel01:
            IDSup01 = row01[0]
            q02 = "select * from gen_r_perbandingan where IDKriteria = \
            '"+IDKri00+"' AND IDsupplier01 = '"+IDSup01+"' and konfirm is null\
            order by IDKriteria, IDSupplier02"
            cur00.execute(q02)
            tabel02=cur00.fetchall()
            n = []
            for row02 in tabel02:
                nil01 = row02[3]
                n.append(nil01)
            m.append(n)
        k.append(m)
        angka = angka + 1
    return k
  
def insertSupplier():
    con00 = database.connector()
    cur00 = con00.cursor()
    matriks= buatmatriks01()
    bobot= bobot01Supplier()
    jml=len(matriks)
    q00="select distinct IDKriteria from gen_r_perbandingan where konfirm is null \
    order by IDKriteria"
    cur00.execute(q00)
    tabel00=cur00.fetchall()
    angka=0
    q03="UPDATE gen_r_supplierbobot SET selesai = current_timestamp"
    cur00.execute(q03)
    con00.commit()
    for i in range(jml):
        list01=matriks[i]
        list02=bobot[i]
        uk=len(list01)
        eigen=cariEigen(list01, uk)
        CR=eigen[3]
        idKri00=tabel00[angka][0]
        angka=angka+1
        q01= "select distinct IDSupplier01 from gen_r_perbandingan where konfirm is null \
        order by IDSupplier01"
        cur00.execute(q01)
        tabel01=cur00.fetchall()
        if(CR<=0.1):
            print("Memenuhi Kriteria")
            for j in range(uk):
                idSup01=tabel01[j][0]
                bobot01=list02[j]
                q02 = "insert into gen_r_supplierbobot (IDKriteria, IDSupplier, Bobot, \
                mulai) values('"+idKri00+"','"+idSup01+"', '"+str(bobot01)+"', current_timestamp)"
                cur00.execute(q02)
                con00.commit()
            return True
        else:
            print("Perbaiki Matriks")
            return False
        
def bobotglobal():
     con00 = database.connector()
     cur00 = con00.cursor()
     jumlah = 0
     q00="select * from gen_r_kriteriabobot where selesai is null"
     cur00.execute(q00)
     tabel00=cur00.fetchall()
     for row00 in tabel00:
         IDkri00=row00[0]
         bobot01=row00[1]
         q01="select * from gen_r_supplierbobot where IDKriteria =\
         '"+IDkri00+"' AND selesai is null ORDER BY IDSupplier,IDKriteria"
         cur00.execute(q01)
         tabel01=cur00.fetchall()
         for row01 in tabel01:
             IDSup00=row01[1]
             bobot02=row01[2]
             bobot03 = bobot01 * bobot02
             q02="UPDATE gen_r_supplierbobot SET BobotGlobal = \
             '"+str(bobot03)+"' where IDKriteria = '"+IDkri00+"' AND \
             IDSupplier = '"+IDSup00+"' AND selesai is null "
             cur00.execute(q02)
             con00.commit()


def supplierrangking():
    con00 = database.connector()
    cur00 = con00.cursor()
    q00= "select IDSupplier, SUM(BobotGlobal) Bobot From gen_r_supplierbobot \
    where selesai is null GROUP BY IDSupplier order by Bobot DESC"
    cur00.execute(q00)
    tabel00=cur00.fetchall()
    angka = 1
    q03="UPDATE gen_r_supplierrangking SET selesai = current_timestamp"
    cur00.execute(q03)
    con00.commit()    
    for row00 in tabel00:
        IDSup00 = row00[0]
        Bobot = row00[1]
        q02 = "insert into gen_r_supplierrangking (IDSupplier, Bobot, \
        Rangking, mulai) values('"+IDSup00+"','"+str(Bobot)+"', \
        '"+str(angka)+"',current_timestamp)"
        angka = angka + 1
        cur00.execute(q02)
        con00.commit()


def MergeCountBobotSupplier(idPenghitung):
    conn = database.connector()
    cursor = conn.cursor()
    try:
        hitungSetengahMatrik01()
        totalkolom01()
        normalisasi01()
        totalbaris01()
        bobot01Supplier()
        hasil = buatmatriks01()   
        m=hasil[0]
        uk=hasil[1]
        hasil2=cariEigen(m, uk)
        hasil_insert = insertSupplier()
        bobotglobal()
        supplierrangking()
        if hasil_insert == {"status" : "berhasil"}:
            #query1 = "UPDATE gen_r_supplierbobot SET idPenghitung = '"+idPenghitung+"' WHERE idPenghitung IS NULL"
            #cursor.execute(query1)
            
            #query2 = "UPDATE gen_r_supplierrangking SET idPenghitung = '"+idPenghitung+"' WHERE idPenghitung IS NULL"
            #cursor.execute(query2)

            #query3 = "UPDATE gen_r_perbandingan SET konfirm = %s, idPenghitung = %s WHERE konfirm IS NULL"
            #konfirm = 1
            #values = (konfirm,idPenghitung)
            #cursor.execute(query3,values)
            #conn.commit()
            hasil_response = {"status" : "berhasil"}
        else: 
            hasil_response = {"status" : "perbaiki matriks"}
    except Exception as e:
        print("error",str(e))
        hasil_response = {"status" : "gagal"}
    return hasil_response


def MergeCountSupplier(idPenghitung):
    conn = database.connector()
    cursor = conn.cursor()
    try:
        hitungSetengahMatrik01()
        totalkolom01 ()
        normalisasi01()
        totalbaris01()
        bobot01Supplier()
        hasil = buatmatriks01()
        m=hasil[0]
        uk=hasil[1]
        hasil=cariEigen(m, uk)
        print('------------')
        print('Eigen: ', hasil[0])
        print('RI: ', hasil[1])
        print('CI: ', hasil[2])
        print('CR: ', hasil[3]) 
        final = insertSupplier()
        bobotglobal()
        supplierrangking()
        query1 = "UPDATE gen_r_supplierbobot SET idPenghitung = '"+idPenghitung+"' WHERE idPenghitung IS NULL"
        cursor.execute(query1)
        
        query2 = "UPDATE gen_r_supplierrangking SET idPenghitung = '"+idPenghitung+"' WHERE idPenghitung IS NULL"
        cursor.execute(query2)

        query3 = "UPDATE gen_r_perbandingan SET konfirm = %s, idPenghitung = %s WHERE konfirm IS NULL"
        konfirm = 1
        values = (konfirm,idPenghitung)
        cursor.execute(query3,values)
        conn.commit()
        if final == True:
            return {"status" : "berhasil"}

        else:
            return {"status" : "perbaiki matriks"}
    except Exception:
        return {"status" : "gagal"}



def HasilPerbandinganSupplierByAdmin(idPenghitung):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.IDKriteria,a.IDSupplier01,a.IDSupplier02,a.Nilai,a.Nilai02,a.idPenghitung FROM gen_r_perbandingan a WHERE a.konfirm = 1 AND a.idPenghitung = '"+idPenghitung+"'"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def HasilBobotSupplierByAdmin(idPenghitung):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT c.IDKriteria,c.IDSupplier,c.Bobot,c.BobotGlobal,c.idPenghitung FROM gen_r_supplierbobot c WHERE c.idPenghitung = '"+idPenghitung+"'"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def HasilRankingSupplierByAdmin(idPenghitung):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT d.IDSupplier,d.Bobot,d.Rangking,d.idPenghitung FROM gen_r_supplierrangking d WHERE d.idPenghitung = '"+idPenghitung+"'"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)






### tambahin semuanya "where selesai is null"
### setelah melakukan pembobotan, gen_r_matriks kriteria sebaiknya di hapus
### atau mencari yang konfirm is null

##bobot01Supplier(cursor, connect)
#####Untuk kriteria
##hitungSetengahMatrik(cursor,connect)
##totalkolom(cursor,connect)
##normalisasi(cursor,connect)
##totalbaris(cursor,connect)
##bobotKriteria(cursor,connect)
##insertkriteria(cursor,connect)
##hasil = buatmatriks(cursor, connect)
##m = hasil[0]
##uk = hasil[1]
##print(m)
##hasil=cariEigen(m, uk)
##print('------------')
##print('Eigen: ', hasil[0])
##print('RI: ', hasil[1])
##print('CI: ', hasil[2])
##print('CR: ', hasil[3])
##print('------------')


###### AHP untuk supplier
##hitungSetengahMatrik01(cursor, connect)
##totalkolom01(cursor, connect)
##normalisasi01(cursor, connect)
##totalbaris01(cursor, connect)
##bobot01Supplier(cursor, connect)
##print(bobot)
##hasil=buatmatriks01(cursor, connect)
##hasil = bobotKriteria(cursor, connect)
##print(hasil)
##insertSupplier(cursor, connect)
             
##bobotglobal(cursor, connect)

#supplierrangking(cursor, connect)


# hitungSetengahMatrik()
# totalkolom() 
# normalisasi()
# totalbaris()
# bobotKriteria()
# hasil = buatmatriks()
# m=hasil[0]
# uk=hasil[1]
# hasil=cariEigen(m, uk)
# hasil2 = insertkriteria()
# if hasil2 == True:
#     output = {"status" : "berhasill"}
# elif hasil2 == False:
#     output = {"status" : "gagal"}
# print(output)
