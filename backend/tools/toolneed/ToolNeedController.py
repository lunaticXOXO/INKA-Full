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

def jumlahTotalPemakaianTool():
    q00 = f"""SELECT distinct Z.idToolStock, format(SUM(Z.jumlah), 1) as jumlahTotal FROM eqp_d_operationtool Z
    GROUP BY Z.idToolStock"""
    return q00


def kebutuhanToolSemuaOperasi():
    q00 =f""" SELECT DISTINCT a.id AS 'idOperasi', b.id AS 'idProses', 
    a.stasiunkerja AS StasiunKerjaOperasi,
    d.toolTypeCode, e.nama, d.Quantity AS jmlhbutuh, f.nama namaUnit, 
    e.isConsumable, a.rencanaMulai, e.notes
    FROM prd_d_operasi a
    left JOIN prd_r_proses b ON a.proses = B.ID 
    left JOIN eqp_r_toolneed d ON d.processCode = b.id
    left JOIN eqp_r_tooltype e ON e.codes = d.toolTypeCode 
    left JOIN gen_r_materialunit f ON f.id = d.Unit where a.mulai is null"""
    return q00



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


def SisaToolStockDanPosisiBesardariNol():
    q01 = SisaToolStockDanPosisi()
    q00 = "SELECT distinct CC6.idToolStock, CC6.toolTypeCode, CC6.sisaAkhir, CC6.onWs "
    q00 = q00 + "FROM ("+q01+")CC6 WHERE CC6.sisaAkhir>0"
    return q00

def SisaToolStockByToolType():
    q01 = SisaToolStockDanPosisiBesardariNol()
    q00 = "SELECT CC10.toolTypeCode, sum(CC10.sisaAkhir) AS TotalSisa, "
    q00 = q00 + "CC10.onWs from ("+q01+")CC10 "
    q00 = q00 + "GROUP BY CC10.toolTypeCode"
    return q00

def sisaToolStockBytoolTypeAndOnws():
    q01 = SisaToolStockByToolType()
    q00 = q01 + ", CC10.onWs"
    return q00


def kebutuhanToolSemuaOperasi():
    q00 =f"""SELECT DISTINCT a.id AS 'idOperasi', b.id AS 'idProses', 
    a.stasiunkerja AS StasiunKerjaOperasi,
    d.toolTypeCode, e.nama, d.Quantity AS jmlhbutuh, f.nama namaUnit, 
    e.isConsumable, a.rencanaMulai, e.notes
    FROM prd_d_operasi a
    left JOIN prd_r_proses b ON a.proses = B.ID 
    left JOIN eqp_r_toolneed d ON d.processCode = b.id
    left JOIN eqp_r_tooltype e ON e.codes = d.toolTypeCode 
    left JOIN gen_r_materialunit f ON f.id = d.Unit where a.mulai is null"""
    return q00


def kebutuhanPerkakasSesuaiTanggal(tgl00,tgl01):
    q01= kebutuhanToolSemuaOperasi()
    q00 = q01 + " and a.rencanaMulai >= '"+tgl00+"' AND a.rencanaMulai <= '"+tgl01+"'"
    return q00



def kebutuhanPerkakasAllWs(tgl00,tgl01):
    q01 = kebutuhanPerkakasSesuaiTanggal(tgl00,tgl01)
    q00 = "SELECT EE1.toolTypeCode,EE1.nama, sum(EE1.jmlhbutuh) as butuh, "
    q00 = q00 + "CAST(EE1.rencanaMulai AS DATE) AS tanggal, EE1.StasiunKerjaOperasi, EE1.notes "
    q00 = q00 + "FROM ("+q01+")EE1 GROUP BY EE1.toolTypeCode, EE1.stasiunKerjaOperasi"
    return q00


def kebutuhanPerkakasDiLantaiProduksi(tgl00, tgl01):
    q01 = kebutuhanPerkakasSesuaiTanggal(tgl00,tgl01)
    q00 = "SELECT GG1.toolTypeCode, GG1.nama, sum(GG1.jmlhbutuh) AS butuh, "
    q00 = q00 + "CAST(GG1.rencanaMulai AS DATE) AS tanggal "
    q00 = q00 + "FROM ("+q01+")GG1 group by GG1.toolTypeCode"
    return q00



