import db.db_handler as database
from flask import request,make_response,jsonify

def posisiTool():
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


def ShowposisiTools():
    con00 = database.connector()
    cur00 = con00.cursor()

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

    cur00.execute(q00)
    records = cur00.fetchall()

    row_headers = [x[0] for x in cur00.description]
    json_data = []
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return  make_response(jsonify(json_data),200)
   

def ShowPosisiToolsByName(namatools):
    con00 = database.connector()
    cur00 = con00.cursor()

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
    WHERE c.logout IS NULL """

    cur00.execute(q00)
    records = cur00.fetchall()
    records_temp = []

    for index in records:
       
        if index[2] == namatools and index[4] != None:
            records_temp.append(index)
            

    
    row_headers = [x[0] for x in cur00.description]
    json_data = []
    
    for data in records_temp:
        json_data.append(dict(zip(row_headers,data)))
    
    return  make_response(jsonify(json_data),200)

#SISA TOOL
# MENGETAHUI JUMLAH TOOL YANG SUDAH TERPAKAI (eqp_d_operationtool)
# Tabel C2
def jumlahTotalPemakaianTool():
    q00 = f"""SELECT distinct Z.idToolStock, format(SUM(Z.jumlah), 1) as jumlahTotal FROM eqp_d_operationtool Z
    GROUP BY Z.idToolStock"""
    return q00

#OPERASI SIAP
#MENGETAHUI KEBUTUHAN TOOL UNTUK MELAKUKAN OPERASI (semua operasi)
#Tabel A3 atau H1
def kebutuhanToolSemuaOperasi():
    q00 = f"""SELECT DISTINCT a.id AS 'idOperasi', b.id AS 'idProses',a.stasiunkerja AS StasiunKerjaOperasi,
    d.toolTypeCode, e.nama, d.Quantity AS jmlhbutuh, f.nama namaUnit, e.isConsumable, a.rencanaMulai, e. notes
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
    q01 = SisaToolStockDanPosisi()
    q00 = "SELECT distinct CC6.idToolStock, CC6.toolTypeCode, CC6.sisaAkhir, CC6.onWs "
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

## pendistribusian Tool
def kebutuhanToolPerhari(tgl00, tgl01):
    q00 = "SELECT DISTINCT a.id AS 'idOperasi', b.id AS 'idProses', "
    q00 = q00 + "a.stasiunkerja AS StasiunKerjaOperasi, d.toolTypeCode,e.nama, "
    q00 = q00 + "d.Quantity AS jmlhbutuh, f.nama as Unit , a.rencanaMulai, e.notes "
    q00 = q00 + "FROM prd_d_operasi a "
    q00 = q00 + "left JOIN prd_r_proses b ON a.proses = b.ID "
    q00 = q00 + "left JOIN eqp_r_toolneed d ON d.processCode = b.id "
    q00 = q00 + "left JOIN eqp_r_tooltype e ON e.codes = d.toolTypeCode "
    q00 = q00 + "left JOIN gen_r_materialunit f ON f.id = d.Unit "
    q00 = q00 + "WHERE a.rencanaMulai >= '"+tgl00+"' AND a.rencanaMulai <= '"+tgl01+"' "
    q00 = q00 + "and a.mulai IS NULL"
    return q00

def jumlahKirimTool(tgl00, tgl01, ws00):
    q01 = kebutuhanToolPerhari(tgl00, tgl01)
    q00 = "SELECT EE1.toolTypeCode,EE1.nama, sum(EE1.jmlhbutuh) as butuh, EE1.Unit, "
    q00 = q00 + "EE1.stasiunKerjaOperasi, CAST(EE1.rencanaMulai AS DATE) AS tanggal, EE1.notes as kelompok "
    q00 = q00 + "FROM ("+q01+")EE1 "
    q00 = q00 + "where EE1.stasiunKerjaOperasi='"+ws00+"'"
    q00 = q00 + " GROUP BY EE1.toolTypeCode, EE1.stasiunKerjaOperasi "
    q00 = q00 + "ORDER BY EE1.stasiunKerjaOperasi"
    return q00


def jumlahBarisKirimTool(tgl00, tgl01, ws00):
    con00 = database.connector()
    cur00 = con00.cursor()
    q01 = jumlahKirimTool(tgl00, tgl01, ws00)
    q00 = "Select Count(*) from("+q01+")FF11"
    cur00.execute(q00)
    tabel00 = cur00.fetchone()
    jml00 = int(tabel00[0])
    return jml00

