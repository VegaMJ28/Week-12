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
student_data = [(101, "Edwin", "Cybersecurity", "CS 1233, Calculus", 3.8), ]

for data in student_data:
    stu = StudentMaster()
    stu.create_student(data[0], data[1], data[2], data[3], data[4])
    students_list.append(stu)

faculty_list = []




st.title("UNIVERSITY MANAGEMENT")
menu = st.sidebar.radio("Navigation Menu",["D

if menu == "D
    st.h
    st.wr

    col1,col2 = st.columns(2)
    col1.metric ("St",len(students_list))


elif menu == "Add"
    st.h

    stu_id = st.number_input("Student ID",min_value=1,step=1)
    stu_name = st.text_input("Student Name(stu_name)")