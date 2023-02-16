from datetime import date
import db.db_handler as database
from flask import request,make_response,jsonify


def AddToolStockByToolPurchaseItem(toolPurchaseItem):
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO eqp_d_toolstock(id,toolPurchaseItem,toolTypeCode,merk,quantity,unit,arrivalDate)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    try:

        data = request.json
        merk = data["merk"]
        quantity = data["quantity"]
        unit = data["unit"]
        arrivalDate = data["arrivalDate"]

        query_purchaseitem = "SELECT purchaseItemId,toolTypeId,quantity FROM eqp_d_toolpurchaseitem WHERE purchaseItemId = '"+toolPurchaseItem+"'"
        cursor.execute(query_purchaseitem)
        records_purchaseitem = cursor.fetchall()

        for index in records_purchaseitem:
            toolPurchaseItem = index[0]
            toolType = index[1]
            quantity_purchaseitem = index[2]
            quantity_purchaseitem = int(quantity_purchaseitem)

    
        query_getquantityunit = "SELECT multiplier FROM gen_r_materialunit WHERE id = '"+unit+"'"
        cursor.execute(query_getquantityunit)
        records_quantityunit = cursor.fetchall()

        for index in records_quantityunit:
            new_qty = index[0]
            


        query_counttooltype = "SELECT COUNT(*) FROM eqp_d_toolstock WHERE toolTypeCode LIKE '"+toolType+"'"
        cursor.execute(query_counttooltype)
        records_count = cursor.fetchall()

        for index in records_count:
            count_data = index[0]

        count_data = int(count_data)
        quantity_int = int(quantity)
        print("Qty Int : ",quantity_int)
        print("count data : ",count_data)
        
        i = 0
        tool_stock = 0   
        for i in range(quantity_int):
            
            if count_data == 0:
                id = toolType + "0000"
                values = (id,toolPurchaseItem,toolType,merk,new_qty,unit,arrivalDate)
                cursor.execute(query,values)
            else:
             
                if quantity_int >= 10:
                    count_data = count_data + 1
                    id = toolType + "00" + str(count_data)
                    values = (id,toolPurchaseItem,toolType,merk,new_qty,unit,arrivalDate)
                    cursor.execute(query,values)
                else:
                    count_data = count_data + 1
                    id = toolType + "000" + str(count_data)
                    print("ID : ",id)
                    values = (id,toolPurchaseItem,toolType,merk,new_qty,unit,arrivalDate)
                    cursor.execute(query,values)
            tool_stock = tool_stock + new_qty
        
        print("Tool Stock : ",tool_stock)
        qty_akhir = 0   
        qty_akhir = quantity_purchaseitem - tool_stock
        if qty_akhir < 0:
            qty_akhir = 0
        
        print("QTY akhir : ",qty_akhir)
        query_accumulate_quantity = "UPDATE eqp_d_toolpurchaseitem SET quantity = %s WHERE purchaseItemId = %s"
        values2 = (qty_akhir,toolPurchaseItem)
        cursor.execute(query_accumulate_quantity,values2)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def ShowToolStockNotRegisteredInBox():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id,b.nama,a.merk,a.quantity,a.unit FROM eqp_d_toolstock a JOIN eqp_r_tooltype b ON b.codes = a.toolTypeCode WHERE a.id NOT IN (SELECT b.toolStockId FROM eqp_d_boxitem b)"
    cursor.execute(query)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records :
        json_data.append(dict(zip(row_headers,data)))
  
    return make_response(jsonify(json_data),200)