def kebutuhanPerkakasSesuaiWS(tgl00, tgl01, ws00):
    q01 = kebutuhanPerkakasSesuaiTanggal(tgl00,tgl01)
    q00 = "SELECT EE1.toolTypeCode,EE1.nama, sum(EE1.jmlhbutuh) as butuh, "
    q00 = q00 + "EE1.stasiunKerjaOperasi, CAST(EE1.rencanaMulai AS DATE) AS tanggal, EE1.notes AS kelompok "
    q00 = q00 + "FROM ("+q01+")EE1 "
    q00 = q00 + "where EE1.stasiunKerjaOperasi='"+ws00+"' "
    q00 = q00 + "GROUP BY EE1.toolTypeCode, EE1.stasiunKerjaOperasi "
    q00 = q00 + "ORDER BY EE1.stasiunKerjaOperasi"
    return q00



def kebutuhanPerkakasdanStokPerkakas(tgl00,tgl01,ws00):
    q01 = kebutuhanPerkakasSesuaiWS(tgl00, tgl01, ws00)
    q02 = SisaToolStockByToolType()
    q00 = "SELECT GG1.toolTypeCode, GG1.nama AS namaTool, sum(GG1.butuh) AS butuh, "
    q00 = q00 + "sum(GG2.TotalSisa)AS Stok, GG1.stasiunKerjaOperasi, GG1.tanggal "
    q00 = q00 + "FROM ("+q01+")GG1 "
    q00 = q00 + "left join ("+q02+")GG2 on GG1.toolTypeCode = GG2.toolTypeCode "
    q00 = q00 + "GROUP BY GG1.toolTypeCode"
    return q00



def kebutuhanPengadaan(tgl00,tgl01,ws00):
    q01 = kebutuhanPerkakasdanStokPerkakas(tgl00,tgl01,ws00)
    q00 = "SELECT GG3.toolTypeCode, GG3.namaTool, GG3.butuh, GG3.Stok, "
    q00 = q00 + "(GG3.butuh-GG3.Stok) as pengadaan, "
    q00 = q00 + "case when (GG3.butuh-GG3.Stok) <0 then 0 "
    q00 = q00 + "when (GG3.butuh-GG3.Stok) >=0 then (GG3.butuh-GG3.Stok) "
    q00 = q00 + "END pengadaanTool, GG3.stasiunKerjaOperasi,GG3.tanggal "
    q00 = q00 + "FROM ("+q01+")GG3"
    return q00


def PengadaanPerkakas(tgl00,tgl01, ws00):
    q01 = kebutuhanPengadaan(tgl00,tgl01, ws00)
    q00 = "SELECT GG4.toolTypeCode, GG4.namaTool, GG4.butuh, GG4.Stok, "
    q00 = q00 + "GG4.pengadaanTool, GG4.stasiunKerjaOperasi, GG4.tanggal FROM ("+q01+")GG4"
    return q00


def jumlahBarisKebutuhanVsStokSaatIni(tgl00, tgl01, ws00, cur00):
    con00 = database.connector()
    cur00 = con00.cursor()
    q01 = PengadaanPerkakas(tgl00,tgl01, ws00)
    q00 = "SELECT COUNT(*) FROM (" + q01 + ")GG5"
    cur00.execute(q00)
    tabel00 = cur00.fetchone()
    jml00 = tabel00[0]
    return jml00


