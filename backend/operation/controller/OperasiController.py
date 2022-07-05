import db.db_handler as database
from datetime import datetime

def GetAllOperasi():
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.id, a.rencanaMulai, a.rencanaSelesai, a.mulai, a.selesai, b.nama, c.nama, d.id FROM prd_d_operasi a "
    query = query + "JOIN prd_r_proses b ON b.id = a.proses "
    query = query + "JOIN gen_r_stasiunkerja c ON c.id = a.stasiunKerja "
    query = query + "JOIN prd_d_produk d ON d.id = a.produk"

    cursor.execute(query)
    records = cursor.fetchall()

    for data in records:
        print("ID Operasi             : ",data[0],)
        print("Rencana Mulai          : ",data[1],)
        print("Rencana Selesai        : ",data[2],)
        print("Tanggal Mulai Aktual   : ",data[3],)
        print("Tanggal Selesai Aktual : ",data[4],)
        print("Nama Proses            : ",data[5],)
        print("Nama Stasiun Kerja     : ",data[6],)
        print("ID Produk              : ",data[7],)

    return records


def AddOperasi():
    conn = database.connector()
    cursor = conn.cursor()

    id, rMulai, rSelesai, proses, stasiunKerja, produk = input("Input ID : "), input("Input Rencana Mulai : "), input("Input Rencana Selesai : "), input("Input ID Proses : "), input("Input ID Stasiun Kerja : "), input("Input ID Produk : ")

    query = "INSERT INTO prd_d_operasi (id, rencanaMulai, rencanaSelesai, mulai, proses, stasiunKerja, produk) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (id, rMulai, rSelesai, datetime.now(), proses, stasiunKerja, produk)
    cursor.execute(query,values)
    
    conn.commit()
    print("Operasi Baru Ditambahkan!")


def StopOperasi():
    conn = database.connector()
    cursor = conn.cursor()

    id = input("Input ID : ")

    query = "UPDATE prd_d_operasi SET selesai = %s WHERE id = %s"
    values = (datetime.now(), id)
    cursor.execute(query,values)
    
    conn.commit()
    print("Operasi Selesai!")