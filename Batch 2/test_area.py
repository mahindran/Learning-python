import mysql.connector

#CODE TO INSERT NEW FEEDBACK
# print("**Please insert below information**")
# CID = input("Company ID = ")
# ZAnalyst = input("Exrate analyst name = ")
# PAnalyst = input("AGS analyst name  = ")
# Ftype = input("Feedback type = ")
# Indikator = input("Indicator name = ")
# ZRemark = input("Exrate comment = ")
# # AGSRemark=""
# # Status=""
# newRow = [CID, ZAnalyst, PAnalyst, Ftype, Indikator, ZRemark]
#
# mydb = mysql.connector.connect(host="localhost", user="root", password="", database="feedbacktool")
#
# mycursor = mydb.cursor()
#
# query = "INSERT INTO feedbacksheet(CompanyID,ExrateAnalyst,AGSAnalyst,FeedbackType,Indicator\
#         ,ExrateRemark) VALUES(%s,%s,%s,%s,%s,%s)"
#
# mycursor.execute(query,newRow)
# mydb.commit()
# mydb.close()
#
# print("Feedback inserted successfully!")


#CODE TO EDIT FEEDBACK
# mydb = mysql.connector.connect(host="localhost",user="root",password="",database="feedbacktool")
# mycursor = mydb.cursor()
# query = "select * from feedbacksheet"
# mycursor.execute(query)
# result = mycursor.fetchall()
# count = mycursor.rowcount
# #print(count)
# for r in result:
#     print(r)
# mydb.close()
#
# print("**Which feedback you want to edit again?**")
# checkID = input("Mention company ID = ")
#
# mydb = mysql.connector.connect(host="localhost", user="root", password="", database="feedbacktool")
# mycursor = mydb.cursor()
# query = "Select * from feedbacksheet WHERE CompanyID ="+str(checkID)
# mycursor.execute(query)
# result = mycursor.fetchall()
#
# cols = ["PrimaryKey","CompanyID","ExrateAnalyst","AGSAnalyst","FeedbackType","Indicator"\
#     ,"ExrateRemark","AGSRemark","Status"]
# a = 0
# for c in result[0][0:8]:
#     i = input("Do you want to change this value? (y/n) = ")
#     if i == "y":
#         newValue = input("Enter new value = ")
#         query = "UPDATE feedbacksheet SET "+cols[a]+"= '"+newValue+"' WHERE CompanyID = "+str(checkID)
#         mycursor.execute(query)
#         mydb.commit()
#         mydb.close()
#     a=a+1

print("**Which feedback you want to respond to?**")
checkID = input("Mention company ID = ")
i1 = input("Please insert your response = ")
i2 = input("Update status = ")

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="feedbacktool")
mycursor = mydb.cursor()

query = "UPDATE feedbacksheet SET AGSRemark = '"+i1+"',Status = '"+i2+"' WHERE CompanyID = " + str(checkID)
mycursor.execute(query)
print(query)
mydb.commit()
mydb.close()

print("Response inserted successfully!")
