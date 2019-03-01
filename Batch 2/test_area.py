import mysql.connector

#CODE FOR NEW FEEDBACK
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


mydb = mysql.connector.connect(host="localhost",user="root",password="",database="feedbacktool")
mycursor = mydb.cursor()
query = "select * from feedbacksheet"
mycursor.execute(query)
result = mycursor.fetchall()
count = mycursor.rowcount
#print(count)
for r in result:
    print(r)
mydb.close()

print("**Which feedback you want to edit again?**")
checkID = input("Mention company ID = ")

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="feedbacktool")
mycursor = mydb.cursor()
query = "Select * from feedbacksheet WHERE CompanyID ="+str(checkID)
mycursor.execute(query)
result = mycursor.fetchall()
print(result)
mydb.close()