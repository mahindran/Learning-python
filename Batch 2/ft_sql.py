import mysql.connector
#from mysql.connector import Error



mydb = mysql.connector.connect(host="localhost",user="root",password="",database="feedbacktool")

mycursor = mydb.cursor()

query = "INSERT INTO feedbacksheet(CompanyID,ExrateAnalyst,AGSAnalyst,FeedbackType,Indicator\
,ExrateRemark) VALUES('110223','MAL','svijaya','re-research','PA','check parameters')"

mycursor.execute(query)
mydb.commit()
mydb.close()

mydb = mysql.connector.connect(host="localhost",user="root",password="",database="feedbacktool")

mycursor = mydb.cursor()

query = "select * from feedbacksheet"
mycursor.execute(query)
result = mycursor.fetchall()
# print(result)
for r in result:
    print(r)
mydb.close()


