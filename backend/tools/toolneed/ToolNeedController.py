import db.db_handler as database
from flask import request,make_response,jsonify

def ShowToolNeedByProcess(idProcess):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.toolTypeCode,c.nama AS 'namaTool',a.processCode,b.nama AS 'namaProses',a.quantity FROM eqp_r_toolneed a JOIN prd_r_proses b ON b.id = a.processCode JOIN eqp_r_tooltype c ON c.codes = a.toolTypeCode WHERE b.id = '"+idProcess+"'"
    cursor.execute(query)

    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return  make_response(jsonify(json_data),200)


def insertToolNeedByProcess(idProcess):
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO eqp_r_toolneed(toolTypeCode,processCode,quantity,unit)VALUES(%s,%s,%s,%s)"
    try:
        data = request.json
        toolTypeCode = data["toolTypeCode"]
        quantity = data["quantity"]
        unit = data["unit"]
        values = (toolTypeCode,idProcess,quantity,unit)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def kebutuhanToolPerhari(tgl00, tgl01):
    q00 = "SELECT DISTINCT a.id AS 'idOperasi', b.id AS 'idProses',"
    q00 = q00 + "a.stasiunkerja AS StasiunKerjaOperasi,"
    q00 = q00 + "d.toolTypeCode,e.nama, d.Quantity AS jmlhbutuh, f.nama namaUnit "
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
    q00 = "SELECT EE1.nama, EE1.toolTypeCode, sum(EE1.jmlhbutuh) as butuh, EE1.stasiunKerjaOperasi "
    q00 = q00 + "from ("+q01+")EE1"
    q00 = q00 + " where EE1.stasiunKerjaOperasi='"+ws00+"' GROUP BY EE1.toolTypeCode, EE1.stasiunKerjaOperasi"
    q00 = q00 + " ORDER BY EE1.stasiunKerjaOperasi "
    return q00



def jumlahBarisKirimTool(tgl00, tgl01, ws00, cur00):
    q01 = jumlahKirimTool(tgl00, tgl01, ws00)
    q00 = "Select Count(*) from("+q01+")FF11"
    cur00.execute(q00)
    tabel00 = cur00.fetchone()
    jml00 = int(tabel00[0])
    return jml00

def insertCPLKirimTool(tgl00, tgl01, ws00, cur00,con00):
    jmlBaris = jumlahBarisKirimTool(tgl00, tgl01, ws00,cur00)
    if (jmlBaris > 0):
        q00 = jumlahKirimTool(tgl00, tgl01, ws00)
        cur00.execute(q00)
        tabel00 = cur00.fetchall()
        # print(tabel00)
        for data in tabel00:
            nama00 = data[0]
            toolType00 = data[1]
            butuh00 = data[2]
            stasiunKerja00 = data[3]
            q01 = "INSERT INTO cpl_kirimtool (namaTool, toolTypeCode, butuh, stasiunKerja) \
            VALUES ('" + nama00 + "', '" + toolType00 + "', '" + str(butuh00) + "', '" + stasiunKerja00 + "')"
            cur00.execute(q01)
            con00.commit()
    print('selesai')

def kirimTool(tgl00, tgl01, ws00, cur00,con00):
    try:
        q01 = "delete from cpl_kirimtool"
        cur00.execute(q01)
        con00.commit()
        insertCPLKirimTool(tgl00, tgl01, ws00, cur00,con00)
        con00.commit()
        hasil = True
    except Exception as e:
        hasil = False
    return hasil


def RequestKebutuhanToolByWorkstation():
    conn = database.connector()
    cursor = conn.cursor()
    data = request.json
    rencanaMulaiA = data["rencanaMulaiA"]
    rencanaMulaiB = data["rencanaMulaiB"]
    workstation = data["workstation"]
    output = kirimTool(rencanaMulaiA,rencanaMulaiB,workstation,cursor,conn)
    if output == True:
        hasil = {"status" : "berhasil"}
    else:
        hasil = {"status" : "gagal"}
    return hasil


def GetRequestToolNeedByWorkstation(workstation):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM cpl_kirimtool WHERE stasiunKerja = '"+workstation+"'"
    cursor.execute(query)

    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return  make_response(jsonify(json_data),200)

