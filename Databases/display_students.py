from database import Student

students = Student.select()

for students in Student:
    print(students.name, students.number, students.age, students.gender, students.code)

