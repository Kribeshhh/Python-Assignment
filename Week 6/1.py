class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


students = []

for i in range(3):
    print(f"\nEnter details for Student {i+1}")
    name = input("Name: ")
    age = int(input("Age: "))

    grades = []
    for j in range(3):
        grade = int(input(f"Grade {j+1}: "))
        grades.append(grade)

    students.append(Student(name, age, grades))

print("\nAverage Grades:")
for student in students:
    print(student.name, ":", student.average_grade())