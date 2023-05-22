import mysql.connector
def connector():
        connect = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='risproskosong')
        return connect


connector()