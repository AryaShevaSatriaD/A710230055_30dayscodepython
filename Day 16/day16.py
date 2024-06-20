# Class Person
class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def display(self):
        print(f"Nama: {self.nama}, Umur: {self.umur}")

# Class Student yang merupakan subclass dari Person
class Student(Person):
    def __init__(self, nama, umur, student_id, major):
        super().__init__(nama, umur)
        self.student_id = student_id
        self.major = major

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}, Major: {self.major}")

# Class Teacher yang merupakan subclass dari Person
class Teacher(Person):
    def __init__(self, nama, umur, employee_id, subject):
        super().__init__(nama, umur)
        self.employee_id = employee_id
        self.subject = subject

    def display(self):
        super().display()
        print(f"Employee ID: {self.employee_id}, Subject: {self.subject}")

# Membuat objek baru dari kelas Student dan Teacher
student2 = Student("Mail", 22, "S67890", "Pendidikan Teknik Informatika")
teacher2 = Teacher("Meimei", 23, "T12345", "Kalkulus")

# Menampilkan informasi student dan teacher
student2.display()
teacher2.display()
