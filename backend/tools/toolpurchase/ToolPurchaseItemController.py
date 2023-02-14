from datetime import date
import db.db_handler as database
from flask import request,make_response,jsonify


def AddToolPurchaseItemByToolPurchase(toolPurchase):
    conn = database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO eqp_d_toolpurchaseitem(purchaseItemId,toolPurchaseId,toolTypeId,quantity,unit,arrivalDatePlan)VALUES(%s,%s,%s,%s,%s,%s)"
    try:
        data = request.json

        toolTypeId = data["toolTypeId"]
        quantity = data["quantity"]
        unit = data["unit"]
        arrivalDatePlan = data["arrivalDatePlan"]

        query_countiditem = "SELECT COUNT(*) FROM eqp_d_toolpurchaseitem"
        cursor.execute(query_countiditem)
        records_count = cursor.fetchall()
        count = ""
        for index in records_count:
            count = index[0]
            count = int(count)

        count = count + 1
        length = len(str(count))
        length = int(length)

        query_purchase = "SELECT toolPurchaseId FROM eqp_d_toolpurchase WHERE toolPurchaseId = '"+toolPurchase+"'"
        cursor.execute(query_purchase)
        toolPurchase = ""
        records_purchase = cursor.fetchall()
        for index in records_purchase:
            toolPurchase = index[0]

        if count < 10 and length == 1 :
            tool_purchase_item = toolPurchase + "00" + str(count)
        
        if count % 10 > 0 and length == 2:
            tool_purchase_item = toolPurchase + "0" + str(count)
        
        if count % 100 > 0 and length == 3:
            tool_purchase_item = toolPurchase + str(count)
        

        

        values = (tool_purchase_item,toolPurchase,toolTypeId,quantity,unit,arrivalDatePlan)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil