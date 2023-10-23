import db.db_handler as database
import datetime
from datetime import date
from flask import request,make_response,jsonify

def GetMaterialStock():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM mat_d_materialstock"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def AddNewMaterialStock():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO mat_d_materialstock(id,purchaseItem,merk,quantity,unit,arrivalDate)VALUES(%s,%s,%s,%s,%s,%s)"
    try:
        data = request.json
        id = data["id"]
        orders = data["orders"]
        merk = data["merk"]
        quantity = data["quantity"]
        unit = data["unit"]
        arrivalDate = data["arrivalDate"]
        values = (id,orders,merk,quantity,unit,arrivalDate)
        cursor.execute(query,values)
        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def GetMaterialStockbyOrder(order):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id,a.purchaseItem,a.merk,a.quantity,c.nama AS 'namaUnit',a.arrivalDate FROM mat_d_materialstock a JOIN mat_d_purchaseitem b ON b.id_item = a.purchaseItem JOIN gen_r_materialunit c ON c.id = a.unit WHERE a.purchaseItem = '"+order+"'"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)
    
def AddMaterialStockbyOrders(orders):
    conn = database.connector()
    cursor = conn.cursor()
    #Query untuk select id_item berdasarkan paramter input
    query = "SELECT id_item FROM mat_d_purchaseitem WHERE id_item = '"+orders+"'"
    cursor.execute(query)
    records = cursor.fetchall()

    
    quantity = ""
    unit = ""

    for index in records:
        orders = index[0]
    print("ID Item : ",orders)

    query_select_mattype = "SELECT a.quantity,a.unit FROM mat_d_purchaseitem a WHERE a.id_item = '"+orders+"'"
    cursor.execute(query_select_mattype)
    records2 = cursor.fetchall()

    for index in records2:
       
        quantity = index[0]
        unit = index[1]
    
    angka_awal = "00"
    angka_akhir = 0
    temp = ""
    today = date.today()

    year = today.year
    month = today.month
    day = today.day
    print(type(month))
    
    today_str = ""
    if month < 10:
        today_str = str(year) + '0' + str(month) + str(day)

    if month >= 10 and day < 10:
        today_str = str(year) + '0' + str(month) + '0' + str(day)

    if month >= 10 and day >= 10:
        today_str = str(year) +  str(month) +  str(day)   

    print("today date : ",today_str)

    query_insert =  "INSERT INTO mat_d_materialstock(id,purchaseItem,merk,quantity,unit,arrivalDate)VALUES(%s,%s,%s,%s,%s,%s)"
    query_insert2 = "INSERT INTO mat_d_materialonws01(workstationCode,materialStock,login)VALUES(%s,%s,%s)"
    query_insert3 = "INSERT INTO mat_d_statusbarcode(id,workstation)VALUES(%s,%s)"
    
    try:
        data = request.json
        #id = data["id"]
        merk = data["merk"]
        quantity = data["quantity"]

        quantity_int = int(quantity)
        unit = data["unit"]
        arrivalDate = data["arrivalDate"]
        workstationCode = "WSGD"
        login = datetime.datetime.now()
        #print("angka unit : ",unit)

        #Query untuk mendapatkan multiplier dari unit yang dipilih
        query_getunit = "SELECT a.multiplier,a.id FROM gen_r_materialunit a WHERE a.id = '"+unit+"'"
        cursor.execute(query_getunit)
        records_unit = cursor.fetchall()
        angka_multiplier_str = ""
        for index in records_unit:
            angka_multiplier_str = index[0]
            unit = index[1]

        #print("Angka STR : ",angka_multiplier_str)
        multiplier = int(angka_multiplier_str)
        #print("multiplier : ",multiplier)
        #Untuk mengecek apakah records kosong atau tidak
       
        x = 0
        #quantity yang diinput akan dilooping 
        for x in range(quantity_int):
            query_get_matstock = "SELECT COUNT(*) FROM mat_d_materialstock WHERE id LIKE '"+today_str+"%'"
            cursor.execute(query_get_matstock)
            records_stock = cursor.fetchall()
            for index2 in records_stock:
                temp = index2[0]
                jumlah = int(temp)
                
            #print("jumlah data : ",jumlah)
            quantity_unit = ""
            if jumlah == 0:
                id_stock = today_str + "000"
                values = (id_stock,orders,merk,quantity_unit,unit,arrivalDate)
                values2 = (workstationCode,id_stock,login)
                values3 = (id_stock,workstationCode)
                cursor.execute(query_insert,values)
                cursor.execute(query_insert2,values2)
                cursor.execute(query_insert3,values3)
                conn.commit()
            else:
                #print("jumlah data : ", jumlah)
                if jumlah >= 10 and jumlah <= 99:
                    angka_awal = '0'
                    #angka_akhir = angka_akhir + 1
                    angka_akhir = jumlah
                    angka_akhir_str = str(angka_akhir)
                    id_stock = today_str  +  angka_awal + angka_akhir_str
                    values = (id_stock,orders,merk,quantity_unit,unit,arrivalDate)
                    values2 = (workstationCode,id_stock,login)
                    values3 = (id_stock,workstationCode)
                    cursor.execute(query_insert,values)
                    cursor.execute(query_insert2,values2)
                    cursor.execute(query_insert3,values3)
                    conn.commit()

                elif jumlah >= 100:
                    #angka_akhir = angka_akhir + 1
                    angka_akhir = jumlah
                    angka_akhir_str = str(angka_akhir)
                    id_stock = today_str  +  angka_akhir_str
                    values = (id_stock,orders,merk,quantity_unit,unit,arrivalDate)
                    values2 = (workstationCode,id_stock,login)
                    values3 = (id_stock,workstationCode)
                    cursor.execute(query_insert,values)
                    cursor.execute(query_insert2,values2)
                    cursor.execute(query_insert3,values3)
                    conn.commit()
                else:
                    #angka_akhir = angka_akhir + 1
                    #print("jumlah data : ",jumlah)
                    angka_akhir =  jumlah 
                    angka_akhir_str = str(angka_akhir)
                    id_stock = today_str + angka_awal + angka_akhir_str
                    values = (id_stock,orders,merk,quantity_unit,unit,arrivalDate)
                    values2 = (workstationCode,id_stock,login)
                    values3 = (id_stock,workstationCode)
                    cursor.execute(query_insert,values)
                    cursor.execute(query_insert2,values2)
                    cursor.execute(query_insert3,values3)
                    conn.commit()
            
            #Query untuk mendapatkan multiplier , multiplier sebagai output quantity nya
            query_get_unit_by_stock = "SELECT b.multiplier FROM mat_d_materialstock a JOIN gen_r_materialunit b ON b.id = a.unit WHERE a.id = '"+id_stock+"'"
            cursor.execute(query_get_unit_by_stock)
            records_unit_by_stock = cursor.fetchall()
            for index in records_unit_by_stock:
                quantity_unit = index[0]
            

            unit_stock = "U01"
            query_update_unit_stock = "UPDATE mat_d_materialstock SET unit = %s, quantity = %s WHERE id = %s"
            values_update_unit_stock = (unit_stock,quantity_unit,id_stock)
            cursor.execute(query_update_unit_stock,values_update_unit_stock)
            conn.commit()
            # print("ID Stock : ",id_stock)
            # print("index : ", x)
            # print("multiplier : ",multiplier)
            print("Quantity : ",quantity_unit)
    
        
        #Query untuk select quantity material stock yang baru saja di insert!
        query_getquantitystock = "SELECT a.quantity FROM mat_d_materialstock a JOIN mat_d_purchaseitem b ON b.id_item = a.purchaseItem WHERE b.id_item = '"+orders+"'"
        cursor.execute(query_getquantitystock)
        records_qtystock = cursor.fetchall()
    
        counter_multiplier = 0
        for index in records_qtystock:
            jumlah_str = index[0]
            jumlah_int = int(jumlah_str)
            counter_multiplier = counter_multiplier + jumlah_int
            

        jumlah_stock = counter_multiplier
        print("jumlah_stock_akhir : ",jumlah_stock)

        #Query untuk GET quantity purchase item dari stock yang telah di tambahkan
        query_getpurchItem = "SELECT a.quantity FROM mat_d_purchaseitem a WHERE a.id_item = '"+orders+"'"
        cursor.execute(query_getpurchItem)
        records_qtyitem = cursor.fetchall()

        for index in records_qtyitem:
            jumlah_str2 = index[0]
            
        
        jumlah_int2 =   int(jumlah_str2)
        jumlah_purchase = jumlah_int2 
        
        print("jumlah purchase item : ", jumlah_purchase)
       
        #print("jumlah_purchase_akhir : ",jumlah_purchase)
        
        #pengurangan jumlah purchase dari jumlah stock yang sudah dimiliki.
        jumlah_now = jumlah_purchase - jumlah_stock
        if jumlah_now < 0:
            jumlah_now = 0
           
        #Query untuk mengupdate jumlah dan unit yang baru berdasarkan jumlah nya.
        query_update_jumlah = "UPDATE mat_d_purchaseitem SET quantity = %s WHERE id_item = %s"
        values4 = (jumlah_now,orders)
        cursor.execute(query_update_jumlah,values4)

        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        hasil = {"status" : "gagal"}
        print("Error",str(e))
    return hasil



def GetPurchaseItemInMatStock(orders):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id_item,c.nama AS 'namaSupplier', d.nama AS 'namaMatType' ,a.quantity,a.unit,e.id,e.nama,e.purchaserName FROM mat_d_purchaseitem a JOIN gen_r_supplier c ON c.code = a.supplierCode JOIN mat_r_materialtype d ON d.code = a.materialTypeCode JOIN mat_d_purchasematerial e ON e.id = a.purchaseId WHERE a.id_item = '"+orders+"'"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)




def GetMaterialBerhasilLogin(id):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT keterangan FROM cpl_matlogin WHERE idMat = '"+id+"'"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)


def InsertBatasMaterialRequirement():
    conn = database.connector()
    cursor = conn.cursor()
    query_insert_time = "INSERT INTO cpl_haruspesan00 (batas,waktu) VALUES (%s,%s)"
    try:
        data = request.json
        batas = data["fullDate"]
        waktu = None
        values = (batas,waktu)
        cursor.execute(query_insert_time,values)
        conn.commit()
        hasil = {"status" : "berhasil"} 
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def ShowBatasMaterialRequirement():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM cpl_haruspesan01 ORDER BY jumlah DESC"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    cursor.close()
    conn.close()
    return make_response(jsonify(json_data),200)
