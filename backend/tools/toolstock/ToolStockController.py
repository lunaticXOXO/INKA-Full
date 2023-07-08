from datetime import date
import db.db_handler as database
from flask import request,make_response,jsonify




def AddToolStockByToolPurchaseItem(toolPurchaseItem):   
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO eqp_d_toolstock(id,toolPurchaseItem,toolTypeCode,merk,quantity,unit,arrivalDate)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    try:

        data = request.json
        merk = data["merk"]
        quantity = data["quantity"]
        unit = data["unit"]
        arrivalDate = data["arrivalDate"]

        query_purchaseitem = "SELECT purchaseItemId,toolTypeId,quantity FROM eqp_d_toolpurchaseitem WHERE purchaseItemId = '"+toolPurchaseItem+"'"
        cursor.execute(query_purchaseitem)
        records_purchaseitem = cursor.fetchall()

        for index in records_purchaseitem:
            toolPurchaseItem = index[0]
            toolType = index[1]
            quantity_purchaseitem = index[2]
            quantity_purchaseitem = int(quantity_purchaseitem)

    
        query_getquantityunit = "SELECT multiplier FROM gen_r_materialunit WHERE id = '"+unit+"'"
        cursor.execute(query_getquantityunit)
        records_quantityunit = cursor.fetchall()

        for index in records_quantityunit:
            new_qty = index[0]
            
        query_counttooltype = "SELECT COUNT(*) FROM eqp_d_toolstock WHERE toolTypeCode LIKE '"+toolType+"'"
        cursor.execute(query_counttooltype)
        records_count = cursor.fetchall()

        for index in records_count:
            count_data = index[0]

        count_data = int(count_data)
        quantity_int = int(quantity)
        print("Qty Int : ",quantity_int)
        print("count data : ",count_data)
        
        i = 0
        tool_stock = 0   
        for i in range(quantity_int):
            
            if count_data == 0:
                id = toolType + "0000"
                values = (id,toolPurchaseItem,toolType,merk,new_qty,unit,arrivalDate)
                cursor.execute(query,values)
            else:
             
                if quantity_int >= 10:
                    count_data = count_data + 1
                    id = toolType + "00" + str(count_data)
                    values = (id,toolPurchaseItem,toolType,merk,new_qty,unit,arrivalDate)
                    cursor.execute(query,values)
                else:
                    count_data = count_data + 1
                    id = toolType + "000" + str(count_data)
                    print("ID : ",id)
                    values = (id,toolPurchaseItem,toolType,merk,new_qty,unit,arrivalDate)
                    cursor.execute(query,values)
            tool_stock = tool_stock + new_qty
        
        print("Tool Stock : ",tool_stock)
        qty_akhir = 0   
        qty_akhir = quantity_purchaseitem - tool_stock
        if qty_akhir < 0:
            qty_akhir = 0
        
        print("QTY akhir : ",qty_akhir)
        query_accumulate_quantity = "UPDATE eqp_d_toolpurchaseitem SET quantity = %s WHERE purchaseItemId = %s"
        values2 = (qty_akhir,toolPurchaseItem)
        cursor.execute(query_accumulate_quantity,values2)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def ShowToolStockNotRegisteredInBox():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id,b.nama,a.merk,a.quantity,a.unit FROM eqp_d_toolstock a JOIN eqp_r_tooltype b ON b.codes = a.toolTypeCode WHERE a.id NOT IN (SELECT b.toolStockId FROM eqp_d_boxitem b)"
    cursor.execute(query)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records :
        json_data.append(dict(zip(row_headers,data)))
  
    return make_response(jsonify(json_data),200)



def ShowToolStock():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id,a.toolTypeCode,a.merk,a.quantity,a.unit,a.arrivalDate FROM eqp_d_toolstock a GROUP BY a.toolTypeCode "
    cursor.execute(query)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records :
        json_data.append(dict(zip(row_headers,data)))
  
    return make_response(jsonify(json_data),200)


def ShowToolTypeInDetailStock(toolTypeCode):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.toolTypeCode,a.merk,a.quantity,a.unit FROM eqp_d_toolstock a WHERE a.toolTypeCode = '"+toolTypeCode+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records :
        json_data.append(dict(zip(row_headers,data)))
  
    return make_response(jsonify(json_data),200)