def insertCPLtoolButuhStok01(tgl00, tgl01, ws00, cur00,con00):
    con00 = database.connector()
    cur00 = con00.cursor()
    try:
        jmlBaris = jumlahBarisKebutuhanVsStokSaatIni(tgl00, tgl01, ws00, cur00)
        if (jmlBaris > 0):
            q02 = "delete from cpl_toolbutuhstok01 where tanggal>= '" + tgl00 + "'"
            q02 = q02 + "AND tanggal <= '" + tgl01 + "' and stasiunKerja= '" + ws00 + "'"
            cur00.execute(q02)
            con00.commit()
            q00 = PengadaanPerkakas(tgl00,tgl01, ws00)
            cur00.execute(q00)
            tabel00 = cur00.fetchall()
            #print(tabel00)
            for data in tabel00:
                toolType00 = data[0]
                nama00 = data[1]
                butuh00 = data[2]
                stok00 = data[3]
                pesan00 = data[4]
                stasiunKerja00 = data[5]
                tgl00 = data[6]
                q01 = "INSERT INTO cpl_toolbutuhstok01 (toolTypeCode, namaTool, butuh, stock, pengadaanTool, stasiunKerja, tanggal) \
                VALUES  ('" + toolType00 + "','" + nama00 + "', '" + str(butuh00) + "', '" + str(stok00) + "', \
                '" + str(pesan00) + "','" + stasiunKerja00 + "','" + str(tgl00) + "')"
                cur00.execute(q01)
                con00.commit()
        print('selesai')
        hasil = True
    except Exception as e:
        print("error",str(e))
        hasil = False
    return hasil


def insertCPLtoolButuhStok02(tgl00, tgl01, ws00, cur00,con00):
    con00 = database.connector()
    cur00 = con00.cursor()
    jmlBaris = jumlahBarisKebutuhanVsStokSaatIni(tgl00, tgl01, ws00, cur00)
    if (jmlBaris > 0):
        # q02 = "delete from cpl_toolbutuhstok"
        # cur00.execute(q02)
        # con00.commit()
        q00 = PengadaanPerkakas(tgl00,tgl01, ws00)
        cur00.execute(q00)
        tabel00 = cur00.fetchall()
        #print(tabel00)
        for data in tabel00:
            toolType00 = data[0]
            nama00 = data[1]
            butuh00 = data[2]
            stok00 = data[3]
            pesan00 = data[4]
            stasiunKerja00 = data[5]
            tgl00 = data[6]
            q01 = "INSERT INTO cpl_toolbutuhstok02 (toolTypeCode, namaTool, butuh, stock, pengadaanTool, stasiunKerja, tanggal) \
            VALUES  ('" + toolType00 + "','" + nama00 + "', '" + str(butuh00) + "', '" + str(stok00) + "', \
            '" + str(pesan00) + "','" + stasiunKerja00 + "','" + str(tgl00) + "')"
            cur00.execute(q01)
            con00.commit()
    print('selesai')


def CPLToolButuhOpr01NotIn02(ws00,tgl00,tgl01):
    q00 = "SELECT a.toolTypeCode, a.namaTool FROM cpl_kirimtool01 a \
    WHERE a.toolTypeCode  NOT IN (SELECT b.toolTypeCode FROM cpl_kirimtool02 b) \
    AND a.stasiunKerja = '" + ws00 + "' and a.tanggal >= '" + tgl00 + "' \
    AND a.tanggal <= '" + tgl01 + "'"
    return q00

def insertToolbutuh02(ws00,cur00,con00,tgl00,tgl01):
    q00 = "INSERT INTO cpl_toolbutuhstok02 (toolTypeCode, namaTool, butuh, stock, "
    q00 = q00 + "pengadaanTool, stasiunKerja, tanggal) "
    q00 = q00 + "(SELECT a.toolTypeCode, a.namaTool, a.butuh, a.stock, "
    q00 = q00 + "a.pengadaanTool, a.stasiunKerja, a.tanggal "
    q00 = q00 + "from cpl_toolbutuhstok01 a WHERE a.stasiunKerja = '" + ws00 + "' "
    q00 = q00 + "and a.tanggal >= '" + tgl00 + "' "
    q00 = q00 + "AND a.tanggal <= '" + tgl01 + "' "
    q00 = q00 + "AND a.toolTypeCode NOT IN (SELECT a.toolTypeCode from cpl_toolbutuhstok02 a "
    q00 = q00 + "WHERE a.stasiunKerja = '" + ws00 + "' and a.tanggal >= '" + tgl00 + "' "
    q00 = q00 + "AND a.tanggal <= '" + tgl01 + "')) "
    return q00


