from flask import request,make_response,jsonify,session
import db.db_handler as database
def AddNewTanggalLibur():
    conn = database.connector()
    cursor = conn.cursor()
    
    try:
        data = request.json
        hariLibur = data["hariLibur"]
        deskripsi = data["deskripsi"]
        query = "INSERT INTO gen_r_harilibur(hariLibur,deskripsi)VALUES('"+hariLibur+"','"+deskripsi+"')"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def GetAllTanggalLibur():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT * FROM gen_r_harilibur ORDER BY hariLibur ASC"
    cursor.execute(query)
    records = cursor.fetchall()

    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))

    return make_response(jsonify(json_data),200)
