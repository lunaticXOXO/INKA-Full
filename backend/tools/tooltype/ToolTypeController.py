from datetime import date
import db.db_handler as database
from flask import request,make_response,jsonify
def ShowToolType():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM eqp_r_tooltype"
    cursor.execute(query)
    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    for data in records:
        json_data.append(dict(zip(row_headers,data)))

    conn.commit()
    cursor.close()
    conn.close()

    return make_response(jsonify(json_data),200)


def AddToolTypeConsumable():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO eqp_r_tooltype(codes,nama)VALUES(%s,%s)"
    codes_default = "CT"

    today = date.today()

    year = today.year
    month = today.month

    year_str = str(year)
    months_str = str(month)
    tokens = list(year_str)
    print("Tokens : ",tokens)
    length = len(tokens)
    x = 0
    year_str_new = ''
    for x in range(length):
        if x >= length - 2:
            year_str_new = year_str_new + tokens[x]
    

    print(year_str_new)
    count = ""
    query_count_idCT = "SELECT COUNT(*) FROM eqp_r_tooltype WHERE codes LIKE 'CT%'"
    cursor.execute(query_count_idCT)
    records = cursor.fetchall()
    for index in records:
        count = index[0]

    count = int(count)
    count = count + 1
    if count > 9 and month > 9:
        codes = codes_default + year_str_new + months_str + "000" + str(count)
    
    if count > 9 and month <= 9:
        codes = codes_default +  year_str_new + "0" +  months_str + "000" + str(count)

    else:
        codes = codes_default + year_str_new + months_str + "0000" + str(count)
    
    print("codes : ", codes)
    try:
        data = request.json
        nama = data["nama"]
        values = (codes,nama)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil



def AddToolTypeNonConsumable():
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO eqp_r_tooltype(codes,nama)VALUES(%s,%s)"
    codes_default = "TS"

    today = date.today()

    year = today.year
    month = today.month

    year_str = str(year)
    months_str = str(month)
    tokens = list(year_str)
    print("Tokens : ",tokens)
    length = len(tokens)
    x = 0
    year_str_new = ''
    for x in range(length):
        if x >= length - 2:
            year_str_new = year_str_new + tokens[x]
    

    print(year_str_new)
    count = ""
    query_count_idCT = "SELECT COUNT(*) FROM eqp_r_tooltype WHERE codes LIKE 'TS%'"
    cursor.execute(query_count_idCT)
    records = cursor.fetchall()
    for index in records:
        count = index[0]

    count = int(count)
    count = count + 1
    if count > 9 and month > 9:
        codes = codes_default + year_str_new + months_str + "000" + str(count)
    
    if count > 9 and month <= 9:
        codes = codes_default +  year_str_new + "0" +  months_str + "000" + str(count)

    else:
        codes = codes_default + year_str_new + months_str + "0000" + str(count)
    
    print("codes : ", codes)
    try:
        data = request.json
        nama = data["nama"]
        values = (codes,nama)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil



