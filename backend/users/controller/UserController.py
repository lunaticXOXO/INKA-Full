import db.db_handler as database
from flask import request,session
import hashlib

def Login():
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = %s AND passwords = %s"
    
    data = request.json
    username = data["username"]
    passwords = data["passwords"]
    passwords = hashlib.md5(passwords.encode('utf8')).hexdigest()
    values = (username,passwords)
    cursor.execute(query,values)
    user = cursor.fetchall()

    userType = 0
    for data in user:
        userType = int(data[2])
        
    if user:
        session['loggedin'] = True
        session['username'] = username
        hasil = {"status" : "berhasil",
                 "userType" : userType}
    else:
        hasil = {"status" : "gagal"}
    return hasil


def Logout():
    try:
        session.pop('loggedin', None)
        session.pop('username', None)
        hasil = {"status" : "berhasil"}
    except:
        hasil = {"status" : "gagal"}
    return hasil


def Register():
    conn = database.connector()
    cursor = conn.cursor() 

    query = "INSERT INTO users(username,passwords,userType)VALUES(%s,%s,%s)"
    try:
        data = request.json
        username = data["username"]
        passwords = data["passwords"]
        userType = data["userType"]
        passwords = hashlib.md5(passwords.encode('utf8')).hexdigest()
        values = (username,passwords,userType)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