def ShowToolStockById(toolstock):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id,b.nama,a.merk,a.unit FROM eqp_d_toolstock a JOIN eqp_r_tooltype b ON b.codes = a.toolTypeCode WHERE a.id = '"+toolstock+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records :
        json_data.append(dict(zip(row_headers,data)))
  
    return make_response(jsonify(json_data),200)

    

def ShowToolStockByPurchaseItem(purchaseItem):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id,a.toolTypeCode,c.nama AS 'namaToolType',a.merk,a.quantity,a.unit,a.arrivalDate FROM eqp_d_toolstock a JOIN eqp_d_toolpurchaseitem b ON b.purchaseItemId = a.toolPurchaseItem JOIN eqp_r_tooltype c ON c.codes = a.toolTypeCode WHERE b.purchaseItemId = '"+purchaseItem+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records :
        json_data.append(dict(zip(row_headers,data)))
  
    return make_response(jsonify(json_data),200)



def ShowToolStockByToolType(toolTypeCode):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id,a.merk,a.quantity,a.unit,a.arrivalDate FROM eqp_d_toolstock a WHERE a.toolTypeCode = '"+toolTypeCode+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records :
        json_data.append(dict(zip(row_headers,data)))
  
    return make_response(jsonify(json_data),200)


def ShowToolTypeInDetailStock(toolTypeCode):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.toolTypeCode,a.merk,a.quantity,a.unit FROM eqp_d_toolstock a WHERE a.toolTypeCode = '"+toolTypeCode+"' GROUP BY a.toolTypeCode"
    cursor.execute(query)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records :
        json_data.append(dict(zip(row_headers,data)))
  
    return make_response(jsonify(json_data),200)


def posisiTool():
    conn = database.connector()
    cursor = conn.cursor()
    q00 = f"""SELECT DISTINCT  a. id AS idToolStock, a.toolTypeCode, 
    e.nama, b.boxId, c.stasiunKerja AS SKtool, 
    d.stasiunKerja AS SKBox, a.quantity,
    case
	    when d.stasiunKerja IS NOT NULL then d.stasiunKerja
	    when c.stasiunKerja IS NOT NULL then c.stasiunKerja
    END onWs FROM eqp_d_toolstock a
    LEFT JOIN eqp_d_boxitem b ON a.id = b.toolStockId
    LEFT JOIN eqp_d_toolonws c ON a.id = c.toolStockId
    LEFT JOIN eqp_d_boxonws d ON b.boxId = d.boxId
    LEFT JOIN eqp_r_tooltype e ON e.codes=a.toolTypeCode 
    WHERE c.logout IS NULL"""
    return q00

#SISA TOOL
# MENGETAHUI JUMLAH TOOL YANG SUDAH TERPAKAI (eqp_d_operationtool)
# Tabel C2
def jumlahTotalPemakaianTool():
    q00 = f"""SELECT distinct Z.idToolStock, format(SUM(Z.jumlah), 1) as jumlahTotal FROM eqp_d_operationtool Z
    GROUP BY Z.idToolStock"""
    return q00


#OPERASI SIAP
#MENGETAHUI KEBUTUHAN TOOL UNTUK MELAKUKAN OPERASI (semua operasi)
#Tabel A3
def kebutuhanToolSemuaOperasi():
    q00 =f"""SELECT DISTINCT a.id AS 'idOperasi', b.id AS 'idProses',a.stasiunkerja AS StasiunKerjaOperasi,
    d.toolTypeCode, e.nama, d.Quantity AS jmlhbutuh, f.nama namaUnit, e.isConsumable
    FROM prd_d_operasi a
    left JOIN prd_r_proses b ON a.proses = B.ID 
    left JOIN eqp_r_toolneed d ON d.processCode = b.id
    left JOIN eqp_r_tooltype e ON e.codes = d.toolTypeCode 
    left JOIN gen_r_materialunit f ON f.id = d.Unit"""
    return q00

