# ============================================================
#  BioSkillz CodeStart — Python Foundations | Batch 01
#  TASK 04: Lists & Tuples (Session 04)
# ============================================================
#
#  Name            : Muhammad Asad
#  GitHub username : Muhammadasad43
#  Date            : 27 November 2026
#
#  DEADLINE: Friday, 27 November 2026, 9:00 PM (PKT)
# ============================================================


# ############################################################
#  PART A: SESSION EXERCISES (from the slides)
# ############################################################

# ------------------------------------------------------------
# Exercise 1: Predict the output
# ------------------------------------------------------------
# 1)  nums = [3, 1, 2]
#     nums.append(5)
#     print(nums)
#     My prediction: [3, 1, 2, 5]
#
# 2)  print([10, 20, 30, 40][1:3])
#     My prediction: [20, 30]  (index 1 up to, not including, 3)
#
# 3)  a = [1, 2]
#     b = a
#     b.append(3)
#     print(a)
#     My prediction: [1, 2, 3]  (b is not a copy, it is the same list as a)
#
# 4)  x = [5, 2, 8]
#     print(x.sort())
#     My prediction: None  (sort() changes the list in place and returns None)
#
# 5)  t = (5,)
#     print(type(t))
#     My prediction: <class 'tuple'>  (the comma makes it a tuple)
#
# 6)  print(len([[1, 2], [3, 4]]))
#     My prediction: 2  (two inner lists)

print("--- Exercise 1 ---")

nums = [3, 1, 2]
nums.append(5)
print(nums)

print([10, 20, 30, 40][1:3])

a = [1, 2]
b = a
b.append(3)
print(a)

x = [5, 2, 8]
print(x.sort())

t = (5,)
print(type(t))

print(len([[1, 2], [3, 4]]))


# ------------------------------------------------------------
# Exercise 2: Find and fix 4 bugs
# ------------------------------------------------------------
# Original buggy program:
#
#     marks = [72, 95, 64]
#     marks.append(88, 50)
#     print("Last:", marks[5])
#
#     best = marks.sort()
#     print("Sorted:", best)
#
#     point = (3, 4)
#     point[0] = 5

print("--- Exercise 2 ---")

marks = [72, 95, 64]
marks.append(88)            # Bug 1 (TypeError): append() takes only ONE item.
marks.append(50)            # Add 88 and 50 with two separate append() calls.
print("Last:", marks[-1])   # Bug 2 (IndexError): the list has 5 items, so the last index is 4,
                            # not 5. marks[-1] always gives the last item.

marks.sort()                # Bug 3 (wrong result, no error): sort() changes the list in place
print("Sorted:", marks)     # and returns None, so best = marks.sort() made best equal None.
                            # Sort first, then print the list itself.

point = (3, 4)
point = (5, point[1])       # Bug 4 (TypeError): tuples cannot be changed. To "change" one,
print("Point:", point)      # build a new tuple.


# ------------------------------------------------------------
# Exercise 3: To-do list manager
# ------------------------------------------------------------
print("--- Exercise 3 ---")

tasks = []

while True:
    print("1) Add 2) Remove 3) Show 4) Quit")
    choice = input("Choose: ").strip()

    if choice == "1":
        task = input("Task: ").strip()
        tasks.append(task)
    elif choice == "2":
        task = input("Task: ").strip()
        if task in tasks:
            tasks.remove(task)
        else:
            print("That task is not in the list")
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks yet")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
    elif choice == "4":
        break
    else:
        print("Please choose 1, 2, 3 or 4")


# ############################################################
#  PART B: TASKS
# ############################################################

# ------------------------------------------------------------
# Task 1: List explorer
# ------------------------------------------------------------
print("--- Task 1 ---")

parts = input("Enter 5 numbers: ").split()

numbers_list = []
for p in parts:
    numbers_list.append(int(p))

print("Sorted :", sorted(numbers_list))
print("Sum    :", sum(numbers_list))
print("Average:", sum(numbers_list) / len(numbers_list))
print("Largest:", max(numbers_list))
print("Smallest:", min(numbers_list))


# ------------------------------------------------------------
# Task 2: Predict the output
# ------------------------------------------------------------
# 1)  print([1, 2, 3] * 2)
#     My prediction: [1, 2, 3, 1, 2, 3]  (* repeats the list)
#
# 2)  x = [4, 7, 1]
#     x.insert(1, 9)
#     print(x)
#     My prediction: [4, 9, 7, 1]  (insert puts 9 at index 1)
#
# 3)  y = [1, 2, 2, 3]
#     y.remove(2)
#     print(y)
#     My prediction: [1, 2, 3]  (remove() deletes only the first 2)
#
# 4)  print(sorted([3, 1, 2], reverse=True))
#     My prediction: [3, 2, 1]
#
# 5)  a, b, c = (1, 2, 3)
#     print(b)
#     My prediction: 2  (tuple unpacking)
#
# 6)  print(" ".join(["Code", "Start"]))
#     My prediction: Code Start

print("--- Task 2 ---")

print([1, 2, 3] * 2)

x = [4, 7, 1]
x.insert(1, 9)
print(x)

y = [1, 2, 2, 3]
y.remove(2)
print(y)

print(sorted([3, 1, 2], reverse=True))

a, b, c = (1, 2, 3)
print(b)

print(" ".join(["Code", "Start"]))


# ------------------------------------------------------------
# Task 3: Find and fix the bugs
# ------------------------------------------------------------
# Original buggy program:
#
#     names = ["ali", "sara", "omar"]
#     names.add("zara")
#
#     for i in range(len(names) + 1):
#         print(names[i].title())
#
#     names.remove("Sara")
#     print("Total:", len(names)

print("--- Task 3 ---")

names = ["ali", "sara", "omar"]
names.append("zara")                    # Bug 1 (AttributeError): lists have append(), not add().

for i in range(len(names)):             # Bug 2 (IndexError): len(names) + 1 goes one index past
    print(names[i].title())             # the end. Use range(len(names)).

names.remove("sara")                    # Bug 3 (ValueError): the list holds "sara" in lowercase,
                                        # and remove() is case-sensitive, so "Sara" is not found.
print("Total:", len(names))             # Bug 4 (SyntaxError): the closing bracket ")" was missing.


# ------------------------------------------------------------
# Task 4: Remove duplicates (without sets)
# ------------------------------------------------------------
print("--- Task 4 ---")

numbers = [3, 7, 3, 9, 7, 1, 3]
unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)


# ------------------------------------------------------------
# Task 5: Your field  (Option A: Codons)
# ------------------------------------------------------------
print("--- Task 5 ---")

dna = input("Enter a DNA sequence: ").strip().upper()

codons = []
for i in range(0, len(dna) - 2, 3):     # step of 3; stops before an incomplete last codon
    codons.append(dna[i:i + 3])

print(codons, "->", len(codons), "codons")
