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
    sess = session['username']
    query_cek = "SELECT username FROM opd_r_operator WHERE username = '"+sess+"'"
    cursor.execute(query_cek)
    records = cursor.fetchall()
    username = ""
    for data in records:
        username = data[0]
    
    if session['username'] == username:
        query_get_operasi = "SELECT * FROM opr_d_operatorneed a JOIN prd_d_operasi b ON b.id = a.operationid JOIN opd_r_operator c ON c.code = a.operatorid WHERE c.username = '"+username+"'"
        cursor.execute(query_get_operasi)
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
