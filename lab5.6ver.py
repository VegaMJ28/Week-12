import mysql.connector
import streamlit as st

def init_db():
    try:
        conn = mysql.connector.connect(host="localhost", user='root', password='')
        cursor = conn.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS university_db()")
        cursor.execute("USE university_db")

        cursor.execute("""CREATE TABLE IF NOT EXISTS Student_Master(stu_id INT PRIMARY KEY, stu_name VARCHAR(100), stu_major VARCHAR(100), stu_courses VARCHAR(150), stu_cgpa FLOAT)""")

        cursor.execute("""CREATE TABLE IF NOT ECISTS Facu;ty_Master(fac_id INT PRIMARY KEY, fac_name VARCHAR(100), fac_department VARCHAR (100), fac_teaches_courses VARCHAR(150)) """)

        conn.commit()
        return conn, cursor
    except Exception as e:
        return None, None


class StudentMaster:
    def __init__(self):
        self.stu_id = 0
        self.stu_name = ""
        self.stu_major = ""
        self.stu_courses = ""
        self.stu_gpa = 0.0

    def create_student(self, stu_id, stu_name, stu_major,
                       stu_courses, stu_gpa):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_major = stu_major
        self.stu_courses = stu_courses
        self.stu_cgpa = stu_gpa

    def display_student(self):
        return {"Student ID:": self.stu_id, "Student Name:": self.stu_name, "Student Major:": self.stu_major,
                "Courses:": self.stu_courses, "GPA:": self.stu_gpa}


class FacultyMaster:
    def __init__(self):
        self.fac_id = 0
        self.fac_name = ""
        self.fac_department = ""
        self.fac_teaches_courses = ""

    def create_faculty(self, fac_id, fac_name, fac_department, fac_courses_taught):
        self.fac_id = fac_id
        self.fac_name = fac_name
        self.fac_department = fac_department
        self.fac_courses_taught = fac_courses_taught

    def display_faculty(self):
        return {"Faculty ID:": self.fac_id, "Faculty Name:": self.fac_name, "Department:": self.fac_department,
                "Course Taught:": self.fac_courses_taught}


students_list = []
student_data = [(101, "Edwin", "Cybersecurity", "CS 1233, Calculus", 3.8),
                (102, "Joshua", "Computer Science", "CS 1234, Calculus", 3.6),
                (103, "Alice", "Data Analysis", "Microeconomics", 3.7),
                (104, "Alisson", "Electrical Engineering", "Digital Electronics, Calculus 3", 3.7),
                ("Maria", "Cybersecurity", "OOP, CS1234", 3.8)]

for data in student_data:
    stu = StudentMaster()
    stu.create_student(data[0], data[1], data[2], data[3], data[4])
    students_list.append(stu)

faculty_list = []
faculty_data = [(201, "Dr.Justus", "Computer Science", "OOP"), (202, "Dr.Hepsiba", "Computer Science", "CS1233"),
                (103, "Prof.Wilkerson", "Mathematics", "Calculus 1"),
                (104, "Dr.Varner", "Engineering", "Digital Electronics, Calculus 3"),
                (105, "Prof.Lea", "Business", "Microeconomics")]

for data in faculty_data:
    fac = FacultyMaster()
    fac.create_faculty(data[0], data[1], data[2], data[3])
    faculty_list.append(fac)


def insert_student_to_db(stu_obj):
    conn,cursor = init_db()
    if conn:
        sql = "INSERT INTO Student_Master VALUES (%s,%s,%s,%s,%s)"
        val = (stu_obj.stu_id, stu_obj.stu_name, stu_obj.stu_major, stu_obj.stu_courses, stu_obj.stu_gpa)
        cursor.execute(sql, val)
        conn.commit()
        conn.close()

def insert_faculty_to_db(fac_obj):
    conn, cursor = init_db()
    if conn:
        sql = "INSERT INTO Faculty_Master VALUES (%s, %s, %s, %s, %s)"
        val = (fac_obj.fac_id, fac_obj.fac_name, fac_obj.fac_department, fac_obj.fac_teaches_courses)








st.title("UNIVERSITY MANAGEMENT")
menu = st.sidebar.radio("Navigation Menu", ["Dashboard", "View Students", "View Faculty", "Add Student", "Add Faculty"])

if menu == "Dashboard":
    st.header("DASHBOARD")
    st.write()


elif menu == "View Students":
    st.header("STUDENTS")
    col1, col2 = st.columns(2)
    col1.metric("St", len(students_list))

elif menu == "View Faculty":
    st.header("FACULTY")

elif menu == "Add Student":
    st.header("ADD A NEW STUDENT")
    stu_id = st.number_input("Student ID", min_value=100, step=1)
    stu_name = st.text_input("Student Name(stu_name)")
    stu_major = st.text_input("Student Major(stu_major)")
    stu_courses = st.text_input("Student Course(stu_courses)")
    stu_gpa = st.number_input("Student GPA(stu_gpa)")


elif menu == "Add Faculty":
    st.header("ADD A NEW FACULTY MEMBER")
    fac_id = st.number_input("Faculty ID", min_value=200, step=1)
    fac_name = st.text_input("Faculty Name(fac_name)")
    fac_department = st.text_input("Faculty Department(fac_department)")
