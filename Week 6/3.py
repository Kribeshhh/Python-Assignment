class StudentResult:
    def __init__(self, name, age, average_grade):
        self.name = name
        self.age = age
        self.average_grade = average_grade

    def has_passed(self):
        return self.average_grade >= 50


students = []

for i in range(3):
    print(f"\nEnter details for Student {i+1}")
    name = input("Name: ")
    age = int(input("Age: "))
    average_grade = float(input("Average Grade: "))

    students.append(StudentResult(name, age, average_grade))

print("\nStudents Who Passed:")
for student in students:
    if student.has_passed():
        print(student.name)