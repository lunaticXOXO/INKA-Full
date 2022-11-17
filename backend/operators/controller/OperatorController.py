from flask import request,make_response,jsonify,session
import db.db_handler as database
import hashlib

def AddQualification():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO opr_r_operatorqualification(codes,descriptions)VALUES(%s,%s)"
    try:
        data = request.json
        codes = data["codes"]
        descriptions = data["descriptions"]
        values = (codes,descriptions)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}

    return hasil


def GetQualification():
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM opr_r_operatorqualification"
    cursor.execute(query)
    records = cursor.fetchall()

    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))

    return make_response(jsonify(json_data),200)

def AddOperator():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO opd_r_operator(code,nama,adress1,postalcode,phone,email,city,username)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        data = request.json
        code = data["id"]
        nama = data["nama"]
        adress1 = data["adress1"]
        postalcode = data["postalcode"]
        phone = data["phone"]
        email = data["email"]
        city = data["city"]
        username = data['username']
        values1 = (code,nama,adress1,postalcode,phone,email,city)
        cursor.execute(query,values1)

        query2 = "INSERT INTO users(username,passwords,userType)VALUES(%s,%s,%s)"
       
        password = '12345ws'
        passwordEncrypt = hashlib.md5(password.encode('utf8')).hexdigest()
        values2 = (username,passwordEncrypt,7)
        cursor.execute(query2,values2)
        conn.commit()

        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    
    return hasil

def GetOperasiByOperatorLogin(username):
    conn = database.connector()
    cursor = conn.cursor()

    #sess = session['username']
    #print("Sess : ",sess)
    query_cek = "SELECT username FROM opd_r_operator WHERE username = '"+username+"'"
    cursor.execute(query_cek)
    records = cursor.fetchall()
    username = ""
    for data in records:
        username = data[0]
    
    #if session['username'] == username:
    query_get_operasi = "SELECT a.id,b.nama,a.rencanaMulai,a.rencanaSelesai,a.mulai,a.selesai FROM prd_d_operasi a JOIN prd_r_proses b ON b.id = a.proses JOIN gen_r_stasiunkerja c ON c.id = a.stasiunKerja WHERE c.id = '"+username+"' ORDER BY a.rencanaMulai ASC"
    cursor.execute(query_get_operasi)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)


def GetMaterialbyOperatorLogin(username):
    conn = database.connector()
    cursor = conn.cursor()
    query_cek = "SELECT username FROM opd_r_operator WHERE username = '"+username+"'"
    cursor.execute(query_cek)
    records = cursor.fetchall()
    username = ""
    for data in records:
        username = data[0]
    
    query_get_material = "SELECT nama, butuh, kurang FROM cpl_matbutuhopr WHERE stasiunKerja = '"+username+"'"
    cursor.execute(query_get_material)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)

def AddLevelByOperator(code):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT code FROM opd_r_operator WHERE code = '"+code+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    idOperator = ""
    for data in records:
        idOperator = data[0]
    query_insert = "INSERT INTO opr_d_operatorlevel(operatorid,qualificationCode)VALUES(%s,%s)"
    try:
        data = request.json
        qualificationCode = data["qualificationCode"]
        values = (idOperator,qualificationCode)
        cursor.execute(query_insert,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def AddOperatorRequirementByProcess(id):
    conn = database.connector()
    cursor = conn.cursor()

    query_select = "SELECT id FROM prd_d_process WHERE id = '"+id+"'"
    id_process = ""
    cursor.execute(query_select)
    records = cursor.fetchall()
    for index in records:
        id_process = index[0]
    
    query_insert = "INSERT INTO operatorrequirement(qualificationCode,processCode)VALUES(%s,%s)"
    try:
        data = request.json
        qualificationCode = data["qualificationCode"]
        values = (qualificationCode,id_process)
        cursor.execute(query_insert,values)
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print("Error",str(e))
    

def GetOperatorRequirementByProcess(idProcess):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id,a.prosesSesudahnya,a.nodalOutput, b.qualificationCode FROM prd_r_proses a JOIN prd_r_operatorrequirement b ON b.processCode = a.id JOIN opr_r_operatorqualification c ON c.codes = b.qualificationCode WHERE a.id = '"+idProcess+"'"
    records = cursor.fetchall()
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)





def ShowOperatorLevelbyOperator(code):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.code,a.nama,b.qualificationCode,c.descriptions FROM opd_r_operator a JOIN opr_d_operatorlevel b ON b.operatorid = a.code JOIN opr_r_operatorqualification c ON c.codes = b.qualificationCode WHERE a.code = '"+code+"'"
    cursor.execute(query)
    records = cursor.fetchall()

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)


def ShowOperator():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM opd_r_operator"
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)
