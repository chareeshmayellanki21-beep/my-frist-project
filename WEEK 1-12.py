# week1_student.py

name = input("Enter student name: ").strip()

while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Marks must be between 0 and 100!")
    except:
        print("Invalid input!")

print(f"\nHi {name}, Your marks: {marks}")

# week2_menu.py

def menu():
    print("\n--- STUDENT SYSTEM ---")
    print("1. Add Marks")
    print("2. View Marks")
    print("3. Exit")

marks = []

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == '1':
        m = int(input("Enter marks: "))
        marks.append(m)
    elif choice == '2':
        print("Marks List:", marks)
    elif choice == '3':
        break
    else:
        print("Invalid choice!")

# week3_grade.py

marks = int(input("Enter marks: "))

if marks >= 90:
    grade = 'A'
elif marks >= 75:
    grade = 'B'
elif marks >= 50:
    grade = 'C'
else:
    grade = 'Fail'

print("Grade:", grade)

# week4_functions.py

def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 50:
        return 'C'
    else:
        return 'Fail'

marks = int(input("Enter marks: "))
print("Grade:", calculate_grade(marks))

# week5_dict.py

student = {
    "name": input("Enter name: "),
    "marks": int(input("Enter marks: "))
}

def show_student(s):
    for key, value in s.items():
        print(f"{key}: {value}")

show_student(student)

# week6_oop.py

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_marks(self, m):
        self.marks.append(m)

    def average(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Sai")

s1.add_marks(80)
s1.add_marks(90)

print("Average:", s1.average())

# week7_inheritance.py

class Student:
    def __init__(self, name):
        self.name = name

class SchoolStudent(Student):
    def grade(self, marks):
        return 'Pass' if marks >= 50 else 'Fail'

s = SchoolStudent("Sai")
print(s.grade(9))

# week8_file.py

def save_data(name, marks):
    with open("students.txt", "a") as f:
        f.write(f"{name},{marks}\n")

def view_data():
    try:
        with open("students.txt", "r") as f:
            for line in f:
                print(line.strip())
    except:
        print("No data found!")

save_data("cherry", 85)
view_data()

# student_module.py

def welcome():
    print("Welcome to Academic Tracker 🎓")

# week10_numpy.py

import numpy as np

marks = np.array([80, 90, 70, 85])

print("Average:", np.mean(marks))
print("Max:", np.max(marks))
print("Min:", np.min(marks))

# week11_pandas.py

import pandas as pd

data = {
    "Name": ["Sai", "Ram", "Krishna"],
    "Marks": [85, 90, 75]
}

df = pd.DataFrame(data)
print(df.sort_values(by="Marks", ascending=False))

# week12_visual.py

import matplotlib.pyplot as plt

students = ["Sai", "Ram", "Krishna"]
marks = [85, 90, 75]

plt.bar(students, marks)
plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

