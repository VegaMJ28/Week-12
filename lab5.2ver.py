
class StudentMaster:
    def __init__(self):
        self.id = ""
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
        print("\nSTUDENT INFORMATION")
        print("Student ID:",self.id)
        print("Student name:", self.name)
        print("Student major:", self.major)
        print("Student courses:", self.courses)
        print("GPA:", self.gpa)


class FacultyMaster:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""
        self.courses_taught = ""

    def create_faculty(self, faculty_id, faculty_name, faculty_department, faculty_courses):
        self.id = faculty_id
        self.name = faculty_name
        self.department = faculty_department
        self.courses_taught = faculty_courses

    def display_faculty(self):
        print("\nFACULTY INFORMATION")
        print("Faculty ID:", self.id)
        print("Faculty Name:", self.name)
        print("Department:", self.department)
        print("Courses Taught:", self.courses_taught)

myStudentsList = []
myFacultyList = []




student_data = [(101, "Edwin", "Cybersecurity", "CS 1233, Calculus", 3.8),
                (102, "Joshua", "Computer Science", "CS 1233, English", 3.5),
                (103, "Pamela", "Business", "Accounting, Economics", 3.9),
                (104, "Maria", "Cybersecurity", "Networking, CS 1233", 3.6),
                (105, "Alisson", "Engineering", "Physics, Calculus", 3.7)]

for data in student_data:
    student = StudentMaster()
    student.create_student(data[0], data[1], data[2], data[3], data[4])
    myStudentsList.append(student)




faculty_data = [(201, "Dr. Justus", "Computer Science", "Programming"),
                (202, "Dr. Varner", "Mathematics", "Calculus"),
                (203, "Prof. Yami", "Business", "Accounting"),
                (204, "Dr. Hepsiba", "Computer Science", "Cybersecurity"),
                (205, "Prof. Rob", "Engineering", "Physics")]

for data in faculty_data:
    faculty = FacultyMaster()
    faculty.create_faculty(data[0], data[1], data[2], data[3])
    myFacultyList.append(faculty)





for student in myStudentsList:
    student.display_student()

for faculty in myFacultyList:
    faculty.display_faculty()