#SISA TOOL
# MENGETAHUI jumlah toolstock, terpakai berapa, sisa berapa dan posisi dimana
# tabel C3
def SisaToolStockDanPosisi():
    q01 = jumlahTotalPemakaianTool()
    q02 = posisiTool()
    q00 = "SELECT distinct w.id AS idToolStock, w.toolTypeCode, w.quantity AS stok, "
    q00 = q00 + "ifnull(AA1. jumlahTotal,0) As terpakai, "
    q00 = q00 + "(w.quantity-ifnull(AA1. jumlahTotal,0)) AS sisaTS, o.isConsumable, "
    q00 = q00 + "case "
    q00 = q00 + "when o.isConsumable = 1 then (w.quantity-ifnull(AA1. jumlahTotal,0)) "
    q00 = q00 + "when o.isConsumable = 0 then w.quantity "
    q00 = q00 + "END sisaAkhir, CC2.onWs "
    q00 = q00 + "FROM eqp_d_toolstock w left join ("+q01+")AA1 ON w.id = AA1.idToolStock "
    q00 = q00 + "LEFT JOIN eqp_r_tooltype o ON o.codes= w.toolTypeCode left join ("+q02+")CC2 "
    q00 = q00 + "ON w.id=CC2.idToolStock"
    return q00

#Mengetahui jumlah toolstock, jumlah terpakai, jumlah sisa dan posisi dimana
# (Consumable dan non consumable)
# consumable= ambil sisaTS, nonConsumable = quantity toolstock
# tabel C4 agregat tabel C3 (sisa akhir besar>0)
# tabel C3 left join C2 left join tooltype dan C1
def SisaToolStockDanPosisiBesardariNol():
    q01 =  SisaToolStockDanPosisi()
    q00 = "SELECT distinct CC6.idToolStock, CC6.toolTypeCode,CC6.sisaAkhir, CC6.onWs "
    q00 = q00 + "FROM ("+q01+")CC6 WHERE CC6.sisaAkhir>0"
    return q00

## mengetahui jumlah tooltype di Workshop berdasarkan WS
## GROUP BY CC10.toolTypeCode, CC10.onWs
## tabel C6, agregat tabel C4
def jumlahToolTypeByWs():
    q01 = SisaToolStockDanPosisiBesardariNol()
    q00 = "SELECT CC10.toolTypeCode, sum(CC10.sisaAkhir) AS TotalSisa, CC10.onWs FROM ("+q01+")CC10 "
    q00 = q00 + "GROUP BY CC10.toolTypeCode, CC10.onWs"
    return q00

## jumlah tooltype di Workshop secara keseluruhan
## GROUP BY CC11.toolTypeCode
## tabel C7, agregat dari tabel C6
def jumlahToolTypeKeseluruhanDiWorkshop():
    conn = database.connector()
    cursor = conn.cursor()
    q01 = jumlahToolTypeByWs()
    q00 = "SELECT CC11.toolTypeCode, sum(CC11.TotalSisa) as totaltoolOnWs FROM ("+q01+")CC11 "
    q00 = q00 + "GROUP BY CC11.toolTypeCode"
    cursor.execute(q00)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records :
        json_data.append(dict(zip(row_headers,data)))
  
    return make_response(jsonify(json_data),200)

## membandingkan jumlah kebutuhan toolType dan jumlah tool type yang sudah ada di WS
## tabel C8 left join kebutuhan operasi left join C7 (jumlah tooltype di Ws)
## syarat : a.mulai operasi is Null
def KebutuhanOperasiVSjumlahToolTypeKeseluruhanDiWorkshop():
    q01 = jumlahToolTypeKeseluruhanDiWorkshop()
    q00 = "SELECT DISTINCT a.id AS 'idOperasi', a.stasiunkerja AS StasiunKerjaOperasi, "
    q00 = q00 + "d.toolTypeCode,e.nama, d.Quantity AS jmlhbutuh, CC12.totaltoolOnWs, "
    q00 = q00 + "f.nama namaUnit, e. isConsumable FROM prd_d_operasi a "
    q00 = q00 + "left JOIN prd_r_proses b ON a.proses = b.ID "
    q00 = q00 + "left JOIN eqp_r_toolneed d ON d.processCode = b.id "
    q00 = q00 + "left JOIN eqp_r_tooltype e ON e.codes = d.toolTypeCode "
    q00 = q00 + "left JOIN gen_r_materialunit f ON f.id = d.Unit "
    q00 = q00 + "Left join ("+q01+")CC12 "
    q00 = q00 + "ON d.toolTypeCode = CC12.toolTypeCode WHERE a.mulai IS NULL"
    return q00