# tabel B5
# jumlah kebutuhan tool type di WS tertentu
# left join C6 (jumlah tooltypebyWS) diketahui kekurangan pendistribusian dan ada di WS mana
def jumlahKebutuhanToolTypeVSKekuranganDistribusiTool(tgl00, tgl01, ws00):
    q01 = jumlahKirimTool(tgl00, tgl01, ws00)
    q02 = jumlahToolTypeByWs()
    q00 = "SELECT FF11.toolTypeCode, FF11.nama, FF11.butuh, ifnull(FF12.TotalSisa,0) AS stok, "
    q00 = q00 + "((FF11.butuh-ifnull(FF12.TotalSisa,0)))as kekurangan, FF11.kelompok, FF12.onWs, "
    q00 = q00 + "case "
    q00 = q00 + "when FF12.onWs IS NOT NULL then FF12.onWs "
    q00 = q00 + "when FF12.onWs	IS NULL then '"+ws00+"' "
    q00 = q00 + "END onWs01, FF11.tanggal FROM ("+q01+")FF11 "
    q00 = q00 + "LEFT JOIN ("+q02+")FF12 ON FF11.stasiunKerjaOperasi = FF12.onWs "
    q00 = q00 + "AND FF11.toolTypeCode = FF12.toolTypeCode"
    return q00

def kekuranganPendistribusianTool(tgl00, tgl01, ws00):
    q01 = jumlahKebutuhanToolTypeVSKekuranganDistribusiTool(tgl00, tgl01, ws00)
    q00 = "SELECT FF13.toolTypeCode, FF13.nama, FF13.butuh, FF13.Kekurangan AS kurang, "
    q00 = q00 + "case when FF13.Kekurangan <0 then 0 when FF13.Kekurangan >= 0 then FF13.Kekurangan end Kekurangan, "
    q00 = q00 + "FF13.onWs01 AS onWs, FF13.tanggal, FF13.kelompok from ("+q01+")FF13"
    return q00

# tgl00 = '2023-06-16 00:00:00'
# tgl01 = '2023-06-17 00:00:00'
# ws00 = "WS03"
# q00 = kekuranganPendistribusianTool(tgl00, tgl01, ws00)
# print (q00)


def kekuranganPendistribusianTool01(tgl00, tgl01,ws00):
    q01 = kekuranganPendistribusianTool(tgl00, tgl01, ws00)
    q00 = "Select FF14.toolTypeCode, FF14.nama, FF14.butuh, "
    q00 = q00 + "FF14.Kekurangan, FF14.onWs, FF14.tanggal, FF14.kelompok From ("+q01+")FF14"
    return q00

def jumlahBariskekuranganPendistribusianTool(tgl00, tgl01, ws00):
    con00 = database.connector()
    cur00 = con00.cursor()
    q01 = kekuranganPendistribusianTool01(tgl00, tgl01,ws00)
    q00 = "select Count(*) from("+q01+")FF14"
    cur00.execute(q00)
    tabel00 = cur00.fetchone()
    jml00 = int(tabel00[0])
    return jml00

def insertCPLKirimTool01(tgl00, tgl01, ws00):
    con00 = database.connector()
    cur00 = con00.cursor()
    try:
        jmlBaris = jumlahBariskekuranganPendistribusianTool(tgl00,tgl01,ws00)
        if (jmlBaris > 0):
            q02 = "delete from cpl_kirimtool01 where tanggal>= '" + tgl00 + "'"
            q02 = q02 + "AND tanggal <= '" + tgl01 + "' and stasiunKerja= '" + ws00 + "'"
            cur00.execute(q02)
            con00.commit()
            q00 = kekuranganPendistribusianTool01(tgl00, tgl01,ws00)
            cur00.execute(q00)
            tabel00 = cur00.fetchall()
            #print(tabel00)
            for data in tabel00:
                nama00 = data[1]
                toolType00 = data[0]
                butuh00 = data[2]
                kurang00 = data[3]
                stasiunKerja00 = data[4]
                tgl00 = data[5]
                klp00 = data[6]
                q01 = "INSERT INTO cpl_kirimtool01 (toolTypeCode, namaTool, butuh, kurangPengemasan , stasiunKerja, tanggal, kelompok) \
                VALUES ('" + toolType00 + "','" + nama00 + "', '" + str(butuh00) + "', '" + str(kurang00) + "', \
                '" + stasiunKerja00 + "', '" + str(tgl00) + "', '" + str(klp00) + "')"
                cur00.execute(q01)
                con00.commit()
        hasil = True
        # print('selesai')
    except Exception as e:
        hasil = False
        print("error",str(e))
    return hasil

