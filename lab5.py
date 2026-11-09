import random
class StudentMaster:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.major = ""
        self.courses = ""
        self.gpa = ""

    def create_student(self):
        self.id = random.randint(100, 199)
        self.name = input("Enter Student Name: ")
        self.major = input("Enter Major: ")


class FacultyMaster:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""
        self.courses_taught = ""

    def create_faculty(self):
        self.id = random.randint(200, 299)
        self.name = input("Enter Faculty Name: ")
        self.department = input("Enter Faculty Department: ")
        self.courses_taught = input("Enter Faculty Course Taught: ")

    




