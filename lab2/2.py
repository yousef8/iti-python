students_grades = {}

with open("students.txt") as students:
    try:
        for line in students:
            name, grade = line.split()
            students_grades[name] = float(grade)
    except ValueError:
        raise ValueError("student grades must be a number")

print(students_grades)

sum = 0.0
for grade in students_grades.values():
    sum += grade

print(f"Avg grades {sum / len(students_grades.values())}")

failed_students = {key: value for key, value in students_grades.items() if value < 60}
print(f"Failed Students {failed_students}")