## membandingkan jumlah kebutuhan toolType dan jumlah tool type yang sudah ada di WS
## untuk operasi yang ada di CPL Layak paling awal
## table C9, tabel C8 tambah syarat Id operasinya ada di CPL_oprLayak diurutkan dari rencana mulai
def kebutuhanOperasiVSTotalToolBerdasarkanOPRLayak(ws00):
    q01 = KebutuhanOperasiVSjumlahToolTypeKeseluruhanDiWorkshop()
    q00 = q01 + " AND a.id = (SELECT b.id FROM cpl_oprlayak b WHERE b.stasiunKerja='"+ws00+"'"
    q00 = q00 + "ORDER BY b.rencanaMulai LIMIT 1)"
    return q00


## membandingkan jumlah kebutuhan toolType dan jumlah tool type yang sudah ada di WS
## table C10, tabel C9 tambah syarat: jumlah butuh > jumlah tool yang ada di ws
## query dasar kebutuhan tool di WS tertentu
def kebutuhanOperasiBesarDariTotalToolBerdasarkanOPRLayak():
    q01 = kebutuhanOperasiVSTotalToolBerdasarkanOPRLayak()
    q00 = q01 + " AND d.Quantity>CC12.totaltoolOnWs"
    return q00

## jumlah kebutuhan dan total tool di WS untuk operasi layak pertama, diketahui kekurangannya
## tabel C11, tabel C9 (ditambah kolom kekurangan dan kurang)
def KekuranganToolOprLayakPertama(ws00):
    q01 = jumlahToolTypeKeseluruhanDiWorkshop()
    q00 = "SELECT DISTINCT a.id AS 'idOperasi', a.stasiunkerja AS StasiunKerjaOperasi, "
    q00 = q00 + "d.toolTypeCode,e.nama, d.Quantity AS jmlhbutuh, CC12.totaltoolOnWs, "
    q00 = q00 + "(d.Quantity - CC12.totaltoolOnWs) AS kurang, "
    q00 = q00 + "case "
    q00 = q00 + "when (d.Quantity - CC12.totaltoolOnWs) < 0 then 0 "
    q00 = q00 + "when (d.Quantity - CC12.totaltoolOnWs) >=0 then (d.Quantity - CC12.totaltoolOnWs) "
    q00 = q00 + "END kekurangan, f.nama namaUnit, e. isConsumable "
    q00 = q00 + "FROM prd_d_operasi a "
    q00 = q00 + "left JOIN prd_r_proses b ON a.proses = b.ID "
    q00 = q00 + "left JOIN eqp_r_toolneed d ON d.processCode = b.id "
    q00 = q00 + "left JOIN eqp_r_tooltype e ON e.codes = d.toolTypeCode "
    q00 = q00 + "left JOIN gen_r_materialunit f ON f.id = d.Unit "
    q00 = q00 + "left JOIN ("+q01+")CC12 ON d.toolTypeCode = CC12.toolTypeCode WHERE a.mulai IS NULL "
    q00 = q00 + "AND a.id = (SELECT b.id FROM cpl_oprlayak b WHERE b.stasiunKerja='"+ws00+"'"
    q00 = q00 + "ORDER BY b.rencanaMulai LIMIT 1)"
    return q00

def KekuranganOprLayakByRencanaMulai(ws00):
    q01 = KekuranganToolOprLayakPertama(ws00)
    q00 = "SELECT CC15.nama AS namaTool, CC15.toolTypeCode, "
    q00 = q00 + "CC15.jmlhbutuh, CC15.kekurangan, CC15.StasiunKerjaOperasi FROM ("+q01+")CC15"
    return q00



