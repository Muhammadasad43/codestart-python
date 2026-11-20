"""
==============================================================
 BioSkillz CodeStart — Python Foundations | Batch 01
 Task 02: Strings & Conditional Statements
==============================================================

 Name     : Muhammad Asad

 Save as  : asad_task_02.py
 Deadline : Friday, 20 November 2026, 9:00 PM (PKT)
 Submit   : Upload this file to YOUR OWN GitHub repository.

 Empowering Skills | Lead with Science
"""


# ==============================================================
# PART A: SESSION EXERCISES
#
# The exercise questions are in the Session 02 recording.
# Session 02 recording (YouTube playlist): https://youtube.com/playlist?list=PLOMPeCDSq-kc&si=uY9I27bFj8yUqc00
# ==============================================================

# --------------------------------------------------------------
# Exercise 1
# --------------------------------------------------------------

# Exercise 1: predict the output
# Predictions (written before running the code):
#   1. yth     ([1:4] takes index 1, 2, 3 -> "y", "t", "h")
#   2. 2       ("banana" has "an" twice: ba-AN-AN-a)
#   3. o       (index -1 is the last character)
#   4. True    (uppercase "Z" = 90 comes before lowercase "a" = 97)
#   5. False   (5 > 3 is True, but 2 > 4 is False, so True and False)
#   6. True    (an empty string is False, so "not" makes it True)

print("Python"[1:4])
print("banana".count("an"))
print("Hello"[-1])
print("Zebra" < "apple")
print(5 > 3 and 2 > 4)
print(not "")



# --------------------------------------------------------------
# Exercise 2
# --------------------------------------------------------------

# Exercise 2: find and fix 4 bugs
#
# Original buggy.py:
#   1  marks = int(input("Marks: "))
#   2  if marks >= 50
#   3      print("Pass")
#   4  else:
#   5  print("Fail")
#   6
#   7  answer = input("Again? ")
#   8  if answer = "yes":
#   9      print("Restarting...")
#
# Bug 1: SyntaxError on line 2.
#        The if statement is missing a colon. Fix: if marks >= 50:
# Bug 2: IndentationError on line 5.
#        The print("Fail") under else is not indented.
#        Fix: indent it by 4 spaces.
# Bug 3: SyntaxError on line 8.
#        A single = assigns a value; comparing needs ==.
#        Fix: if answer == "yes":
# Bug 4 (bonus): No error message, but a logic bug.
#        Typing "Yes" with a capital Y does nothing, because
#        "Yes" == "yes" is False (strings are case-sensitive).
#        Fix: use answer.lower() so any capitalisation works.

marks = int(input("Marks: "))
if marks >= 50:                         # fixed: colon added
    print("Pass")
else:
    print("Fail")                       # fixed: indented

answer = input("Again? ")
if answer.lower() == "yes":             # fixed: == and .lower()
    print("Restarting...")



# --------------------------------------------------------------
# Exercise 3
# --------------------------------------------------------------

# Exercise 3: Student Grader
student = input("Student name: ").strip().title()   # clean the name
marks_text = input("Marks (0-100): ").strip()

if marks_text.isdigit():                 # check it is a number
    score = int(marks_text)
    if score > 100:                      # bonus: marks above 100
        print("Marks must be 0-100")
    else:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 50:
            grade = "D"
        else:
            grade = "F"
        print(f"{student} scored {score}/100 → Grade {grade}")
else:
    print("Please enter marks as a whole number")



# ==============================================================
# PART B: TASKS
# ==============================================================

# --------------------------------------------------------------
# Task 1: Name Formatter (String Methods)
# --------------------------------------------------------------

full_name = input("Enter your full name: ")

print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Title case:", full_name.title())
print("Total characters:", len(full_name))
print("Number of 'a':", full_name.lower().count("a"))


# --------------------------------------------------------------
# Task 2: Email Breakdown (Indexing and Slicing)
# --------------------------------------------------------------

email = input("Enter your email: ")

at_pos = email.find("@")    # position of "@", reused in the slices

print("First character:", email[0])
print("Last character:", email[-1])
print("Position of @:", at_pos)
print("Username:", email[:at_pos])
print("Domain:", email[at_pos + 1:])
print("Gmail address:", email.endswith("gmail.com"))


# --------------------------------------------------------------
# Task 3: Report Card (f-strings and Typecasting)
# --------------------------------------------------------------

student_name = input("Enter your name: ")
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

total = subject1 + subject2 + subject3
percentage = (total / 300) * 100

print("----- Report Card -----")
print(f"Name: {student_name}")
print(f"Total: {total} out of 300")
print(f"Percentage: {percentage:.2f}%")


# --------------------------------------------------------------
# Task 4: Grade Calculator (if, elif and else)
# --------------------------------------------------------------

grade_marks = int(input("Enter your marks: "))

if grade_marks < 0 or grade_marks > 100:    # invalid check comes first
    print("Invalid marks")
elif grade_marks >= 85:
    print("Grade: A")
elif grade_marks >= 70:
    print("Grade: B")
elif grade_marks >= 55:
    print("Grade: C")
elif grade_marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")


# --------------------------------------------------------------
# Task 5: Login Checker (Nested Conditions)
# --------------------------------------------------------------

username = input("Enter username: ").strip().lower()   # not case-sensitive
password = input("Enter password: ")                   # case-sensitive

if username == "codestart":
    if password == "python123":
        print("Login successful. Welcome to CodeStart!")
    else:
        print("Incorrect password. Please try again.")
else:
    print("Username not found.")
