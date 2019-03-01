import mysql.connector

class User:

    def __init__(self):
        pass

    def exrate(self):
        pass

    def ags(self):
        pass

class Insert:

    def __init__(self):
        pass

    def newFeedback(self):
        print("**Please insert below information**")
        CID = input("Company ID = ")
        ZAnalyst = input("Exrate analyst name = ")
        PAnalyst = input("AGS analyst name  = ")
        Ftype = input("Feedback type = ")
        Indikator = input("Indicator name = ")
        ZRemark = input("Exrate comment = ")
        # AGSRemark=""
        # Status=""
        newRow = [CID, ZAnalyst, PAnalyst, Ftype, Indikator, ZRemark]

        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="feedbacktool")

        mycursor = mydb.cursor()

        query = "INSERT INTO feedbacksheet(CompanyID,ExrateAnalyst,AGSAnalyst,FeedbackType,Indicator\
                ,ExrateRemark) VALUES(%s,%s,%s,%s,%s,%s)"

        mycursor.execute(query, newRow)
        mydb.commit()
        mydb.close()

        print("Feedback inserted successfully!")

    def editFeedback(self):
        self.all()

        print("**Which feedback you want to edit again?**")
        checkID = input("Mention company ID = ")

        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="feedbacktool")
        mycursor = mydb.cursor()
        query = "Select * from feedbacksheet WHERE CompanyID =" + str(checkID)
        mycursor.execute(query)
        result = mycursor.fetchall()
        print(result)


    def response(self):
        self.all()
        print("**Which feedback you want to edit again?**")
        checkID = input("Mention company ID = ")

        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="feedbacktool")
        mycursor = mydb.cursor()
        query = "Select * from feedbacksheet WHERE CompanyID =" + str(checkID)
        mycursor.execute(query)
        result = mycursor.fetchall()
        print(result)
        #newText = input("Insert your response = ")
        #query = "Select * from feedbacksheet WHERE CompanyID =" + str(checkID)

        print("Response inserted successfully!")
        wb.save("ft_file.xlsx")


class Check(Insert):

    def __init__(self):
        pass

    def all(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="feedbacktool")

        mycursor = mydb.cursor()

        query = "select * from feedbacksheet"
        mycursor.execute(query)
        result = mycursor.fetchall()
        # print(result)
        for r in result:
            print(r)
        mydb.close()

    def welcomeScreen(self):
        print("----Welcome to AGS Exrate Feedback Tool----")
        print("[1] Insert feedback (for Exrate analysts)")
        print("[2] Insert response (for AGS analysts)")
        print("[3] Edit feedback (for Exrate analysts)")
        print("[4] Edit response (for AGS analysts)")
        print("[5] Check FT worksheet")
        print("[0] Exit")
        infut = input("Please enter your input number = ")
        if infut== "1":
            self.newFeedback()
        elif infut == "2":
            self.response()
        elif infut == "3":
            self.editFeedback()
        elif infut == "4":
            self.editFeedback()
        elif infut == "5":
            self.all()
        elif infut == "0":
            pass

    def byUser(self):
        pass

    def byStatus(self):
        pass


if __name__ == "__main__":

    ft = Check()
    ft.welcomeScreen()
