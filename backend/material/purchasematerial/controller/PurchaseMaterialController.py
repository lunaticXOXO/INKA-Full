import db.db_handler as database
from flask import request,make_response,jsonify

def PurchaseMaterial():
    conn = database.connector()
    cursor = conn.cursor()

    query = "INSERT INTO mat_d_purchasematerial(id,nama,purchaseName,purchaseDate)VALUES(%s,%s,%s,%s)"
    try:
        data = request.json
        id = data["id"]
        nama = data["nama"]
        purchaseName = data["purchaseName"]
        purchaseDate = data["purchaseDate"]
        values = (id,nama,purchaseName,purchaseDate)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil