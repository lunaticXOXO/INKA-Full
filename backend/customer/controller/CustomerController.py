import db.db_handler as database
from flask import request,make_response,jsonify

def ShowAllCustomer():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM gen_r_customer"
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)


def ShowCustomerNames():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT nama FROM gen_r_customer"
    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    records = cursor.fetchall()

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)    


def AddNewCustomer():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO gen_r_customer(id,nama,adress1,adress2,postalcode,phone,fax,email,situs,pic,remark,city)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    try:
        data = request.json
        id = data["id"]
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
        values = (id,nama,adress1,adress2,postalcode,phone,fax,email,situs,pic,remark,city)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"Status" : "Berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil =  {"Status" : "Gagal"}
    
    return hasil


def UpdateCustomer(id):        
    conn = database.connector()
    cursor = conn.cursor()
    query = "UPDATE gen_r_customer SET nama = %s,adress1 = %s,adress2 = %s,postalcode = %s,phone = %s,fax = %s,email = %s,situs = %s,pic = %s,remark = %s,city = %s WHERE id = '"+id+"'"
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
        hasil = {"Status" : "Berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"Status" : "Gagal"}
    return hasil