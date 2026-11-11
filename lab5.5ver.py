import streamlit as st

class StudentMaster:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.major = ""
        self.courses = ""
        self.gpa = 0.0

    def create_student(self, student_id, student_name, student_major,
                       student_courses, student_gpa):
        self.id = student_id
        self.name = student_name
        self.major = student_major
        self.courses = student_courses
        self.gpa = student_gpa

    def display_student(self):
        return{"Student ID:":self.id,"Student Name:":self.name,"Student Major:":self.major,"Courses:":self.courses,"GPA:":self.gpa}


class FacultyMaster:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.department = ""
        self.courses_taught = ""

    def create_faculty(self, faculty_id, faculty_name, faculty_department, faculty_courses):
        self.id = faculty_id
        self.name = faculty_name
        self.department = faculty_department
        self.courses_taught = faculty_courses

    def display_faculty(self):
        return{"Faculty ID:":self.id, "Faculty Name:":self.name, "Department:":self.department,"Course Taught:":self.courses_taught}



students_list = []
student_data = [(101, "Edwin", "Cybersecurity", "CS 1233, Calculus", 3.8), (102, "Joshua", "Computer Science", "CS 1234, Calculus", 3.6), (103, "Alice", "Data Analysis", "Microeconomics", 3.7), (104, "Alisson", "Electrical Engineering", "Digital Electronics, Calculus 3", 3.7), ("Maria", "Cybersecurity", "OOP, CS1234", 3.8)]

for data in student_data:
    stu = StudentMaster()
    stu.create_student(data[0], data[1], data[2], data[3], data[4])
    students_list.append(stu)

faculty_list = []
faculty_data = [(201, "Dr.Justus", "Computer Science", "OOP"), (202, "Dr.Hepsiba", "Computer Science", "CS1233"), (103, "Prof.Wilkerson", "Mathematics", "Calculus 1"), (104, "Dr.Varner", "Engineering", "Digital Electronics, Calculus 3"), (105, "Prof.Lea", "Business", "Microeconomics")]

for data in faculty_data:
    fac = FacultyMaster()
    fac.create_faculty(data[0], data[1], data[2], data[3])
    faculty_list.append(fac)



st.title("UNIVERSITY MANAGEMENT")
menu = st.sidebar.radio("Navigation Menu",["Dashboard", "View Students", "View Faculty", "Add Student", "Add Faculty"])

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
    