from flask import request,make_response,jsonify
import db.db_handler as database

def AddQualification():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO opr_r_operatorqualification(id,descriptions)VALUES(%s,%s)"
    try:
        data = request.json
        id = data["id"]
        descriptions = data["descriptions"]
        values = (id,descriptions)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil
    
def AddOperator():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO opr_r_operator(id,nama,adress1,postalcode,phone,email,city)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    try:
        data = request.json
        id = data["id"]
        nama = data["nama"]
        adress1 = data["adress1"]
        postalcode = data["postalcode"]
        phone = data["phone"]
        email = data["email"]
        city = data["city"]

        values1 = (id,nama,adress1,postalcode,phone,email,city)
        cursor.execute(query,values1)
        query2 = "INSERT INTO opr_d_operatorlevel(operatorid,qualificationCode)VALUES('"+id+"',%s)"
        qualificationCode = data["qualificationCode"]
        values2 = qualificationCode
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