# tabel B4  mengetahui tooltype yang ada di toolbutuhstock02 ga ada di toolbutuhstock01 yang dilakukan pada ws sama
def stock02NotInStock01(ws00,tgl00,tgl01):
    q00 = "SELECT g.toolTypeCode, g.namaTool, g.butuh, g.stock, g.pengadaanTool, g.stasiunKerja, g.tanggal \
    FROM cpl_toolbutuhstok02 g WHERE g.toolTypeCode NOT IN \
    (SELECT h.toolTypeCode FROM cpl_toolbutuhstok01 h) AND g.stasiunKerja = '" + ws00 + "' and g.tanggal >= '" + tgl00 + "' \
    AND g.tanggal <= '" + tgl01 + "'"
    return q00

def stock02NotInStock011(ws00,tgl00,tgl01):
    q00 = "SELECT g.toolTypeCode FROM cpl_toolbutuhstok02 g WHERE g.toolTypeCode NOT IN \
    (SELECT h.toolTypeCode FROM cpl_toolbutuhstok01 h) AND g.stasiunKerja = '" + ws00 + "' and g.tanggal >= '" + tgl00 + "' \
    AND g.tanggal <= '" + tgl01 + "'"
    return q00

def deleteCplStock02(ws00,tgl00,tgl01):
    q01 = stock02NotInStock011(ws00,tgl00,tgl01)
    q00 = "delete from cpl_toolbutuhstok02 where stasiunKerja = '" + ws00 + "' and tanggal >= '" + tgl00 + "' \
    AND tanggal <= '" + tgl01 + "' AND toolTypeCode IN (" + q01 + ")"
    return q00

def updateCplStock02(ws00,tgl00,tgl01):
    q00 = "UPDATE cpl_toolbutuhstok02 e SET e.pengadaanTool = (SELECT f.pengadaanTool "
    q00 = q00 + "FROM cpl_toolbutuhstok01 f WHERE f.stasiunKerja='" + ws00 + "' AND "
    q00 = q00 + "e.toolTypeCode = f.toolTypeCode), e.butuh = (SELECT f.butuh "
    q00 = q00 + "FROM cpl_toolbutuhstok01 f WHERE f.stasiunKerja='" + ws00 + "' AND "
    q00 = q00 + "e.toolTypeCode = f.toolTypeCode), e.stock = (SELECT f.stock "
    q00 = q00 + "FROM cpl_toolbutuhstok01 f WHERE f.stasiunKerja='" + ws00 + "' AND "
    q00 = q00 + "e.toolTypeCode = f.toolTypeCode) WHERE e.stasiunKerja='" + ws00 + "' and e.tanggal >= '" + tgl00 + "' "
    q00 = q00 + "AND tanggal <= '" + tgl01 + "'"
    return q00

def butuhToolStock(ws00,tgl00,tgl01):
    con00 = database.connector()
    cur00 = con00.cursor()
    try:
        q00 = "delete from cpl_toolbutuhstok01 where stasiunKerja = '" + ws00 + "' and tanggal >= '" + tgl00 + "' "
        q00 = q00 + "AND tanggal <= '" + tgl01 + "'"
        cur00.execute(q00)
        con00.commit()

        output_insert = insertCPLtoolButuhStok01(tgl00, tgl01, ws00, cur00, con00)
        if output_insert == True:
            q02 = insertToolbutuh02(ws00,cur00,con00,tgl00,tgl01)
            cur00.execute(q02)
            con00.commit()
            q03 = deleteCplStock02(ws00,tgl00,tgl01)
            cur00.execute(q03)
            con00.commit()
            q04 = updateCplStock02(ws00,tgl00,tgl01)
            cur00.execute(q04)
            con00.commit()
            return True
    except Exception as e:
        print("error",str(e))
        return False


def MergeButuhToolStock():
    try:
        data = request.json
        tgl00 = data["rencanaMulaiA"]
        tgl01 = data["rencanaMulaiB"]
        ws = data["workstation"]
        final = butuhToolStock(ws,tgl00,tgl01)
        if final == True:
            hasil = {"status" : "berhasil"}
        else:
            hasil = {"status" : "gagal"}
    except Exception as e:
        hasil = {"status" : "error"}
        print("error",str(e))
    return hasil