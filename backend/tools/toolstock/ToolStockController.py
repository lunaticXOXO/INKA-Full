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
            count = index[0]

        count_data = int(count_data)
        quantity_int = int(quantity)

        total_stock = 0
        for i in range(quantity_int):   
            if count == 0:
                id = toolType + "0000"
                values = (id,toolPurchaseItem,toolType,merk,new_qty,unit,arrivalDate)
                cursor.execute(query,values)
            else:
                i = 0
                if quantity_int >= 10:
                    count_data = count_data + i
                    id = toolType + count
                    values = (id,toolPurchaseItem,toolType,merk,new_qty,unit,arrivalDate)
                    cursor.execute(query,values)
                else:
                    count_data = count_data + i
                    id = toolType + count
                    values = (id,toolPurchaseItem,toolType,merk,new_qty,unit,arrivalDate)
                    cursor.execute(query,values)
                    
            query_updateUnit = "UPDATE eqp_d_toolstock SET unit = U01 WHERE toolPurchaseItem = '"+toolPurchaseItem+"'"
            cursor.execute(query_updateUnit)
            total_stock = total_stock + int(new_qty)
        
        
        qty_akhir = 0   
        qty_akhir = quantity_purchaseitem - total_stock
        if qty_akhir < 0:
            qty_akhir = 0
        
        query_accumulate_quantity = "UPDATE eqp_d_toolpurchaseitem SET quantity = '"+qty_akhir+"' WHERE purchaseItemId = '"+toolPurchaseItem+"'"
        cursor.execute(query_accumulate_quantity)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil
