"""
==============================================================
 BioSkillz CodeStart — Python Foundations | Batch 01
 Task 01: Variables, Data Types, Input, Operators & Typecasting
==============================================================

 Name     : Muhammad Asad

 Save as  : asad_task_01.py
 Deadline : Friday, 20 November 2026, 9:00 PM (PKT)
 Submit   : Upload this file to YOUR OWN GitHub repository.

 Empowering Skills | Lead with Science
"""


# ==============================================================
# PART A: SESSION EXERCISES
#
# The exercise questions are in the Session 01 recording.
# Session 01 recording (YouTube playlist): https://youtube.com/playlist?list=PLOMPeCDSq-kc&si=uY9I27bFj8yUqc00
# ==============================================================

# --------------------------------------------------------------
# Exercise 1
# --------------------------------------------------------------

# Exercise 1: predict the output
# Predictions (written before running the code):
#   1. 3.5            (/ is true division, always gives a float)
#   2. 3              (// is floor division)
#   3. 72             (+ joins two strings, it does not add them)
#   4. <class 'float'> (7.0 has a decimal point)
#   5. 50             (** first: 4**2 = 16, then 3*16 = 48, then 2+48)
#   6. True           (any non-empty string is True, even "0")

print(7 / 2)
print(7 // 2)
print("7" + "2")
print(type(7.0))
print(2 + 3 * 4 ** 2)
print(bool("0"))



# --------------------------------------------------------------
# Exercise 2
# --------------------------------------------------------------

# Exercise 2: find and fix the bugs
#
# Original buggy.py:
#   1  Name = input("Name: ")
#   2  print("Hello", name)
#   4  age = input("Age: ")
#   5  print("Next year:", age + 1)
#   7  print("Done")
#
# Bug 1: NameError on line 2.
#        The variable was created as "Name" (capital N) but used as
#        "name". Python is case-sensitive. Fix: use "name" on line 1.
# Bug 2: TypeError on line 5.
#        input() returns a string, and a string cannot be added to
#        the integer 1. Fix: convert with int(age).

name = input("Name: ")                # fixed: lowercase "name"
print("Hello", name)

age = int(input("Age: "))             # fixed: typecast to int
print("Next year:", age + 1)

print("Done")



# --------------------------------------------------------------
# Exercise 3
# --------------------------------------------------------------

# Exercise 3: Bill splitter
total_bill = int(input("Total bill: "))
friends = int(input("Number of friends: "))

print("Each pays:", total_bill // friends)
print("Left over:", total_bill % friends)

# Bonus: exact share with / compared to the // share
print("Exact share:", total_bill / friends)
print("Whole-rupee share (//):", total_bill // friends)



# ==============================================================
# PART B: TASKS
# ==============================================================

# --------------------------------------------------------------
# Task 1: Variables and Data Types
# --------------------------------------------------------------

# Four variables about myself
name = "Muhammad Asad"      # string
age = 18                    # integer
height = 1.63               # float (5'4" is about 1.63 metres)
is_student = True           # boolean

# type() tells us the data type of each value
print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))


# --------------------------------------------------------------
# Task 2: Temperature Converter (Input and Typecasting)
# --------------------------------------------------------------

# input() always returns a string, so convert it to float
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Fahrenheit:", round(fahrenheit, 2))
print("Kelvin:", round(kelvin, 2))


# --------------------------------------------------------------
# Task 3: Simple Calculator (Arithmetic Operators)
# --------------------------------------------------------------

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Power:", num1 ** num2)


# --------------------------------------------------------------
# Task 4: Savings Tracker (Assignment Operators)
# --------------------------------------------------------------

savings = 1000
print("Starting savings:", savings)

savings += 500      # gift
print("After gift:", savings)

savings -= 300      # books
print("After buying books:", savings)

savings *= 2        # doubled by year end
print("After doubling:", savings)


# --------------------------------------------------------------
# Task 5: Scholarship Check (Comparison and Logical Operators)
# --------------------------------------------------------------

marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))

marks_ok = marks >= 80
attendance_ok = attendance >= 75

print("Marks 80 or more:", marks_ok)
print("Attendance 75% or more:", attendance_ok)
print("Qualifies for scholarship:", marks_ok and attendance_ok)
