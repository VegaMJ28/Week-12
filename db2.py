import mysql.connector
from mysql.connector import cursor

mydb = mysql.connector.connect(host="localhost", user="root", passwd="")
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE StudentsDB")
#print("Database created successfully")
#mydb.close()

mycursor.execute("""CREATE TABLE IF NOT EXISTS Student(StudentID INT PRIMARY KEY, Name VARCHAR(50),Department VARCHAR(50))""")
print("Student Table created successfully")

def insert_student():
    sid = int(input("Enter Student ID:"))
    name = input("Enter Student Name:")
    department = input("Enter Department:")
    sql = "INSERT INTO Student VALUES (%s, %s, %s)"
    values = (sid, name, department)
    mycursor.execute(sql, values)
    mydb.commit()
    print("Student inserted successfully")

def display_students():
    cursor.execute("SELECT * FROM Student")
    for row in mycursor.fetchall():
        print(row)

def update_student():
    sid = int(input("Enter Student ID:"))
    name = input("Enter Student New Name:")
    department = input("Enter Student New Department:")
    sql = ""
        UPDATE Student
        SET Name = %s, Department = %s, WHERE Student_id = %s """cursor.execute(sql, (name, dept"""