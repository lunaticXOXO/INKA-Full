import mysql.connector
def connector():
        connect = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='tesi00')
        return connect


connector()