import mysql.connector,tabulate

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
mycursor = mydb.cursor()
mycursor.execute("USE EducationSystem")

def checktableexists(tablename):
    mycursor.execute("SHOW TABLES LIKE %s", (tablename,))
    rec1 = mycursor.fetchone()
    return rec1

def course():
    if checktableexists("course"):
        pass
    else:
        mycursor.execute("CREATE TABLE course(Course_Number INT PRIMARY KEY, Course_Name VARCHAR(20), Course_Duration VARCHAR(20), Course_Mode VARCHAR(20), Course_Type VARCHAR(20), College_Name VARCHAR(20), Location VARCHAR(20), Contact_Details VARCHAR(20));")

def subscriber():
    if checktableexists("subscriber"):
        pass
    else:
        mycursor.execute("CREATE TABLE subscriber(Subscriber_Number INT, Subscriber_Name VARCHAR(20), Subscriber_Email VARCHAR(20), Subscriber_Status VARCHAR(20), Newsletter_Status VARCHAR(10));")

def addcourse():
    n = int(input("No. Records to be Added:"))
    for i in range(n):
        print("\nRecord:" + str(i + 1))
        cono = int(input("Enter Course Number:"))
        cona = input("Enter Course Name:")
        codu = input("Enter Course Duration:")
        while True:
            como = input("Enter Course Mode(Fulltime/Part-time/Distance/Online):")
            if como in ["Fulltime", "Part-time", "Distance", "Online"]:
                break
            else:
                print("Not a valid Option:")
        while True:
            coty = input("Enter Course Type(Degree/Diploma/Certification):")
            if coty in ["Degree", "Diploma", "Certification"]:
                break
            else:
                print("Not a valid Option:")
        colna = input("Enter College Name:")
        loca = input("Enter Location:")
        code = input("Enter Contact Details:")
        mycursor.execute("INSERT INTO inventory VALUES(%s, %s, %s, %s, %s, %s, %s)", (cono, cona, codu, coty, colna, loca, code))
        mydb.commit()

def addsubscriber():
    n = int(input("No. Records to be Added:"))
    for i in range(n):
        print("\nRecord:" + str(i + 1))
        suno = int(input("Enter Subscriber Number:"))
        suna = input("Enter Subscriber Name:")
        suid = input("Enter Subscriber EmailID :")
        while True:
            sust = input("Enter Subscriber Status(Active/Closed):")
            if sust in ["Active", "Closed"]:
                break
            else:
                print("Not a valid Option:")
        while True:
            nest = input("Enter Newsletter Status(Sent/Returned):")
            if nest in ["Sent", "Returned"]:
                break
            else:
                print("Not a valid Option:")
        mycursor.execute("INSERT INTO sales VALUES(%s, %s, %s, %s, %s)", (suno, suna, suid, sust, nest))
        mydb.commit()

def modify(tablename):
    tarfie = input("Enter Field to be modified:")
    if tablename == "course":
        if tarfie in ["Course_Number", "Course_Name", "Course_Duration", "Course_Mode", "Course_Type", "College_Name", "Location", "Contact_Details"]:
            tarval = eval(input("Enter Course_Number:"))
            chanval = eval(input("Enter New value:"))
            mycursor.execute("UPDATE %s SET %s=%s WHERE %s=%s" % (tablename, tarfie, chanval, "Course_Number", tarval))
            mydb.commit()
        else:
            print("Field Does not Exist")
    else:
        if tarfie in ["Subscriber_Number","Subscriber_Name", "Subscriber_Email", "Subscriber_Status", "Newsletter_Status"]:
            tarval = eval(input("Enter Subscriber_Number:"))
            chanval = eval(input("Enter New value:"))
            mycursor.execute("UPDATE %s SET %s=%s WHERE %s=%s" % (tablename, tarfie, chanval, "Subscriber_Number", tarval))
            mydb.commit()
        else:
            print("Field Does not Exist")

def search(tablename):
    if tablename == "course":
        ch = int(input("Search Using\n1.Course Number\n2.Course Name\nOption:"))
        if ch == 1:
            cono = int(input("Enter Course Number:"))
            mycursor.execute("SELECT * FROM course WHERE Course_Number=%s", (cono,))
        elif ch == 2:
            cona = input("Enter Course Name:")
            mycursor.execute("SELECT * FROM course WHERE Course_Name=%s", (cona,))
        header = ["Course Number", "Course Name", "Course Duration", "Course Mode", "Course Type", "College Name", "Location", "Contact Details"]
    else:
        ch = int(input("Search Using\n1.Subscriber Number\n2.Subscriber Name\nOption:"))
        if ch == 1:
            suno = int(input("Enter Subscriber Number:"))
            mycursor.execute("SELECT * FROM subscriber WHERE Subscriber_Number=%s", (suno,))
        elif ch == 2:
            suna = input("Enter Subscriber Name:")
            mycursor.execute("SELECT * FROM subscriber WHERE Subscriber_Name=%s", (suna,))
        header = ["Subscriber Number", "Subscriber Name", "Subscriber Email", "Subscriber Status", "Newsletter Status"]
    rec = mycursor.fetchall()    
    print(tabulate.tabulate(rec, header, tablefmt="grid"))

def delete(tablename):
    if tablename == "course":
        cono = int(input("Enter Course Number:"))
        mycursor.execute("DELETE FROM %s WHERE Course_Number=%s" % (tablename, cono))
    else:
        suno = int(input("Enter Subscriber Number:"))
        mycursor.execute("DELETE FROM %s WHERE Subscriber_Number=%s" % (tablename, suno))
    mydb.commit()
    print("Record has successfully been deleted")

def ger():
    print("\nList of Subscribers with Active Status")
    mycursor.execute("SELECT * FROM subscriber WHERE Status='Active'")
    rec = mycursor.fetchall()
    headers = ["Subscriber Number", "Subscriber Name", "Email", "Phone", "Status"]
    print(tabulate.tabulate(rec, headers, tablefmt="grid"))
        
def admin():
    while True:
        ch = int(input("--------" * 7 + "Education Management System" + "--------" * 7 + "\n\nWelcome To Education Management System\nAdmin Menu\n\t1.Course\n\t2.Subscriber\n\t3.Generate Report\n\t4.Exit\nOption:"))
        if ch == 1:
            course()
            opt = int(input("\nCourse Menu\n\t1.Add\n\t2.Modify\n\t3.Delete\n\t4.Search\nOption:"))
            if opt == 1:
                addcourse()
            elif opt == 2:
                modify("course")
            elif opt == 3:
                delete("course")
            elif opt == 4:
                search("course")
            else:
                print("Option does not exist")
        elif ch == 2:
            subscriber()
            opt = int(input("\nSubscriber Menu\n\t1.Add\n\t2.Modify\n\t3.Delete\n\t4.Search\nOption:"))
            if opt == 1:
                addsubscriber()
            elif opt == 2:
                modify("subscriber")
            elif opt == 3:
                delete("subscriber")
            elif opt == 4:
                search("subscriber")
            else:
                print("Option does not exist")
        elif ch == 3:
            ger()
        elif ch == 4:
            break
        else:
            print("Option does not exist")

admin()

