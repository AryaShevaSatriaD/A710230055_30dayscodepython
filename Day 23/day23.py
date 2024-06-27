class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def get_students(self):
        return self.students

    def get_courses(self):
        return self.courses


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        course.add_student(self)

    def get_courses(self):
        return self.courses


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        return self.students


# Contoh penggunaan
uni = University("Universitas Muhammadiyah Surakarta")
student1 = Student("upin", "001")
student2 = Student("ipin", "002")
course1 = Course("Matematika")
course2 = Course("Fisika")

uni.add_student(student1)
uni.add_student(student2)
uni.add_course(course1)
uni.add_course(course2)

student1.enroll(course1)
student2.enroll(course1)
student2.enroll(course2)

print(f"Daftar mahasiswa di {uni.name}:")
for student in uni.get_students():
    print(f"- {student.name} ({student.id})")

print(f"Daftar mata kuliah yang diambil oleh {student2.name}:")
for course in student2.get_courses():
    print(f"- {course.name}")
