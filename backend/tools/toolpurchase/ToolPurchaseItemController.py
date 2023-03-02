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
        
        print("Tool Purchase : ", toolPurchase)


        if count < 10 and length == 1 :
            tool_purchase_item = toolPurchase + "00" + str(count)
        
        if count % 10 > 0 and length == 2:
            tool_purchase_item = toolPurchase + "0" + str(count)
        
        if count % 100 > 0 and length == 3:
            tool_purchase_item = toolPurchase + str(count)
    
        values = (tool_purchase_item,toolPurchase,toolTypeId,quantity,unit,arrivalDatePlan)
        cursor.execute(query,values)
        print("ID iTEM : ",tool_purchase_item)
      
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def ShowToolPurchaseItemByPurchase(toolPurchase):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.purchaseItemId,c.nama AS 'namaToolType', a.quantity,d.nama,a.arrivalDatePlan FROM eqp_d_toolpurchaseitem a JOIN eqp_d_toolpurchase b ON b.toolPurchaseId = a.toolPurchaseId JOIN eqp_r_tooltype c ON c.codes = a.toolTypeId JOIN gen_r_materialunit d ON d.id = a.unit WHERE b.toolPurchaseId = '"+toolPurchase+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records :
        json_data.append(dict(zip(row_headers,data)))
  
    return make_response(jsonify(json_data),200)