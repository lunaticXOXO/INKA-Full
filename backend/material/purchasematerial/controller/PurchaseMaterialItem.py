import datetime
import db.db_handler as database
from flask import request,make_response,jsonify
import random
import string
import time

def GetMaterialItem():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * from mat_d_purchaseitem"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def PurchaseMaterialItem():
    conn = database.connector()
    cursor = conn.cursor()

    query = "INSERT INTO mat_d_purchaseitem(id_item,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,purchaseId)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    try:
       data = request.json 
       id_item = data["id_item"]
       supplierCode = data["supplierCode"]
       materialTypeCode = data["materialTypeCode"]
       quantity = data["quantity"]
       unit = data["unit"]
       schedulledArrival = data["schedulledArrival"]
       purchaseId = data["purchaseId"]
       values = (id_item,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,purchaseId)
       cursor.execute(query,values)
       conn.commit()
       cursor.close()
       conn.close()
       hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def PurchaseMaterialItemByIDPurchase(idPurchase):
    conn = database.connector()
    cursor = conn.cursor()

    query_select = "SELECT id FROM mat_d_purchasematerial WHERE id = '"+idPurchase+"'"
    cursor.execute(query_select)
    records = cursor.fetchall()
    for index in records:
        idPurchase = index[0]

    #GET Id Purchase yang di klik
    print("ID Purchase : ",idPurchase)

    #Angka awal dan angka akhir di set 00 & 0
    angka_awal = '00'
    angka_akhir = 0
    temp = ""
    id_item_new = ""    


    query_get_purchaseItem = "SELECT a.id_item FROM mat_d_purchaseitem a JOIN mat_d_purchasematerial b ON b.id = a.purchaseId WHERE b.id = '"+idPurchase+"'"
    cursor.execute(query_get_purchaseItem)
    records_matitem = cursor.fetchall()

    for index in records_matitem:
        temp = index[0]
    print("temp : ",temp)
    if temp == '':
        print("test2")
        id_item_new = idPurchase + "000"
    else:
        angka_akhir_str = ""
        for index in records_matitem:
            if angka_akhir >= 10:
                angka_awal = '0'
                angka_akhir = angka_akhir + 1
                angka_akhir_str = str(angka_akhir)
                id_item_new = idPurchase + angka_awal + angka_akhir_str
            else:
                angka_akhir = angka_akhir + 1
                angka_akhir_str = str(angka_akhir)
                id_item_new = idPurchase + angka_awal + angka_akhir_str

    print("ID Item : ",id_item_new)
    query_insert = "INSERT INTO mat_d_purchaseitem(id_item,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,purchaseId)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    try:
        data = request.json
        supplierCode = data["supplierCode"]
        materialTypeCode = data["materialTypeCode"]
        quantity = data["quantity"]
        unit = data["unit"]
        schedulledArrival = data["schedulledArrival"]
        values = (id_item_new,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,idPurchase)
        cursor.execute(query_insert,values)
        print("ID Item : ",id_item_new)
        conn.commit()
        #Query untuk menampilkan hasil multiplier dan quantity
        query_get_multiplie = "SELECT a.quantity,b.multiplier FROM mat_d_purchaseitem a JOIN gen_r_materialunit b ON b.id = a.unit WHERE a.id_item = '"+id_item_new+"'"
        cursor.execute(query_get_multiplie)
        records_unit = cursor.fetchall()
        mul_str = ""
        qty_str = ""
        for index in records_unit:
            qty_str = index[0]
            mul_str = index[1]
        
        print("qty_str : ",qty_str)
        qty_int = int(qty_str)
        mul_int = int(mul_str)
        
        
        #total kan qty int dengan multiplier
        total = qty_int * mul_int
        unit = "U01"
        query_update = "UPDATE mat_d_purchaseitem SET quantity = %s, unit = %s WHERE id_item = %s"
        values = (total,unit,id_item_new)
        cursor.execute(query_update,values)
        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def UpdatePemesanan(id):
    conn = database.connector()
    cursor = conn.cursor()  

    query_select_before = "SELECT jumlah, Harga, LeadTime, MinimalOrder,unit FROM cpl_haruspesan03 WHERE id = '"+id+"'"
    cursor.execute(query_select_before)
    records = cursor.fetchall()

    for index in records:
        harga_before    = index[1]
        leadtime_before = index[2]
        minimal_before  = index[3]
       
    kriteria = ""
    query_update1 = "UPDATE cpl_haruspesan03 SET jumlah = %s, Harga = %s,LeadTime = %s, MinimalOrder = %s, unit = %s WHERE id = '"+id+"'"
    try:
        data = request.json
        jumlah = data["jumlah"]
        harga = data["Harga"] #kriteria K02
        leadtime = data["LeadTime"] #Kriteria K03
        minimalorder = data["MinimalOrder"] #kriteria K05
        unit = data["unit"]
        values  = (jumlah,harga,leadtime,minimalorder,unit)
        cursor.execute(query_update1,values)
        conn.commit()

        query_select_after = "SELECT jumlah, Harga, LeadTime, MinimalOrder,unit,pemasok,code,RencanaKedatangan FROM cpl_haruspesan03 WHERE id = '"+id+"'"
        cursor.execute(query_select_after)
        records2 =  cursor.fetchall()
        for index2 in records2:
            harga_after = index2[1]
            leadtime_after = index2[2]
            minimal_after = index2[3]
            pemasok = index2[5]
            materialtype = index2[6]
            rencana_before = index2[7]

        query_update2 = "UPDATE mat_r_materialtypesupplier SET Nilai = %s WHERE materialTypeCode = %s AND supplierCode = %s AND IDKriteria = %s"
       
        cek = None
        for i in range(3):
            cek = False
            if harga_before != harga_after:
                kriteria = "K02"
                values2 = (harga_after,materialtype,pemasok,kriteria)
                cursor.execute(query_update2,values2)
                conn.commit()
            if minimal_before != minimal_after:
                kriteria = "K05"
                values2 = (minimal_after,materialtype,pemasok,kriteria)
                cursor.execute(query_update2,values2)
                conn.commit()

            if leadtime_before != leadtime_after:
                kriteria = "K03"
                values2 = (leadtime_after,materialtype,pemasok,kriteria)
                cursor.execute(query_update2,values2)
                conn.commit()
               
    
    except Exception as e:     
        print("error",str(e))
       

    cursor.close()
    conn.close()
  
   