def insertCPLKirimTool02(tgl00, tgl01, ws00):
    con00 = database.connector()
    cur00 = con00.cursor()
    try:
        jmlBaris = jumlahBariskekuranganPendistribusianTool(tgl00, tgl01, ws00)
        if (jmlBaris > 0):
            q00 = kekuranganPendistribusianTool01(tgl00, tgl01,ws00)
            cur00.execute(q00)
            tabel00 = cur00.fetchall()
            #print(tabel00)
            for data in tabel00:
                nama00 = data[1]
                toolType00 = data[0]
                butuh00 = data[2]
                kurang00 = data[3]
                stasiunKerja00 = data[4]
                tgl00 = data[5]
                klp00 = data[6]
                q01 = "INSERT INTO cpl_kirimtool02 (toolTypeCode, namaTool, butuh, kurangPengemasan, stasiunKerja, tanggal, kelompok) \
                VALUES ('" + toolType00 + "','" + nama00 + "', '" + str(butuh00) + "', '" + str(kurang00) + "', \
                '" + stasiunKerja00 + "', '" + str(tgl00) + "', '" + str(klp00) + "')"
                cur00.execute(q01)
                con00.commit()
        hasil = True
        print('selesai')
    except Exception as e:
        hasil = False
        print("error",str(e))
    return hasil

# tabel B1
# Query untuk mengetahui data yang ada di CPLkirimtool01 tetapi tidak ada di CPL CPLkirimtool02
# yang ditampilkan tooltype saja
def CPLToolButuhOpr01NotIn02(ws00,tgl00,tgl01):
    q00 = "SELECT a.toolTypeCode, a.namaTool FROM cpl_kirimtool01 a \
    WHERE a.toolTypeCode  NOT IN (SELECT b.toolTypeCode FROM cpl_kirimtool02 b) \
    AND a.stasiunKerja = '" + ws00 + "' and a.tanggal >= '" + tgl00 + "' \
    AND a.tanggal <= '" + tgl01 + "'"
    return q00

# tabel B2  memasukkan tool yang ada toolbutuhopr01 tapi ga da di toolbutuhopr02 ke toolbutuhopr02
def insertKrm02(ws00,tgl00,tgl01):
    con00 = database.connector()
    cur00 = con00.cursor()
    q00 = "INSERT INTO cpl_kirimtool02(toolTypeCode, namaTool, butuh, kurangPengemasan, stasiunKerja, tanggal, kelompok) "
    q00 = q00 + "SELECT a.toolTypeCode, a.namaTool, a.butuh, a.kurangPengemasan , a.stasiunKerja, a.tanggal, a.kelompok "
    q00 = q00 + "from cpl_kirimtool01 a WHERE a.stasiunKerja = '"+ws00+"' and a.tanggal >= '"+tgl00+"' "
    q00 = q00 + "AND a.tanggal <= '"+tgl01+"' AND a.toolTypeCode NOT IN(SELECT a.toolTypeCode from cpl_kirimtool02 a "
    q00 = q00 + "WHERE a.stasiunKerja = '"+ws00+"' and a.tanggal >= '"+tgl00+"' AND a.tanggal <= '"+tgl01+"')"
    cur00.execute(q00)
    con00.commit()


# def insertKrm02(ws00,tgl00,tgl01):
#     q00 = "INSERT INTO cpl_kirimtool02 (toolTypeCode, namaTool, butuh, kekuranganPendistribusian, stasiunKerja, tanggal, kelompok) "
#     q00 = q00 + "(SELECT d.toolTypeCode, d.namaTool, d.butuh, d.kekuranganPendistribusian, d.stasiunKerja, d.tanggal, d.kelompok "
#     q00 = q00 + "FROM cpl_kirimtool01 d WHERE d.stasiunKerja = '"+ws00+"' "
#     q00 = q00 + "AND d.toolTypeCode IN (SELECT a.toolTypeCode FROM cpl_kirimtool01 a "
#     q00 = q00 + "WHERE a.toolTypeCode  NOT IN (SELECT b.toolTypeCode FROM cpl_kirimtool02 b) "
#     q00 = q00 + "AND a.stasiunKerja = @ws AND a.tanggal >= '"+tgl00+"' "
#     q00 = q00 + "AND a.tanggal <= '"+tgl01+"'))"

