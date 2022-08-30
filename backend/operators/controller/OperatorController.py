from flask import request,make_response,jsonify
import db.db_handler as database

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
    records = cursor.fetchall()

    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))

    return make_response(jsonify(json_data),200)

def AddOperator():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO opd_r_operator(code,nama,adress1,postalcode,phone,email,city)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    try:
        data = request.json
        code = data["id"]
        nama = data["nama"]
        adress1 = data["adress1"]
        postalcode = data["postalcode"]
        phone = data["phone"]
        email = data["email"]
        city = data["city"]

        values1 = (code,nama,adress1,postalcode,phone,email,city)
        cursor.execute(query,values1)

        query2 = "INSERT INTO users(username,passwords,userType)VALUES(%s,%s,%s)"
        username = data['username']
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