def UpdatePemesananMerge(id):
    cek = UpdatePemesanan(id)
    time.sleep(8)
    conn = database.connector()
    cursor = conn.cursor()


    query_getharuspesan03 = "SELECT RencanaKedatangan FROM cpl_haruspesan03 WHERE id = '"+id+"'"
    cursor.execute(query_getharuspesan03)
    data = cursor.fetchone()
    rencana_before = data[0]

    query_getharuspesan02 = "SELECT RencanaKedatangan FROM cpl_haruspesan02 WHERE id = '"+id+"'"
    cursor.execute(query_getharuspesan02)
    data = cursor.fetchone()
    rencana_after = data[0]

   
    try:
        if  rencana_before != rencana_after:
            print("test")
            query_update3 = "UPDATE cpl_haruspesan03 SET RencanaKedatangan = %s WHERE id = %s"
            values3 = (rencana_after,id)
            cursor.execute(query_update3,values3)
            conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        hasil = {"status" : "gagal"}
        print("error",str(e))
    
    cursor.close()
    conn.close()
    return hasil



def GetMaterialItemByPurchaseMaterial(idPurchase):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id_item,a.supplierCode,a.materialTypeCode,a.quantity,c.nama AS 'namaUnit',a.schedulledArrival,a.purchaseId FROM mat_d_purchaseitem a "
    query += "JOIN mat_d_purchasematerial b ON b.id = a.purchaseId JOIN gen_r_materialunit c ON c.id = a.unit "
    query += "WHERE a.purchaseId = '"+idPurchase+"' AND a.quantity != 0 ORDER BY a.id_item DESC"

    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)




def GetPurchaseMaterialinPurchaseItem(idPurchase):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM  mat_d_purchasematerial WHERE id = '"+idPurchase+"'"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def GetPurchaseMaterialItemComparedMatStock(idPurchase):
    conn = database.connector()
    cursor = conn.cursor()
    query_show = "SELECT a.id_item,a.materialTypeCode,a.purchaseId,a.quantity,a.schedulledArrival,a.supplierCode,b.nama AS 'unit' FROM mat_d_purchaseitem a JOIN gen_r_materialunit b ON b.id = a.unit WHERE a.purchaseId = '"+idPurchase+"' AND a.quantity != 0 ORDER BY a.id_item DESC "
       
    cursor.execute(query_show)
    records_purch_item = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    for data in records_purch_item:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)



