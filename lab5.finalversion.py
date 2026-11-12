import mysql.connector
import streamlit as st
def init_db():
    conn = mysql.connector.connect(host="localhost",user="root",password="")
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS university_db_lab5")
    cursor.execute("USE university_db_lab5")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Student_Master (stu_id INT PRIMARY KEY, stu_name VARCHAR(100), stu_major VARCHAR(100), stu_courses VARCHAR(150), stu_cgpa FLOAT)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Faculty_Master (fac_id INT PRIMARY KEY, fac_name VARCHAR(100), fac_department VARCHAR(100), fac_teaches_courses VARCHAR(150))""")
    conn.commit()
    return conn, cursor


class Student_Master:
    def __init__(self):
        self.stu_id = 0
        self.stu_name = ""
        self.stu_major = ""
        self.stu_courses = ""
        self.stu_cgpa = 0.0

    def create_student(self, stu_id, stu_name, stu_major, stu_courses, stu_cgpa):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_major = stu_major
        self.stu_courses = stu_courses
        self.stu_cgpa = stu_cgpa

    def display_student(self):
        print(f"ID: {self.stu_id} | Name: {self.stu_name} | Major: {self.stu_major}")

class Faculty_Master:
    def __init__(self):
        self.fac_id = 0
        self.fac_name = ""
        self.fac_department = ""
        self.fac_teaches_courses = ""

    def create_faculty(self, fac_id, fac_name, fac_department, fac_teaches_courses):
        self.fac_id = fac_id
        self.fac_name = fac_name
        self.fac_department = fac_department
        self.fac_teaches_courses = fac_teaches_courses

    def display_faculty(self):
        print(f"ID: {self.fac_id} | Name: {self.fac_name} | Dept: {self.fac_department}")


def insert_student_to_db(stu_obj):
    conn, cursor = init_db()
    sql = "INSERT INTO Student_Master VALUES (%s, %s, %s, %s, %s)"
    val = (stu_obj.stu_id, stu_obj.stu_name, stu_obj.stu_major, stu_obj.stu_courses, stu_obj.stu_cgpa)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()

def insert_faculty_to_db(fac_obj):
    conn, cursor = init_db()
    sql = "INSERT INTO Faculty_Master VALUES (%s, %s, %s, %s)"
    val = (fac_obj.fac_id, fac_obj.fac_name, fac_obj.fac_department, fac_obj.fac_teaches_courses)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()

def fetch_students_from_db():
    conn, cursor = init_db()
    if conn:
        cursor.execute("SELECT * FROM Student_Master")
        rows = cursor.fetchall()
        conn.close()
        return rows
    return []

def fetch_faculty_from_db():
    conn, cursor = init_db()
    if conn:
        cursor.execute("SELECT * FROM Faculty_Master")
        rows = cursor.fetchall()
        conn.close()
        return rows
    return[]


st.title("University Management System")

menu = st.sidebar.radio("Main Menu",["Dashboard", "Add Student", "Add Faculty", "View Students", "View Faculty"])

if menu == "Dashboard":
    st.header("Setup")
    st.write("University Management System")
    st.info("Use side menu to create Students and Faculty members")

elif menu == "Add Student":
    st.header("Create New Student")
    stu_id = st.number_input("Student ID", min_value=1, step=1)
    stu_name = st.text_input("Student Name")
    stu_major = st.text_input("Major")
    stu_courses = st.text_input("Courses")
    stu_cgpa = st.number_input("CGPA", min_value=0.0, max_value=4.0, step=0.1)

    if st.button("Save Student to Database"):
        if stu_name != "" and stu_major != "":
            try:
                new_stu = Student_Master()
                new_stu.create_student(stu_id, stu_name, stu_major, stu_courses, stu_cgpa)
                insert_student_to_db(new_stu)
                st.success(f"Student '{stu_name}' saved.")
            except Exception as e:
                st.error(f"Student '{stu_name}' already exists.")
        else:
            st.warning("Please fill in the information.")

elif menu == "Add Faculty":
    st.header("Create New Faculty")
    fac_id = st.number_input("Faculty ID ", min_value=1, step=1)
    fac_name = st.text_input("Faculty Name ")
    fac_department = st.text_input("Department")
    fac_teaches = st.text_input("Courses Taught )")

    if st.button("Save Faculty to Database"):
        if fac_name.strip() != "" and fac_department.strip() != "":
            try:
                new_fac = Faculty_Master()
                new_fac.create_faculty(fac_id, fac_name, fac_department, fac_teaches)
                insert_faculty_to_db(new_fac)
                st.success(f"Faculty '{fac_name}' saved.")
            except Exception as e:
                st.error(f"Faculty '{fac_name}' already exists.")
        else:
            st.warning("Please fill in the information.")

elif menu == "View Students":
    st.header("Students in DB")
    rows = fetch_students_from_db()
    if rows:
        st.table(rows)
    else:
        st.info("No students in database yet.")

elif menu == "View Faculty":
    st.header("Faculty in DB")
    rows = fetch_faculty_from_db()
    if rows:
        st.table(rows)
    else:
        st.info("No faculty in database yet.")