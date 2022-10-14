import db.db_handler as db
from flask import request,make_response,jsonify

def AddSupplier():
    conn = db.connector()
    cursor = conn.cursor()

    query = "INSERT INTO gen_r_supplier(code,nama,adress1,adress2,postalcode,phone,fax,email,situs,pic,remark,city)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        data = request.json
        code = data["code"]
        nama = data["nama"]
        adress1 = data["adress1"]
        adress2 = data["adress2"]
        postalcode = data["postalcode"]
        phone = data["phone"]
        fax = data["fax"]
        email = data["email"]
        situs = data["situs"]
        pic = data["pic"]
        remark = data["remark"]
        city = data["city"]
        values = (code,nama,adress1,adress2,postalcode,phone,fax,email,situs,pic,remark,city)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil

def UpdateSupplier(code):
    conn = db.connector()
    cursor = conn.cursor()

    query = "UPDATE gen_r_supplier SET nama = %s,adress1 = %s,adress2 = %s,postalcode = %s,phone = %s,fax = %s,email = %s,situs = %s,pic = %s,remark = %s,city = %s WHERE code = '"+code+"'"
    try:
        data = request.json
        nama = data["nama"]
        adress1 = data["adress1"]
        adress2 = data["adress2"]
        postalcode = data["postalcode"]
        phone = data["phone"]
        fax = data["fax"]
        email = data["email"]
        situs = data["situs"]
        pic = data["pic"]
        remark = data["remark"]
        city = data["city"]
        values = (nama,adress1,adress2,postalcode,phone,fax,email,situs,pic,remark,city)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil

def GetSupplier():
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM gen_r_supplier"
    cursor.execute(query)
    records = cursor.fetchall()
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)



def GetSupplier():
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM gen_r_supplier"
    cursor.execute(query)
    records = cursor.fetchall()
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)