# tabel B4  mengetahui tooltype yang ada di toolbutuhopr02 ga ada di butuhopr01 yang dilakukan pada ws sama
def krm02NotInKrm01(ws00):
    q00 = "SELECT g.toolTypeCode, g.namaTool, g.butuh, g.kurangPengemasan , g.stasiunKerja, g.tanggal, g.kelompok \
    FROM cpl_kirimtool02 g WHERE g.toolTypeCode NOT IN \
    (SELECT h.toolTypeCode FROM cpl_kirimtool01 h) AND g.stasiunKerja = '" + ws00 + "'"
    return q00

def krm02NotInKrm011(ws00):
    q00 = "SELECT g.toolTypeCode FROM cpl_kirimtool02 g WHERE g.toolTypeCode NOT IN \
    (SELECT h.toolTypeCode FROM cpl_kirimtool01 h) AND g.stasiunKerja = '" + ws00 + "'"
    return q00

def deleteCplKrm02(ws00):
    q01 = krm02NotInKrm011(ws00)
    q00 = "delete from cpl_kirimtool02 where stasiunKerja = '" + ws00 + "' \
    AND toolTypeCode IN (" + q01 + ")"
    return q00

# def updateCplKrm02(ws00):
#     q00 = "UPDATE cpl_kirimtool02 e SET e.kekuranganPendistribusian = (SELECT f.kekuranganPendistribusian "
#     q00 = q00 + "FROM cpl_kirimtool01 f WHERE f.stasiunKerja='" + ws00 + "' AND "
#     q00 = q00 + "e.toolTypeCode = f.toolTypeCode) WHERE e.stasiunKerja='" + ws00 + "'"
#     return q00
def updateCplKrm02(ws00,tgl00,tgl01):
    q00 = "UPDATE cpl_kirimtool02 e SET e.kurangPengemasan  = "
    q00 = q00 + "(SELECT f.kurangPengemasan  FROM cpl_kirimtool01 f "
    q00 = q00 + "WHERE f.stasiunKerja='" + ws00 + "' AND f.tanggal >= '" + tgl00 + "' "
    q00 = q00 + "AND f.tanggal <= '" + tgl00 + "'"
    q00 = q00 + "AND e.toolTypeCode = f.toolTypeCode and e.tanggal = f.tanggal), e.tanggal= "
    q00 = q00 + "(SELECT f.tanggal FROM cpl_kirimtool01 f "
    q00 = q00 + "WHERE f.stasiunKerja='" + ws00 + "' AND f.tanggal >= '" + tgl00 + "'"
    q00 = q00 + "AND f.tanggal <= '" + tgl01+ "'"
    q00 = q00 + "AND e.toolTypeCode = f.toolTypeCode and e.tanggal = f.tanggal), e.kurangPengemasan = "
    q00 = q00 + "(SELECT f.kurangPengemasan FROM cpl_kirimtool01 f "
    q00 = q00 + "WHERE f.stasiunKerja='" + ws00 + "' AND f.tanggal >= '" + tgl00 + "'"
    q00 = q00 + "AND f.tanggal <= '" + tgl01+ "'"
    q00 = q00 + "AND e.toolTypeCode = f.toolTypeCode and e.tanggal = f.tanggal) "
    q00 = q00 + "WHERE e.stasiunKerja='" + ws00 + "' "
    return q00

def kirimTool_distribution():
    con00 = database.connector()
    cur00 = con00.cursor()
    try:
        data = request.json
        tgl00 = data["tgl00"]
        tgl01 = data["tgl01"]
        ws00 = data["ws00"]
        q00 = "delete from cpl_kirimtool01 where stasiunKerja = '" + ws00 + "'"
        cur00.execute(q00)
        con00.commit()

        if insertCPLKirimTool01(tgl00, tgl01, ws00) == True:
        
            insertKrm02(ws00,tgl00,tgl01)
            q03 = deleteCplKrm02(ws00)
            q04 = updateCplKrm02(ws00,tgl00,tgl01)
            cur00.execute(q03)
            cur00.execute(q04)

            con00.commit()
            hasil = {"status" : "berhasil"}
    except Exception as e:
        hasil = {"status" : "gagal"}
        print("error",str(e))
    return hasil

def peminjaman_tools():
    return kirimTool_distribution()