def OrderMaterialLoop(code):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM cpl_haruspesan02"
    cursor.execute(query)
    records = cursor.fetchall()

    try:
        query_insert = "INSERT INTO mat_d_purchaseitem(id_item,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,purchaseId)VALUES(%s,%s,%s,%s,%s,%s)"

        for index in records:
            query2 = "SELECT * FROM cpl_haruspesan02 WHERE code = '"+code+"'"
            cursor.execute(query2)
            data = cursor.fetchone()
            code = data[0]
            if index[0] == code:
                values = (data[0],data[1],data[2])
                cursor.execute(query_insert,values)
        
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        hasil = {"status" : "berhasil"}
        print("Error",str(e))
    return hasil



def AddTimeOrderMaterial():
    conn = database.connector()
    cursor = conn.cursor()

    query = "INSERT INTO cpl_haruspesan00(batas,waktu)VALUES(%s,%s)"
        
    try:
        data = request.json
        batas = data["fullDate"]
        waktu = None
        values = (batas,waktu)
        cursor.execute(query,values)

        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        hasil = {"status" : "gagal"}
        print("error",str(e))
    return hasil


def ShowMaterialHarusPesan():
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM cpl_haruspesan02 a ORDER BY a.pemasok,a.peringkat ASC"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def InsertMaterialHarusPesan():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO cpl_haruspesan03(id,code,nama,jumlah,pemasok,peringkat,RencanaKedatangan,LeadTime,Harga,MinimalOrder,purchaseid,unit)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        data = request.json
        id = data["id"]
        code = data["code"]
        nama = data["nama"]
        jumlah = data["jumlah"]
        pemasok = data["pemasok"]
        peringkat = data["peringkat"]
        rencanadatang = data["RencanaKedatangan"]
        leadtime    = data["LeadTime"]
        harga = data["Harga"]
        minimalorder = data["MinimalOrder"]
        purchaseid = data["purchaseid"]
        unit =  "U01"
        values = (id,code,nama,jumlah,pemasok,peringkat,rencanadatang,leadtime,harga,minimalorder,purchaseid,unit)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("error",str(e))
        hasil = {"status" : "gagal"}
    return hasil

def ShowHasilPemesanan(purchaseid):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM cpl_haruspesan03 WHERE purchaseid = '"+purchaseid+"' ORDER BY pemasok ASC"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)



def InsertHasilPesananToPurchaseItem(purchaseid):
    conn = database.connector()
    cursor = conn.cursor()
    try:
        query_insert = "INSERT INTO mat_d_purchaseitem(id_item,supplierCode,materialTypeCode,quantity,unit,schedulledArrival,purchaseId,LeadTime,Harga,MinimalOrder)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        query = "SELECT * FROM cpl_haruspesan03 WHERE purchaseid = '"+purchaseid+"' ORDER BY pemasok ASC"
        cursor.execute(query)
        records = cursor.fetchall()

        query_count = "SELECT COUNT(*) FROM mat_d_purchaseitem WHERE purchaseId LIKE '"+purchaseid+"%'"

        for index in records:
            cursor.execute(query_count)
            data = cursor.fetchone()
            count = int(data[0])
            id_item      = purchaseid + str(count).zfill(3)
        
            materialType = index[1]
            quantity     = index[3]
            supplierCode = index[4]
            scheduller   = index[6]
            LeadTime     = index[7]
            Harga        = index[8]
            MinOrder     = index[9]
            unit         = index[11]
            values = (id_item,supplierCode,materialType,quantity,unit,scheduller,purchaseid,LeadTime,Harga,MinOrder)
            cursor.execute(query_insert,values)
        
        query_delete = "DELETE FROM cpl_haruspesan03"
        cursor.execute(query_delete)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def DeletePesananMaterial(id):
    conn = database.connector()
    cursor = conn.cursor()
    query = "DELETE FROM cpl_haruspesan03 WHERE id = '"+id+"'"
    try:
        cursor.execute(query)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("error",str(e))
        hasil = {"status" : "gagal"}
    return hasil

